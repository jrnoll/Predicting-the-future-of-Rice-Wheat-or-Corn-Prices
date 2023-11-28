import s3fs
from s3fs.core import S3FileSystem
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit


def feature_extract():
    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR_wh = 's3://ece5984-bucket-jrnoll/Project'  # Insert here
    # Get data from S3 bucket as a pickle file
    wheat_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_wheat_prices.pkl')), allow_pickle=True)
    corn_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_corn_prices.pkl')), allow_pickle=True)
    rice_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_rice_prices.pkl')), allow_pickle=True)

    # Load pickle data locally
    # wheat_df = np.load('clean_wheat_prices.pkl', allow_pickle=True)
    # corn_df = np.load('clean_corn_prices.pkl', allow_pickle=True)
    # rice_df = np.load('clean_rice_prices.pkl', allow_pickle=True)

    # Set Target Variable
    target_wheat = pd.DataFrame(wheat_df['Price_wheat_ton'])
    target_corn = pd.DataFrame(corn_df['Price_corn_ton'])
    target_rice = pd.DataFrame(rice_df['Price_rice_ton'])
    # Selecting the Features
    features_wheat = ['Year', 'Month', 'Price_wheat_ton_infl', 'Inflation_rate']

    # feature extraction on the wheat dataset
    # Scaling wheat dataframe
    scaler = MinMaxScaler()
    feature_transform_wheat = scaler.fit_transform(wheat_df[features_wheat])
    feature_transform_wheat = pd.DataFrame(columns=features_wheat, data=feature_transform_wheat, index=wheat_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_wheat):
        X_train, X_test = feature_transform_wheat[:len(train_index)], feature_transform_wheat[len(train_index): (
                len(train_index) + len(test_index))]
        y_train, y_test = target_wheat[:len(train_index)].values.ravel(), target_wheat[len(train_index): (
                len(train_index) + len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_wheat = 's3://ece5984-bucket-jrnoll/Project/wheat'  # Insert here
    with s3.open('{}/{}'.format(DIR_wheat, 'X_train_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_wheat, 'X_test_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_wheat, 'y_train_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_wheat, 'y_test_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

    # feature extraction on the corn dataset
    features_corn = ['Year', 'Month', 'Price_corn_ton_infl', 'Inflation_rate']
    # Scaling corn dataframe
    scaler = MinMaxScaler()
    feature_transform_corn = scaler.fit_transform(corn_df[features_corn])
    feature_transform_corn = pd.DataFrame(columns=features_corn, data=feature_transform_corn, index=corn_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_corn):
        X_train, X_test = feature_transform_corn[:len(train_index)], feature_transform_corn[len(train_index): (
                len(train_index) + len(test_index))]
        y_train, y_test = target_corn[:len(train_index)].values.ravel(), target_corn[len(train_index): (
                len(train_index) + len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_corn = 's3://ece5984-bucket-jrnoll/Project/corn'  # Insert here
    with s3.open('{}/{}'.format(DIR_corn, 'X_train_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_corn, 'X_test_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_corn, 'y_train_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_corn, 'y_test_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

    # feature extraction on the rice  dataset
    features_rice = ['Year', 'Month', 'Price_rice_ton_infl', 'Inflation_rate']
    # Scaling rice dataframe
    scaler = MinMaxScaler()
    feature_transform_rice = scaler.fit_transform(rice_df[features_rice])
    feature_transform_rice = pd.DataFrame(columns=features_rice, data=feature_transform_rice, index=rice_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_rice):
        X_train, X_test = feature_transform_rice[:len(train_index)], feature_transform_rice[len(train_index): (
                len(train_index) + len(test_index))]
        y_train, y_test = target_rice[:len(train_index)].values.ravel(), target_rice[len(train_index): (
                len(train_index) + len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_rice = 's3://ece5984-bucket-jrnoll/Project/rice'  # Insert here
    with s3.open('{}/{}'.format(DIR_rice, 'X_train_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_rice, 'X_test_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_rice, 'y_train_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_rice, 'y_test_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

# for local testing
# feature_extract()
