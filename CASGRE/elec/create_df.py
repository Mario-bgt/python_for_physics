import pandas as pd
from gps_converter import *
df = pd.read_excel('Mappe1.xlsx')
df.Total_Power.astype(int)
i = 134106
for i in range(0, 134106):
    x = df.at[i, '_x']
    y = df.at[i, '_y']
    if type(x) != int:
        wgs84 = [47.3748, 8.1920, 500]
    else:
        converter = GPSConverter()
        lv03 = [df.at[i, '_x']-2000000, df.at[i, '_y']-1000000, 500]
        wgs84 = converter.LV03toWGS84(lv03[0], lv03[1], lv03[2])
    df.at[i, 'lat'] = wgs84[0]
    df.at[i,'lon'] = wgs84 [1]

df.to_pickle("a_file.pkl")