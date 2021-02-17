# Akan melanjutkan untuk fungsi statistik .min() dan .max()
# untuk mengaggregasi dataset pollutant setelah di groupby.

import pandas as pd
# Load data https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv(
    'global_air_quality_4000rows.csv')
# Create variabel pollutant 
pollutant = gaq[['country', 'city', 'pollutant', 'value']].pivot_table(
    index=['country', 'city'], columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())

# Group berdasarkan country dan terapkan aggregasi min, method .min()
# setelah penerapan method .groupby() digunakan untuk memunculkan nilai terkecil dari tiap kelompok
# [5] Group berdasarkan country dan terapkan aggregasi min
pollutant_min = pollutant.groupby('country').min()
print('Nilai min pollutant (5 teratas:\n', pollutant_min.head())

# Group berdasarkan country dan terapkan aggregasi max, method .max()
# setelah penerapan method .groupby() digunakan untuk memunculkan nilai terbesar dari tiap kelompok
# [6] Group berdasarkan country dan terapkan aggregasi max
pollutant_max = pollutant.groupby('country').max()
print('Nilai max pollutant (5 teratas):\n', pollutant_max.head())

# Group berdasarkan country dan terapkan aggregasi first, method .first()
# setelah penerapan method .groupby() digunakan untuk memunculkan item pertama dari tiap kelompok
# [7] Group berdasarkan country dan terapkan aggregasi first
pollutant_first = pollutant.groupby('country').first()
print('Item pertama pollutant (5 teratas):\n', pollutant_first.head())

# Group berdasarkan country dan terapkan aggregasi last, method .last()
# setelah penerapan method .groupby() digunakan untuk memunculkan item terakhir dari tiap kelompok
# [8] Group berdasarkan country dan terapkan aggregasi last
pollutant_last = pollutant.groupby('country').last()
print('Item terakhir pollutant (5 teratas):\n', pollutant_last.head())
