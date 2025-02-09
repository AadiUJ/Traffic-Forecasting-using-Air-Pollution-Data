
from google.colab import drive
drive.mount('/content/drive',force_remount=True)



# Read the dataset

import pandas as pd
dataset = pd.read_csv("Data/Air_Quality/Air_Quality_Sensor_Readings.csv")
dataset_v2 = pd.read_csv("Data/Air_Quality/Air_Quality_Sensor_Readings_v2.csv")
dataset = pd.concat([dataset, dataset_v2], axis=0)

dataset

dataset.head()

dataset_v1 = dataset.drop(["Timestamp","pm25", "sound"], axis=1)
#dataset_v1.iloc[0:16,:]



"""# Correlation analysis"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute pairwise correlation of columns
correlation_matrix = dataset_v1.corr()

# Plotting
plt.figure(figsize=(10,8))
sns.set_context("talk", font_scale=0.75)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Analysis')
plt.show()

"""Plot the readings with x-axis as datetime"""

# Convert the 'Timestamp' column to datetime format
dataset['Timestamp'] = pd.to_datetime(dataset['Timestamp'], unit='s')

dataset['Timestamp']

# Plotting
plt.figure(figsize=(14, 10))
for column in dataset.columns[1:]:
    plt.plot(dataset['Timestamp'], dataset[column], label=column)

plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Plot of Various Columns')
plt.tight_layout()
plt.grid(True)
plt.show()

"""# Day 24 of September"""

import pandas as pd
dataset = pd.read_csv("Data/Air_Quality/Shifted_Sensor_Data.xlsx")

dataset_v1 = dataset.drop(["Timestamp","pm25", "sound"], axis=1)

# Convert the 'Timestamp' column to datetime format
dataset['Timestamp'] = pd.to_datetime(dataset['Timestamp'], unit='s')

dataset['Timestamp']

dataset.head()

# Plotting
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 10))
for column in dataset.columns[1:]:
    plt.plot(dataset['Timestamp'].iloc[1:], dataset[column].iloc[1:], label=column)

plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Plot of Various Columns')
plt.tight_layout()
plt.grid(True)
plt.show()

"""# Shift the Methane reading by 1 unit and VOC by 2 units"""



import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute pairwise correlation of columns
correlation_matrix = dataset_v1.corr()

# Plotting
plt.figure(figsize=(10,8))
sns.set_context("talk", font_scale=0.75)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Analysis')
plt.show()

import pandas as pd
dataset_with_image_info = pd.read_csv('Data/Air_Quality/Sensor_Data_with_image_data.csv')

# Convert the 'Timestamp' column to datetime format
dataset_with_image_info['Timestamp'] = pd.to_datetime(dataset_with_image_info['Timestamp'], unit='s')
dataset_with_image_info.head()

# This is the original data to which the image path was added and hence we know the number of vehicles present at each row
dataset = pd.read_csv("Data/Air_Quality/Sensor_Data_v2.csv")

"""# Coorelation analysis when image analysis is added to it"""

dataset_image_v1 = dataset_with_image_info.drop(["Timestamp","pm25", "sound", "Image Path"], axis=1)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute pairwise correlation of columns
correlation_matrix = dataset_image_v1.corr()

# Plotting
plt.figure(figsize=(10,8))
sns.set_context("talk", font_scale=0.75)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Analysis')
plt.show()

# Convert the 'Timestamp' column to datetime format
dataset_with_image_info['Timestamp'] = pd.to_datetime(dataset_with_image_info['Timestamp'], unit='s')

# Plotting
plt.figure(figsize=(14, 10))
"""
for column in dataset_with_image_info.columns[1:]:
    plt.plot(dataset_with_image_info['Timestamp'], dataset_with_image_info[column], label=column)
"""
plt.plot(dataset_with_image_info['Timestamp'], dataset_with_image_info['CO'], label='CO')
plt.plot(dataset_with_image_info['Timestamp'], dataset_with_image_info['num_vehicles'], label='num_vehicles')

plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Plot of Various Columns')
plt.tight_layout()
plt.grid(True)
plt.show()

list_1 = list(dataset_with_image_info['VOC'])
list_2 = list(dataset_with_image_info['num_vehicles'])

len(list_2)

import numpy as np

def time_shifted_correlation(list1, list2, max_lag):
    """
    Calculate time-shifted correlation between two lists for all shifts up to max_lag.

    :param list1: First list of values.
    :param list2: Second list of values.
    :param max_lag: Maximum lag to consider.
    :return: Dictionary with lag as key and correlation as value.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")

    correlations = {}
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            shifted_list1 = list1[:lag]
            shifted_list2 = list2[-lag:]
        elif lag > 0:
            shifted_list1 = list1[lag:]
            shifted_list2 = list2[:-lag]
        else:
            shifted_list1 = list1
            shifted_list2 = list2

        correlation = np.corrcoef(shifted_list1, shifted_list2)[0, 1]
        correlations[lag] = correlation

    return correlations

correlation_dict = time_shifted_correlation(list_1, list_2, 30)

correlation_dict = time_shifted_correlation(list_1, list_2, 30)

max(correlation_dict.values())

import pandas as pd
dataset_with_image_info = pd.read_csv("Data/Air_Quality/Sensor_Data_with_imagedata_mean_vehicl_count.csv")
# Convert the 'Timestamp' column to datetime format
dataset_with_image_info['Timestamp'] = pd.to_datetime(dataset_with_image_info['Timestamp'], unit='s')
dataset_with_image_info.head()
dataset_image_v1 = dataset_with_image_info.drop(["Timestamp","pm25", "sound", "Image Path", "num_vehicles"], axis=1)

dataset_with_image_info.head()

# Compute pairwise correlation of columns
correlation_matrix = dataset_image_v1.corr()

# Plotting
plt.figure(figsize=(10,8))
sns.set_context("talk", font_scale=0.75)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Analysis')
plt.show()

list_1 = list(dataset_image_v1['VOC'])
list_2 = list(dataset_image_v1['CO'])

correlation_dict = time_shifted_correlation(list_1, list_2, 30)
max(correlation_dict.values())

correlation_dict.values()

# Plotting
plt.figure(figsize=(14, 10))

plt.plot(dataset_with_image_info['Timestamp'], dataset_with_image_info['CO'], label='CO')
plt.plot(dataset_with_image_info['Timestamp'], dataset_with_image_info['mean no. of vehicles']*10, label='mean no. of vehicles')

plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Plot of Various Columns')
plt.tight_layout()
plt.grid(True)
plt.show()
