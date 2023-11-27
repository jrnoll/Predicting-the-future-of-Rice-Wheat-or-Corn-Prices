import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd


def outlier_thresholds(dataframe, col_name):
    quartile1 = dataframe[col_name].quantile(0.25)
    quartile3 = dataframe[col_name].quantile(0.75)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False


def replace_with_thresholds(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if low_limit > 0:
        dataframe.loc[(dataframe[col_name] < low_limit), col_name] = low_limit
        dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit
    else:
        dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit


def transform_data():
    s3 = S3FileSystem()
    # S3 bucket directory (data lake)
    DIR = 's3://ece5984-bucket-jrnoll/Project'  # Insert here
    # Get data from S3 bucket as a pickle file
    raw_data = np.load(s3.open('{}/{}'.format(DIR, 'data.pkl')), allow_pickle=True)

    # raw_data = np.load('data.pkl', allow_pickle=True)
    # Dividing the raw dataset for each company individual product
    print("1st raw data!")
    print(raw_data['Price_wheat_ton_infl'])
    # raw_data.columns = raw_data.columns.swaplevel(0, 1)
    # raw_data.sort_index(axis=1, level=0, inplace=True)
    df_wheat_rw = raw_data[['Year', 'Month', 'Price_wheat_ton', 'Price_wheat_ton_infl', 'Inflation_rate']]
    df_corn_rw = raw_data[['Year', 'Month', 'Price_corn_ton', 'Price_corn_ton_infl', 'Inflation_rate']]
    df_rice_rw = raw_data[['Year', 'Month', 'Price_rice_ton', 'Price_rice_ton_infl', 'Inflation_rate']]
    print("2nd raw data!")
    print(raw_data)
    print(raw_data.shape)

    # Dropping rows with NaN in them
    df_wheat_rw = df_wheat_rw.dropna()
    df_corn_rw = df_corn_rw.dropna()
    df_rice_rw = df_rice_rw.dropna()

    print("*************************dropna***************************")
    print(df_wheat_rw)

    # Dropping duplicate rows
    df_wheat_rw.drop_duplicates()
    df_corn_rw.drop_duplicates()
    df_rice_rw.drop_duplicates()

    # convert month name to int
    df_wheat_rw["Month"] = pd.to_datetime(df_wheat_rw['Month'], format='%b').dt.month
    df_corn_rw["Month"] = pd.to_datetime(df_corn_rw['Month'], format='%b').dt.month
    df_rice_rw["Month"] = pd.to_datetime(df_rice_rw['Month'], format='%b').dt.month

    print("************************convert month name to int***************************")
    print(df_wheat_rw)

    # check outliers
    check_outlier(df_wheat_rw, "Price_wheat_ton")

    low_limit, up_limit = outlier_thresholds(df_wheat_rw, "Price_wheat_ton")
    print(low_limit, up_limit)

    numeric_columns = [col for col in df_wheat_rw.columns if df_wheat_rw[col].dtypes != "O"]
    print(numeric_columns)

    for col in numeric_columns:
        replace_with_thresholds(df_wheat_rw, col)

    print("************************ outliers ***************************")
    print(df_wheat_rw)

    # Push cleaned data to S3 bucket warehouse
    DIR_wh = 's3://ece5984-bucket-jrnoll/Project'  # Insert here
    with s3.open('{}/{}'.format(DIR_wh, 'clean_wheat_prices.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_wheat_rw))
    with s3.open('{}/{}'.format(DIR_wh, 'clean_corn_prices.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_corn_rw))
    with s3.open('{}/{}'.format(DIR_wh, 'clean_rice_prices.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_rice_rw))


# for local testing
transform_data()
