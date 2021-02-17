# Terkadang Pandas salah mengenali object datetime menjadi object string dan
# pandas menjadi tidak bisa memanfaatkan full benefit dari time index.

# Basic format datetime menurut ISO 8601: YYYY-mm-dd HH:MM:SS.

# Terdapat beberapa cara untuk mengubah kolom waktu menjadi format yang benar as datetime object di Pandas.

import pandas as pd
# Load dataset https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv

# [1] read_csv, terdapat keyword argument 'parse_dates',
# yang jika di set True dan set index untuk kolom waktu tersebut maka kolom datetime tersebut
# akan transform as datetime Pandas dan menjadi index

gaq = pd.read_csv('global_air_quality_4000rows.csv',
                  parse_dates=True, index_col='timestamp')
# Cetak 5 data teratas
print(gaq.head())
# Cetak info dari dataframe gaq
print('info')
print(gaq.info())
