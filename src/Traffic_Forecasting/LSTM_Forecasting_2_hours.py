from google.colab import drive
drive.mount('/content/drive', force_remount=True)

"""# Read the data"""

import pandas as pd
dataset = pd.read_csv("Data/Traffic_Forecasting/Traffic_Forecasting_Data.csv")
dataset.columns

"""# Pick one column"""

sample = dataset['single_city_column_1']

from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-4:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix: end_ix+4]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

n_steps = 24*4
X_features, y_label = split_sequence(sample, n_steps)

import numpy as np
print(np.array(X_features).shape)
print(np.array(y_label).shape)

import keras
# Split into train and test (20% in test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_features, y_label, test_size=0.2, random_state=42)


# split into samples
#X, y = split_sequence(normalized_values, n_steps)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], n_features))
# define model
model = Sequential()
model.add(LSTM(50, activation='relu',  input_shape=(n_steps, n_features)))
#model.add(LSTM(50, activation='relu'))
model.add(Dense(4))
opt = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=opt, loss='mse')
# fit model
model.fit(X_train, y_train, epochs=300, verbose=2, validation_split = 0.15)

model.summary()

import numpy as np
predictions = model.predict(X_test)

import math
import numpy as np

predictions = np.array(predictions).squeeze()

# Difference between inversed and y_raw
# Difference between inversed and y_raw
from sklearn.metrics import mean_squared_error
print(y_test.shape)
print(predictions.shape)
MSE = mean_squared_error(y_test, predictions, squared=False)
print("MSE: ", MSE)

RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

import matplotlib.pyplot as plt
# Plot the true values and the ARIMA predictions
plt.figure(figsize=(12, 6))
plt.plot(y_test[30], label='Ground Truth', color='blue')
plt.plot(predictions[30], label='LSTM Forecast', color='red')
plt.xlabel('Time Steps (15 Minutes)')
plt.ylabel('Traffic Value')
plt.title('Time Series with LSTM Forecast')
plt.legend()
plt.grid(True)
plt.show()

MAE = np.mean(np.abs((y_test - predictions)))
print('MAE: ', MAE)

model.save('/content/drive/Models/lstm_model.h5')
