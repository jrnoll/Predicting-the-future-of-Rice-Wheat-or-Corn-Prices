import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from keras.layers import Dense
import tempfile


def build_train():
    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR_wheat = 's3://ece5984-bucket-jrnoll/Project/wheat'  # Insert here
    DIR_corn = 's3://ece5984-bucket-jrnoll/Project/corn'  # Insert here
    DIR_rice = 's3://ece5984-bucket-jrnoll/Project/rice'  # Insert here

    X_train_wheat = np.load(s3.open('{}/{}'.format(DIR_wheat, 'X_train_wheat.pkl')), allow_pickle=True)
    X_test_wheat = np.load(s3.open('{}/{}'.format(DIR_wheat, 'X_test_wheat.pkl')), allow_pickle=True)
    y_train_wheat = np.load(s3.open('{}/{}'.format(DIR_wheat, 'y_train_wheat.pkl')), allow_pickle=True)
    y_test_wheat = np.load(s3.open('{}/{}'.format(DIR_wheat, 'y_test_wheat.pkl')), allow_pickle=True)

    X_train_corn = np.load(s3.open('{}/{}'.format(DIR_corn, 'X_train_corn.pkl')), allow_pickle=True)
    X_test_corn = np.load(s3.open('{}/{}'.format(DIR_corn, 'X_test_corn.pkl')), allow_pickle=True)
    y_train_corn = np.load(s3.open('{}/{}'.format(DIR_corn, 'y_train_corn.pkl')), allow_pickle=True)
    y_test_corn = np.load(s3.open('{}/{}'.format(DIR_corn, 'y_test_corn.pkl')), allow_pickle=True)

    X_train_rice = np.load(s3.open('{}/{}'.format(DIR_rice, 'X_train_rice.pkl')), allow_pickle=True)
    X_test_rice = np.load(s3.open('{}/{}'.format(DIR_rice, 'X_test_rice.pkl')), allow_pickle=True)
    y_train_rice = np.load(s3.open('{}/{}'.format(DIR_rice, 'y_train_rice.pkl')), allow_pickle=True)
    y_test_rice = np.load(s3.open('{}/{}'.format(DIR_rice, 'y_test_rice.pkl')), allow_pickle=True)

    # wheat dataset model
    # Process the data for LSTM
    trainX_wheat = np.array(X_train_wheat)
    testX_wheat = np.array(X_test_wheat)
    X_train_wheat = trainX_wheat.reshape(X_train_wheat.shape[0], 1, X_train_wheat.shape[1])
    X_test_wheat = testX_wheat.reshape(X_test_wheat.shape[0], 1, X_test_wheat.shape[1])

    # Building the LSTM Model
    lstm_wheat = Sequential()
    lstm_wheat.add(LSTM(32, input_shape=(1, trainX_wheat.shape[1]), activation='relu', return_sequences=False))
    lstm_wheat.add(Dense(1))
    lstm_wheat.compile(loss='mean_squared_error', optimizer='adam')

    # Model Training
    history_wheat = lstm_wheat.fit(X_train_wheat, y_train_wheat, epochs=25, batch_size=8, verbose=1, shuffle=False,
                                 validation_data=(X_test_wheat, y_test_wheat))

    # Save model temporarily
    with tempfile.TemporaryDirectory() as tempdir:
        lstm_wheat.save(f"{tempdir}/lstm_wheat.h5")
        # Push saved model to S3
        s3.put(f"{tempdir}/lstm_wheat.h5", f"{DIR_wheat}/lstm_wheat.h5")

    # corn dataset model
    # Process the data for LSTM
    trainX_corn = np.array(X_train_corn)
    testX_corn = np.array(X_test_corn)
    X_train_corn = trainX_corn.reshape(X_train_corn.shape[0], 1, X_train_corn.shape[1])
    X_test_corn = testX_corn.reshape(X_test_corn.shape[0], 1, X_test_corn.shape[1])

    # Building the LSTM Model
    lstm_corn = Sequential()
    lstm_corn.add(LSTM(32, input_shape=(1, trainX_corn.shape[1]), activation='relu', return_sequences=False))
    lstm_corn.add(Dense(1))
    lstm_corn.compile(loss='mean_squared_error', optimizer='adam')

    # Model Training
    history_corn = lstm_corn.fit(X_train_corn, y_train_corn, epochs=25, batch_size=8, verbose=1, shuffle=False,
                                 validation_data=(X_test_corn, y_test_corn))

    # Save model temporarily
    with tempfile.TemporaryDirectory() as tempdir:
        lstm_corn.save(f"{tempdir}/lstm_corn.h5")
        # Push saved model to S3
        s3.put(f"{tempdir}/lstm_corn.h5", f"{DIR_corn}/lstm_corn.h5")

    # rice dataset model
    # Process the data for LSTM
    trainX_rice = np.array(X_train_rice)
    testX_rice = np.array(X_test_rice)
    X_train_rice = trainX_rice.reshape(X_train_rice.shape[0], 1, X_train_rice.shape[1])
    X_test_rice = testX_rice.reshape(X_test_rice.shape[0], 1, X_test_rice.shape[1])

    # Building the LSTM Model
    lstm_rice = Sequential()
    lstm_rice.add(LSTM(32, input_shape=(1, trainX_rice.shape[1]), activation='relu', return_sequences=False))
    lstm_rice.add(Dense(1))
    lstm_rice.compile(loss='mean_squared_error', optimizer='adam')

    # Model Training
    history_rice = lstm_rice.fit(X_train_rice, y_train_rice, epochs=25, batch_size=8, verbose=1, shuffle=False,
                                   validation_data=(X_test_rice, y_test_rice))

    # Save model temporarily
    with tempfile.TemporaryDirectory() as tempdir:
        lstm_rice.save(f"{tempdir}/lstm_rice.h5")
        # Push saved temporary model to S3
        s3.put(f"{tempdir}/lstm_rice.h5", f"{DIR_rice}/lstm_rice.h5")
