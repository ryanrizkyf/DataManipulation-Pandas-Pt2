# Jika dataset yang telah terlebih dahulu atau telah terlanjur di load dengan pd.read_csv dan
# Pandas salah mengenali object datetime menjadi object string, maka dapat mengubah kolom
# tertentu dari dataset tersebut menjadi format datetime.

import pandas as pd

# Load dataset https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv(
    'global_air_quality_4000rows.csv')
# Cetak 5 data teratas
print('Sebelum diubah dalam format datetime:\n', gaq.head())

# [2] pd.to_datetime digunakan untuk mentransform salah satu kolom di dataframe menjadi
# datetime Pandas dan kemudian set menjadi index. Mari perhatikan kembali contoh berikut
# Ubah menjadi datetime
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
# Cetak 5 data teratas
print('Sesudah diubah dalam format datetime:\n', gaq.head())

# Dataframe awal indexnya masih berupa urutan bilangan bulat dari nol.
# Kemudian dengan menerapkan pd.to_datetime dan set_index, dataframe sudah memiliki index berupa datetime.
