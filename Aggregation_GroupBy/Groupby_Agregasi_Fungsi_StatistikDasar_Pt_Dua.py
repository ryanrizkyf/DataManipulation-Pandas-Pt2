# Akan melanjutkan untuk fungsi statistik lainnya yaitu .sum() dan .nunique()
# untuk mengaggregasi dataset pollutant setelah di groupby.

import pandas as pd
# Load data https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv(
    'global_air_quality_4000rows.csv')
# Create variabel pollutant 
pollutant = gaq[['country', 'city', 'pollutant', 'value']].pivot_table(
    index=['country', 'city'], columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())

# Group berdasarkan country dan terapkan aggregasi sum, method .sum()
# setelah penerapan method .groupby() digunakan untuk mencari total nilai dari tiap kelompok
# [3] Group berdasarkan country dan terapkan aggregasi sum
pollutant_sum = pollutant.groupby('country').sum()
print('Total pollutant (5 teratas):\n', pollutant_sum.head())

# Group berdasarkan country dan terapkan aggregasi nunique, method .nunique()
# setelah penerapan method .groupby() digunakan untuk mencari berapakah jumlah unique value dari tiap kelompok
# [4] Group berdasarkan country dan terapkan aggregasi nunique
pollutant_nunique = pollutant.groupby('country').nunique()
print('Jumlah unique value pollutant (5 teratas):\n', pollutant_nunique.head())
