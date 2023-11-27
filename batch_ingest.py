from kaggle.api.kaggle_api_extended import KaggleApi
from s3fs.core import S3FileSystem
import pickle
import pandas as pd
import numpy as np


def ingest_data():
    api = KaggleApi()
    api.authenticate()

    # Signature: dataset_list_files(dataset)
    # dataset string should be in format [owner]/[dataset-name]
    api.dataset_download_file('timmofeyy/-cerial-prices-changes-within-last-30-years', 'rice_wheat_corn_prices.csv')
    data = pd.read_csv("rice_wheat_corn_prices.csv", sep=",")

    print(data)

    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-bucket-jrnoll/Project'  # insert here
    # Push data to S3 bucket as a pickle file
    with s3.open('{}/{}'.format(DIR, 'data.pkl'), 'wb') as f:
        f.write(pickle.dumps(data))

# for local testing
# ingest_data()
