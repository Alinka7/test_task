"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""
# TODO Import the necessary libraries
# TODO Import the dataset 

import pandas as pd
import numpy as np

# TODO Write a function in order to fix date (this relate only to the year info) and apply it
# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
path = r'./data/weather_dataset.data'

data =  pd.read_csv(path, sep='\s+')

data['Yr'] = data['Yr'] + 1900
data['date'] =  pd.to_datetime(dict(year=data.Yr, month=data.Mo, day=data.Dy))
del data['Yr']
del data['Mo']
del data['Dy']

data = data[['date', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6', 'loc7', 'loc8', 'loc9', 'loc10', 'loc11', 'loc12']]

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data.set_index('date', inplace = True)
data.index

# TODO Compute how many values are missing for each location over the entire record
missing_value = data.isnull().sum()
# TODO Compute how many non-missing values there are in total
non_missing_value = sum(data.notnull().sum())
data.notnull().sum()

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
data = data.apply(pd.to_numeric, errors='coerce')
data.loc[data.duplicated()]
# no duplicate values

# working with outliers
data.boxplot()
def outliers(data_frame, column):
    data = data_frame[column]
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    IQR = q3 - q1
    outliers_min = q1 - (1.5 * IQR)
    outliers_max = q3 + (1.5 * IQR)

    df_outliers = data[(data < outliers_min) | (data > outliers_max)]
    data_frame = data_frame[data_frame[column] >= outliers_min]
    data_frame = data_frame[data_frame[column] <= outliers_max]
    return data_frame

for i in list(data.columns):
    data = outliers(data, i)

data.boxplot()
for i in list(data.columns):
    data = outliers(data, i)

data.boxplot()

# working with NaNs
def replacing_nans(df):
    mean = df.mean()
    data_frame = df.fillna(mean)
    return data_frame


data['loc1'] = replacing_nans(data['loc1'])
data['loc2'] = replacing_nans(data['loc2'])
data['loc3'] = replacing_nans(data['loc3'])
data['loc4'] = replacing_nans(data['loc4'])
data['loc5'] = replacing_nans(data['loc5'])
data['loc6'] = replacing_nans(data['loc6'])
data['loc7'] = replacing_nans(data['loc7'])
data['loc8'] = replacing_nans(data['loc8'])
data['loc9'] = replacing_nans(data['loc9'])
data['loc10'] = replacing_nans(data['loc10'])
data['loc11'] = replacing_nans(data['loc11'])
data['loc12'] = replacing_nans(data['loc12'])
# checking the nans
data.isnull().sum()

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
data.mean().mean()

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
# the first way
loc_stats = pd.DataFrame()
loc_stats['min'] = data.min()
loc_stats['max'] = data.max()
loc_stats['mean'] = data.mean()
loc_stats['std'] = data.std()
loc_stats.transpose()

# the second way
loc_stats= data.describe()
loc_stats.loc[['std', 'min', 'max', 'mean']]

# TODO Find the average windspeed in January for each location
data['date'] = data.index
data['month'] = pd.DatetimeIndex(data['date']).month
average_windspeed_January = pd.DataFrame(data[data['month'] == 1].mean(), columns = ['average']).drop('month')
average_windspeed_January

# TODO Downsample the record to a yearly frequency for each location
data['year'] = pd.DatetimeIndex(data['date']).year
yearly_frequency = pd.DataFrame(data.resample('1y').mean()).drop(columns=['month', 'year'])
yearly_frequency

# TODO Downsample the record to a monthly frequency for each location
monthly_frequency = pd.DataFrame(data.resample('1m').mean()).drop(columns=['month', 'year'])
monthly_frequency

# TODO Downsample the record to a weekly frequency for each location
weekly_frequency = pd.DataFrame(data.resample('1w').mean()).drop(columns=['month', 'year'])
weekly_frequency

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week(assume that the first week starts on January 2 1961) for the first 21 weeks
weekly = data.resample('w').agg(['max','min','mean','std'])
first_21_week = weekly.loc[weekly.index[1:22]].drop(columns=['month', 'year'])
first_21_week

