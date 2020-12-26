import os
import pandas as pd
import tarfile

data_path = './Data'
raw_data_path = os.path.join(data_path, 'Raw data')
AOTP_path = os.path.join(raw_data_path, 'AOTP')

if not os.path.exists(os.path.join(data_path)):
    print(f'\nMaking {data_path} directory..')
    os.mkdir(data_path)

if not os.path.exists(os.path.join(raw_data_path)):
    print(f'\nMaking {raw_data_path} directory..')
    os.mkdir(raw_data_path)

if not os.path.exists(os.path.join(AOTP_path)):
    print(f'\nMaking {AOTP_path} directory..')
    os.mkdir(AOTP_path)

print('\nExtracting Airline On-Time Performance Data..')
tar_file_path = os.path.join(
    raw_data_path, 'Airline On-Time Performance Data.tar')
tar = tarfile.open(tar_file_path, 'r')
tar.extractall(path=AOTP_path)
tar.close()

print('\nReading data..')
AOTP = pd.DataFrame()
for file_name in os.listdir(AOTP_path):
    print(f'\nReading {file_name}..')
    temp_df = pd.read_csv(os.path.join(AOTP_path, file_name), encoding='utf-8')
    temp_df.drop('Unnamed: 30', axis=1, inplace=True)
    AOTP = AOTP.append(temp_df, ignore_index=True)

print('\nSaving Airline On-Time Performance Data..')
AOTP.to_csv(os.path.join(raw_data_path, 'AOTP.csv'), index=False)
print('\nDone!')
