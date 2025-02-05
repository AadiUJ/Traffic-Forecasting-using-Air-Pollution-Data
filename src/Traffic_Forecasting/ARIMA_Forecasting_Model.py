from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the synthetic time series data from the CSV file
data = pd.read_csv('Data/Traffic_Forecasting/Traffic_Forecasting_Data.csv')

data['index_col'] = range(1, len(data) + 1)


# Extract the time steps and time series values
time_steps = data['index_col'].values
time_series = data['single_city_column_1'].values

# Plot the synthetic time series
plt.figure(figsize=(12, 6))
plt.plot(time_steps, time_series, label='Synthetic Time Series')
plt.xlabel('Time Steps (15 Minutes)')
plt.ylabel('Value')
plt.title('Time Series example with Trend, Seasonality, and Noise')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA



# Extract the time steps and time series values
time_steps = data['index_col'].values
time_series = data['single_city_column_1'].values

# Split the data into training and testing sets
train_size = int(0.8 * len(time_series))  # Use 80% of data for training
train_data, test_data = time_series[:train_size], time_series[train_size:]

# Plot the synthetic time series
plt.figure(figsize=(12, 6))
plt.plot(time_steps, time_series, label='Synthetic Time Series', color='blue')
plt.axvline(time_steps[train_size], linestyle='--', color='gray', label='Train/Test Split')
plt.xlabel('Time Steps (15 Minutes)')
plt.ylabel('Value')
plt.title('Time Series example with Trend, Seasonality, and Noise')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error



# Extract the time steps and time series values
time_steps = data['index_col'].values
time_series = data['single_city_column_1'].values
train_window = 24 # in hours
test_window = 2 # in hours
train_size = train_window*4
test_data_list = []
forecast_list = []

for window_start in range(0, len(data) - (train_window+test_window)*4, 10):
    print(window_start)
    print('train end', window_start + train_window*4)
    print('test end', window_start + (train_window+2)*4)


    train_data, test_data = time_series[window_start:window_start + train_window*4], time_series[window_start + train_window*4: window_start + (train_window+2)*4]

    """
    # Split the data into training and testing sets
    train_size = int(0.8 * len(time_series))  # Use 80% of data for training
    train_data, test_data = time_series[:train_size], time_series[train_size:]
    """

    # Fit ARIMA model to the training data (p,d,q)
    model = ARIMA(train_data, order=(10, 1, 10))
    results = model.fit()


    # Make predictions using ARIMA on the testing data
    num_predictions = len(test_data)
    forecast = results.forecast(steps=num_predictions)

    test_data_list.extend(test_data)
    forecast_list.extend(forecast)




# Plot the true values and the ARIMA predictions
plt.figure(figsize=(12, 6))
plt.plot(time_steps, time_series, label='Synthetic Time Series', color='blue')
plt.plot(time_steps[window_start + train_window*4: window_start + (train_window+2)*4], forecast, label='ARIMA Forecast', color='red')
plt.axvline(time_steps[train_size], linestyle='--', color='gray', label='Train/Test Split')
plt.xlabel('Time Steps (15 Minutes)')
plt.ylabel('Value')
plt.title('Time Series with ARIMA Forecast')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(test_data_list, forecast_list)
print("Mean Absolute Error (MAE):", mae)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(test_data_list, forecast_list))
print("Root Mean Squared Error (RMSE):", rmse)

# Plot the true values and the ARIMA predictions
plt.figure(figsize=(12, 6))
plt.plot(time_steps, time_series, label='Synthetic Time Series', color='blue')
plt.plot(time_steps[window_start + train_window*4: window_start + (train_window+2)*4], forecast, label='ARIMA Forecast', color='red')
plt.axvline(time_steps[train_size], linestyle='--', color='gray', label='Train/Test Split')
plt.xlabel('Time Steps (15 Minutes)')
plt.ylabel('Value')
plt.title('Time Series with ARIMA Forecast')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(test_data_list, forecast_list)
print("Mean Absolute Error (MAE):", mae)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(test_data_list, forecast_list))
print("Root Mean Squared Error (RMSE):", rmse)
