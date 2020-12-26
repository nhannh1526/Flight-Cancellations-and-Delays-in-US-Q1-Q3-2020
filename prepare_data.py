import os
import pandas as pd

path = './Data/Raw data'
AOTP_path = os.path.join(path, 'AOTP.csv')
pandemic_path = os.path.join(path, 'pandemic.csv')
processed_GSOD_path = os.path.join(path, 'processed_GSOD.csv')
processed_airports_path = os.path.join(path, 'processed_airports.csv')
processed_carriers_path = os.path.join(path, 'processed_carriers.csv')
data_path = os.path.join(path, '..', 'data.csv')

print('\nReading data..')
AOTP = pd.read_csv(AOTP_path, encoding='utf-8')
pandemic = pd.read_csv(pandemic_path, encoding='utf-8')
GSOD = pd.read_csv(processed_GSOD_path, encoding='utf-8',
                   dtype={'FRSHTT': str})
airports = pd.read_csv(processed_airports_path, encoding='utf-8')
carriers = pd.read_csv(processed_carriers_path, encoding='utf-8')

AOTP.sort_values('FL_DATE', inplace=True)

print('\nMerging pandemic data..')
AOTP = pd.merge(AOTP, pandemic, how='left', left_on='FL_DATE', right_on='Date')
AOTP.drop(['Date'], axis=1, inplace=True)
AOTP.rename(columns={'Daily Cases': 'DAILY_CASES'}, inplace=True)

print('\nMerging origin airports data..')
AOTP = pd.merge(AOTP, airports, how='left', left_on='ORIGIN', right_on='iata')
AOTP.drop(['iata', 'country'], axis=1, inplace=True)
columns = {
    'airport': 'ORIGIN_AIRPORT',
    'city': 'ORIGIN_CITY',
    'state': 'ORIGIN_STATE',
    'lat': 'ORIGIN_LAT',
    'long': 'ORIGIN_LONG'
}
AOTP.rename(columns=columns, inplace=True)

print('\nMerging origin airports weather conditions')
AOTP = pd.merge(AOTP, GSOD, how='left', left_on=[
                'ORIGIN', 'FL_DATE'], right_on=['iata', 'DATE'])
AOTP.drop(['DATE', 'LATITUDE', 'LONGITUDE', 'iata'], axis=1, inplace=True)
columns = {
    'STATION': 'ORIGIN_STATION',
    'NAME': 'ORIGIN_NAME',
    'TEMP': 'ORIGIN_TEMP',
    'DEWP': 'ORIGIN_DEWP',
    'SLP': 'ORIGIN_SLP',
    'STP': 'ORIGIN_STP',
    'VISIB': 'ORIGIN_VISIB',
    'WDSP': 'ORIGIN_WDSP',
    'PRCP': 'ORIGIN_PRCP',
    'SNDP': 'ORIGIN_SNDP',
    'FRSHTT': 'ORIGIN_FRSHTT'
}
AOTP.rename(columns=columns, inplace=True)

print('\nMerging destination airports data..')
AOTP = pd.merge(AOTP, airports, how='left', left_on='DEST', right_on='iata')
AOTP.drop(['iata', 'country'], axis=1, inplace=True)
columns = {
    'airport': 'DEST_AIRPORT',
    'city': 'DEST_CITY',
    'state': 'DEST_STATE',
    'lat': 'DEST_LAT',
    'long': 'DEST_LONG'
}
AOTP.rename(columns=columns, inplace=True)

print('\nMerging destination airports weather conditions')
AOTP = pd.merge(AOTP, GSOD, how='left', left_on=[
                'DEST', 'FL_DATE'], right_on=['iata', 'DATE'])
AOTP.drop(['DATE', 'LATITUDE', 'LONGITUDE', 'iata'], axis=1, inplace=True)
columns = {
    'STATION': 'DEST_STATION',
    'NAME': 'DEST_NAME',
    'TEMP': 'DEST_TEMP',
    'DEWP': 'DEST_DEWP',
    'SLP': 'DEST_SLP',
    'STP': 'DEST_STP',
    'VISIB': 'DEST_VISIB',
    'WDSP': 'DEST_WDSP',
    'PRCP': 'DEST_PRCP',
    'SNDP': 'DEST_SNDP',
    'FRSHTT': 'DEST_FRSHTT'
}
AOTP.rename(columns=columns, inplace=True)

print('\nRelacing carriers..')
carriers_dict = carriers.set_index('Code').T.to_dict('list')
AOTP['OP_UNIQUE_CARRIER'].replace(carriers_dict, inplace=True)

print('\nSaving data..')
AOTP.to_csv(data_path, index=False)
print('\nDone.')
