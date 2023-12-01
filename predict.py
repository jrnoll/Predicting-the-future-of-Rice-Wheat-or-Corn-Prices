import botocore
import numpy as np
import pandas as pd
import s3fs
import tensorflow
from s3fs.core import S3FileSystem
import h5py
import boto3
import pickle


def predict():
    # Create a boto3 client.
    s3 = boto3.client('s3')

    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

    # The name of the S3 bucket
    bucket_name = 'ece5984-bucket-jrnoll'

    # Download the file
    try:
        s3.download_file(bucket_name, 'Project/wheat/lstm_wheat.h5', '/root/airflow/dags/lstm_wheat.h5')
        s3.download_file(bucket_name, 'Project/corn/lstm_corn.h5', '/root/airflow/dags/lstm_corn.h5')
        s3.download_file(bucket_name, 'Project/rice/lstm_rice.h5', '/root/airflow/dags/lstm_rice.h5')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print('Success! Found it!')

    # model = Sequential([Dense(units=64, activation='relu', input_shape=(1, 2)),])
    wheat_model = tensorflow.keras.models.load_model('lstm_wheat.h5')
    corn_model = tensorflow.keras.models.load_model('lstm_corn.h5')
    rice_model = tensorflow.keras.models.load_model('lstm_rice.h5')

    print(wheat_model.summary())
    print(corn_model.summary())
    print(rice_model.summary())

    predicted_data = []

    for y in range(2022, 2025):
        for m in range(1, 13):
            predictions_wheat = wheat_model.predict([[[y, m]]])
            predictions_corn = corn_model.predict([[[y, m]]])
            predictions_rice = rice_model.predict([[[y, m]]])

            predicted_values_wheat = predictions_wheat[0][0]
            predicted_values_corn = predictions_corn[0][0]
            predicted_values_rice = predictions_rice[0][0]

            predicted_data.append([y, m, predicted_values_wheat, predicted_values_corn, predicted_values_rice])

    predicted_prices = pd.DataFrame(predicted_data, columns=['Year', 'Month',
                                                             'Predicted_Wheat',
                                                             'Predicted_Corn',
                                                             "Predicted_Rice"])

    DIR = 's3://ece5984-bucket-jrnoll/Project/'
    with s3.open('{}/{}'.format(DIR, 'predicted_prices.pkl'), 'wb') as f:
        f.write(pickle.dumps(predicted_prices))
