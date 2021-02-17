# Pada bagian ini akan mempelajari bagaimanakah caranya me-resampling data
# (baik upsampling atau downsampling) berdasarkan frekuensi, misalnya sekali 2 minggu, tiap 12 jam, dsb.

import pandas as pd
# Load dataset https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv(
    'global_air_quality_4000rows.csv')
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
print('Dataset sebelum di-resampling (5 teratas):\n', gaq.head())

# [1] Data ini downsampling dari daily to 2 weekly, kemudian dihitung rata-ratanya,
# jika ada nilai NaN maka dapat diisi dengan fillna method = 'ffill'
gaq_2weekly = gaq.resample('2W').mean().fillna(method='ffill')
print('Downsampling daily to 2 weekly - mean - ffill (5 teratas):\n', gaq_2weekly.head())

# [2] Selanjutnya, data awal di upsampling dari daily to 8 hourly, kemudian hitung rata-ratanya,
# jika ada nilai NaN maka dapat di isi dengan fillna method = 'bfill'
gaq_8hourly = gaq.resample('8H').mean().fillna(method='bfill')
print('Upsampling daily to 8 hourly - mean - bfill (5 teratas):\n', gaq_8hourly.head())

# Resample dari daily to 2 monthly, hitung reratanya, dan fillna = 'bfill'
gaq_2monthly = gaq.resample('2M').mean().fillna(method='bfill')
print('Resampling daily to 2 monthly - mean - ffill (5 teratas):\n',
      gaq_2monthly.head())
