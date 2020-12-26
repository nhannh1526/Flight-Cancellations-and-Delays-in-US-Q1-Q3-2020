from datetime import timezone, datetime
import os
import pandas as pd
import wget
import tarfile

data_path = './Data'
raw_data_path = os.path.join(data_path, 'Raw data')
GSOD_path = os.path.join(raw_data_path, 'GSOD')
sep_30 = datetime(2020, 9, 30).replace(tzinfo=timezone.utc).timestamp()


def conveting_date_to_timestamp(year, month, day):
    dt = datetime(year, month, day)
    return dt.replace(tzinfo=timezone.utc).timestamp()


def converting_timestamp_to_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')


if not os.path.exists(os.path.join(data_path)):
    print(f'\nMaking {data_path} directory..')
    os.mkdir(data_path)

if not os.path.exists(os.path.join(raw_data_path)):
    print(f'\nMaking {raw_data_path} directory..')
    os.mkdir(raw_data_path)

if not os.path.exists(os.path.join(GSOD_path)):
    print(f'\nMaking {GSOD_path} directory..')
    os.mkdir(GSOD_path)

print('\nDownloading Global Surface Summary of the Day..')
url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/archive/2020.tar.gz'
wget.download(url, out=raw_data_path)

print('\nExtracting Global Surface Summary of the Day..')
tar_file_path = os.path.join(raw_data_path, '2020.tar.gz')
tar = tarfile.open(tar_file_path, 'r:gz')
tar.extractall(path=GSOD_path)
tar.close()

print('\nReading data..')
GSOD = pd.DataFrame()
for file_name in os.listdir(GSOD_path):
    print(f'\nReading {file_name}..')
    temp_df = pd.read_csv(os.path.join(GSOD_path, file_name),
                          encoding='utf-8', dtype={'FRSHTT': str})
    temp_df = temp_df[['STATION', 'DATE', 'LATITUDE',
                       'LONGITUDE', 'NAME', 'TEMP',
                       'DEWP', 'SLP', 'STP',
                       'VISIB', 'WDSP', 'PRCP',
                       'SNDP', 'FRSHTT']]
    temp_df['DATE'] = temp_df['DATE'].apply(
        lambda dt: conveting_date_to_timestamp(int(dt[:4]), int(dt[5:7]), int(dt[8:])))
    temp_df = temp_df.loc[temp_df['DATE'] <= sep_30, :]
    temp_df['DATE'] = temp_df['DATE'].apply(
        lambda ts: converting_timestamp_to_date(ts))
    GSOD = GSOD.append(temp_df, ignore_index=True)

print('\nSaving Global Surface Summary of the Day..')
GSOD.to_csv(os.path.join(raw_data_path, 'GSOD.csv'), index=False)
print('\nDone!')
