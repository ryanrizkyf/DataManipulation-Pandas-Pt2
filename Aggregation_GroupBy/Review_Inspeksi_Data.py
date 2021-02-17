# Mari review kembali terkait dengan inspeksi data yang pernah dilakukan pada modul sebelumnya.
# Akan menggunakan dataset
# https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv

import pandas as pd
# Load data global_air_quality.csv
global_air_quality = pd.read_csv(
    'global_air_quality_4000rows.csv')
print('Lima data teratas:\n', global_air_quality.head())
# Melakukan pengecekan terhadap data
print('Info global_air_quality:\n', global_air_quality.info())
# Melakukan count tanpa groupby
print('Count tanpa groupby:\n', global_air_quality.count())
# Melakukan count dengan groupby
gaq_groupby_count = global_air_quality.groupby('source_name').count()
print('Count dengan groupby (5 data teratas):\n', gaq_groupby_count.head())

# Terdapat perbedaan antara melakukan count dengan groupby dan tanpa groupby :
# 1. Terdapat index apa yang di specify as groupby
# 2. Perhitungan jadi berdasarkan apa yang di specify as groupby
# 3. Overall, lebih mudah untuk membaca data summary yang telah di groupby
