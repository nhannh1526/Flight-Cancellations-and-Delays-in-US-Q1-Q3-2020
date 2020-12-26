import os
import pandas as pd

path = './Data/Raw data'
AOTP_path = os.path.join(path, 'AOTP.csv')
GSOD_path = os.path.join(path, 'GSOD.csv')
airports_path = os.path.join(path, 'airports.csv')
carriers_path = os.path.join(path, 'carriers.csv')

processed_GSOD_path = os.path.join(path, 'processed_GSOD.csv')
processed_airports_path = os.path.join(path, 'processed_airports.csv')
processed_carriers_path = os.path.join(path, 'processed_carriers.csv')

print('\nReading data..')
AOTP = pd.read_csv(AOTP_path, encoding='utf-8')
GSOD = pd.read_csv(GSOD_path, encoding='utf-8', dtype={'FRSHTT': str})
airports = pd.read_csv(airports_path, encoding='utf-8')
carriers = pd.read_csv(carriers_path, encoding='utf-8')

print('\nDeleting unnecessary carriers..')
carriers = carriers[carriers['Code'].isin(
    pd.Series(AOTP['OP_UNIQUE_CARRIER'].unique()))]
print('\nSaving processed carriers..')
carriers.to_csv(processed_carriers_path, index=False)

print('\nDeleting unnecessary airports..')
airports = airports[airports['iata'].isin(pd.Series(AOTP['ORIGIN'].unique()))]
print('\nSaving processed airports..')
airports.to_csv(processed_airports_path, index=False)


def check_bool(row):
    if 'US' in row[-2:]:
        return True
    else:
        return False


def rounding_coordinates(lat, long, decimal_place=1):
    return (round(lat, decimal_place), round(long, decimal_place))


print('\nDeleting unnecessary GSOD..')
GSOD = GSOD[~GSOD['NAME'].isna()]
bool_list = list(map(check_bool, GSOD['NAME']))
GSOD = GSOD[bool_list]
GSOD['LAT_LONG'] = list(zip(GSOD['LATITUDE'], GSOD['LONGITUDE']))
GSOD['LAT_LONG'] = GSOD['LAT_LONG'].apply(
    lambda coor: rounding_coordinates(coor[0], coor[1]))
airports['LAT_LONG'] = list(zip(airports['lat'], airports['long']))
airports['LAT_LONG'] = airports['LAT_LONG'].apply(
    lambda coor: rounding_coordinates(coor[0], coor[1]))
left = GSOD[GSOD['LAT_LONG'].isin(airports['LAT_LONG'])]
right = airports
GSOD = pd.merge(left, right, on='LAT_LONG')
GSOD.drop(['LAT_LONG', 'airport', 'city', 'state',
           'country', 'lat', 'long'], axis=1, inplace=True)
GSOD.drop_duplicates(subset=['DATE', 'iata'], inplace=True)
print('\nSaving processed GSOD..')
GSOD.to_csv(processed_GSOD_path, index=False)

print('\nDone.')
