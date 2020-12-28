import pickle
import numpy as np
import json
import pandas as pd
from datetime import datetime
with open('./models/Ridge.pkl', 'rb') as file:
    regressor = pickle.load(file)

with open('./models/Naive Bayes.pkl', 'rb') as file:
    classifier = pickle.load(file)

taxi_in_list = pd.read_csv('./etc/TAXI_IN.csv')
taxi_out_list = pd.read_csv('./etc/TAXI_OUT.csv')
mapping = json.load(open('./etc/mapping.json'))
range_values = json.load(open('./etc/range.json'))


def categorical_variable(name, display_name):
    while True:
        try:
            categorical = str(input('{}: '.format(display_name)))
            categorical_temp = categorical
            categorical = mapping[name][categorical]
            return categorical, categorical_temp
        except:
            pass


def taxi_variable(name, display_name):
    while True:
        try:
            TAXI = str(input('{}: '.format(display_name)))
            if TAXI == '' and name == 'TAXI_IN':
                TAXI = taxi_in_list[taxi_in_list['DEST'] == DEST_temp][name]
            elif TAXI == '' and name == 'TAXI_OUT':
                TAXI = taxi_out_list[taxi_out_list['ORIGIN']
                                     == ORIGIN_temp][name]
            TAXI = float(TAXI)
            if range_values[name]['min'] <= TAXI <= range_values[name]['max']:
                return TAXI
        except:
            pass


def continous_variable(name, display_name):
    while True:
        try:
            continous = float(input('{}: '.format(display_name)))
            if range_values[name]['min'] <= continous <= range_values[name]['max']:
                return continous
        except:
            pass


def binary_variable(display_name):
    while True:
        try:
            binary = int(input('{}: '.format(display_name)))
            if binary in [0, 1]:
                return binary
        except:
            pass


while True:
    try:
        MONTH = int(input('Month: '))
        DAY_OF_MONTH = int(input('Day of Month: '))
        date = datetime.strptime(
            '2020' + '-' + str(MONTH) + '-' + str(DAY_OF_MONTH), '%Y-%m-%d')
        DAY_OF_WEEK = datetime.weekday(date) + 1
        if range_values['MONTH']['min'] <= MONTH <= range_values['MONTH']['max']:
            if range_values['DAY_OF_MONTH']['min'] <= DAY_OF_MONTH <= range_values['DAY_OF_MONTH']['max']:
                break
    except:
        pass

OP_UNIQUE_CARRIER, _ = categorical_variable('carrier', 'Carrier')
ORIGIN, ORIGIN_temp = categorical_variable('org', 'ORIGIN')
ORIGIN_TEMP = continous_variable('ORIGIN_TEMP', 'Origin temp')
ORIGIN_DEWP = continous_variable('ORIGIN_DEWP', 'Origin dewp')
ORIGIN_VISIB = continous_variable('ORIGIN_VISIB', 'Origin visib')
ORIGIN_WDSP = continous_variable('ORIGIN_WDSP', 'Origin wdsp')
ORIGIN_PRCP = continous_variable('ORIGIN_PRCP', 'Origin prcp')
ORIGIN_FOG = binary_variable('Origin Fog')
ORIGIN_RAIN = binary_variable('Origin Rain')
ORIGIN_SNOW = binary_variable('Origin Snow: ')
ORIGIN_HAIL = binary_variable('Origin Hail: ')
ORIGIN_THUNDER = binary_variable('Origin Thunder')
ORIGIN_TORNADO = binary_variable('Origin Tornado')
DEST, DEST_temp = categorical_variable('dest', 'DEST')
DEST_TEMP = continous_variable('DEST_TEMP', 'Dest temp')
DEST_DEWP = continous_variable('DEST_DEWP', 'Dest dewp')
DEST_VISIB = continous_variable('DEST_VISIB', 'Dest visib')
DEST_WDSP = continous_variable('DEST_WDSP', 'Dest wdsp')
DEST_PRCP = continous_variable('DEST_PRCP', 'Dest prcp')
DEST_FOG = binary_variable('Dest Fog')
DEST_RAIN = binary_variable('Dest Rain')
DEST_SNOW = binary_variable('Dest Snow')
DEST_HAIL = binary_variable('Dest Hail')
DEST_THUNDER = binary_variable('Dest Thunder')
DEST_TORNADO = binary_variable('Dest Tornado')
TAXI_OUT = taxi_variable('TAXI_OUT', 'TAXI OUT')
TAXI_IN = taxi_variable('TAXI_IN', 'TAXI IN')
CRS_DEP_TIME = int(continous_variable('CRS_DEP_TIME', 'CRS Department Time'))
CRS_ARR_TIME = int(continous_variable('CRS_ARR_TIME', 'CRS Arrival Time'))
CRS_ELAPSED_TIME = continous_variable('CRS_ELAPSED_TIME', 'CRS Elapse Time')
DISTANCE = continous_variable('DISTANCE', 'Distance')
DIVERTED = float(binary_variable('Diverted'))
DAILY_CASES = continous_variable('DAILY_CASES', 'Daily cases')
BEGINNING_OF_OUTBREAK = float(binary_variable('Beginning of Outbreak'))

test = np.array([MONTH, DAY_OF_MONTH, DAY_OF_WEEK, OP_UNIQUE_CARRIER, ORIGIN,
                 DEST, CRS_DEP_TIME, TAXI_OUT, TAXI_IN, CRS_ARR_TIME,
                 DIVERTED, CRS_ELAPSED_TIME, DISTANCE, DAILY_CASES,
                 ORIGIN_TEMP, ORIGIN_DEWP, ORIGIN_VISIB, ORIGIN_WDSP,
                 ORIGIN_PRCP, DEST_TEMP, DEST_DEWP, DEST_VISIB, DEST_WDSP,
                 DEST_PRCP, ORIGIN_FOG, ORIGIN_RAIN, ORIGIN_SNOW, ORIGIN_HAIL,
                 ORIGIN_THUNDER, ORIGIN_TORNADO, DEST_FOG, DEST_RAIN,
                 DEST_SNOW, DEST_HAIL, DEST_THUNDER, DEST_TORNADO,
                 BEGINNING_OF_OUTBREAK]).reshape(1, -1)

print(f'This flight will be delayed for {regressor.predict(test)} minutes')

test = np.array([MONTH, DAY_OF_MONTH, DAY_OF_WEEK, OP_UNIQUE_CARRIER, ORIGIN, DEST,
                 CRS_DEP_TIME, TAXI_OUT, TAXI_IN, CRS_ARR_TIME, DIVERTED, CRS_ELAPSED_TIME, DISTANCE, DAILY_CASES,
                 ORIGIN_TEMP, ORIGIN_DEWP, ORIGIN_VISIB, ORIGIN_WDSP, ORIGIN_PRCP,
                 DEST_TEMP, DEST_DEWP, DEST_VISIB, DEST_WDSP, DEST_PRCP, regressor.predict(test)[
                     0],
                 ORIGIN_FOG, ORIGIN_RAIN, ORIGIN_SNOW, ORIGIN_HAIL, ORIGIN_THUNDER, ORIGIN_TORNADO,
                 DEST_FOG, DEST_RAIN, DEST_SNOW, DEST_HAIL, DEST_THUNDER, DEST_TORNADO, BEGINNING_OF_OUTBREAK]).reshape(1, -1)
pred = classifier.predict(test)
if pred == 1:
    print('This flight will be cancelled!')
else:
    print('This flight will not be cancelled!')
