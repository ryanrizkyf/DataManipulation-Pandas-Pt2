# Diberikan 4 csv files yang isinya retail data untuk tiap Quarter:

# csv (data dari bulan January - March)
# https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/retail_data_from_1_until_3.csv
# csv (data dari bulan April - June)
# https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/retail_data_from_4_until_6.csv
# csv (data dari bulan July - September)
# https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/retail_data_from_7_until_9.csv
# csv (data dari bulan October - December)
# https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/retail_data_from_10_until_12.csv

# Goal: Automation untuk pembuatan grafik dari measurement yang dibutuhkan.

# [1]. Load masing-masing data *.csv dengan Pandas
# [2]. Pengecekan dan Transformasi Data
# Cek data sekilas (melihat bentuk data biasanya 5 data teratas)
# Cek list kolom untuk semua dataframe apakah seluruh kolom dari keempat dataframe yang terpisah itu sama
# Jika sama digabungkan.
# Cek informasi dataframe yang telah digabungkan
# Statistik deskriptif dari dataframe yang telah digabungkan.
# [3] Transformasi Data
# Jika ada data yang tidak seharusnya maka dapat dibuang
# Jika ada kolom yang seharusnya bertipe datetime64 ubahlah
# Cek kembali informasi dataframe
# Tampilkan kembali statistik deskriptif dari dataframe
# [4]. Filter province yang hanya termasuk 5 provinsi besar di Jawa
# (DKI Jakarta, Jawa Barat, Jawa Tengah, Jawa Timur, dan Yogyakarta)
# [5]. Mengelompokkan data berdasarkan order_date dan province yang sudah difilter dan
# menghitung order unique count, customer unique count, product unique count, brand unique count,
# dan GMV (Gross Merchandise Volume = total_price untuk semua penjualan)
# [6]. Melakukan unstack untuk mendapatkan order_date di bagian baris dan province di bagian column
# [7]. Slicing data untuk masing-masing measurement (kolom), misal: kolom order
# [8]. Lakukan resampling pada data tersebut untuk dilakukan perhitungan secara bulanan
# [9]. Plot untuk hasil pada langkah #[8]


import pandas as pd
import matplotlib.pyplot as plt

# [1]. Load masing-masing data dengan pandas
retail_data1 = pd.read_csv(
    'retail_data_from_1_until_3.csv')
retail_data2 = pd.read_csv(
    'retail_data_from_4_until_6.csv')
retail_data3 = pd.read_csv(
    'retail_data_from_7_until_9.csv')
retail_data4 = pd.read_csv(
    'retail_data_from_10_until_12.csv')

# [2]. Pengecekan Data
print('PENGECEKAN DATA\n\n')
#      Cek data sekilas (tampilkan 5 baris teratas)
print(retail_data1.head())
#      Cek list kolom untuk semua dataframe
print('Kolom retail_data1: %s' % retail_data1.columns)
print('Kolom retail_data2: %s' % retail_data2.columns)
print('Kolom retail_data3: %s' % retail_data3.columns)
print('Kolom retail_data4: %s' % retail_data4.columns)
#      Concat multiple dataframe menjadi 1 dataframe
retail_table = pd.concat(
    [retail_data1, retail_data2, retail_data3, retail_data4])
print('\nJumlah baris:', retail_table.shape[0])
#      Pengecekan dataframe info
print('\nInfo:')
print(retail_table.info())
#      Pengecekan statistik deskriptif
print('\nStatistik deskriptif:\n', retail_table.describe())

# [3]. Transformasi Data
print('TRANSFORMASI DATA\n\n')
#      Memastikan data yang memiliki item_price < 0 atau total_price < 0
cek = retail_table.loc[(retail_table['item_price'] < 0)
                       | (retail_table['total_price'] < 0)]
print('\nitem_price < 0 atau total_price < 0:\n', cek)
#      Jika tidak masuk akal datanya dapat dibuang
if cek.shape[0] != 0:
    retail_table = retail_table.loc[(retail_table['item_price'] > 0) & (
        retail_table['total_price'] > 0)]
#      Cek apakah masih ada order_id yang bernilai undefined dan delete row tersebut
cek = retail_table.loc[retail_table['order_id'] == 'undefined']
print('\norder_id yang bernilai undefined:\n', cek)
#      Jika ada maka buang baris tersebut
if cek.shape[0] != 0:
    retail_table = retail_table.loc[retail_table['order_id'] != 'undefined']

#      Transform order_id menjadi int64
retail_table['order_id'] = retail_table['order_id'].astype('int64')
#      Transform order_date menjadi datetime Pandas
retail_table['order_date'] = pd.to_datetime(retail_table['order_date'])
#      Cek dataframe info kembali untuk memastikan
print('\nInfo:')
print(retail_table.info())
#      Cek statistik deskriptif kembali, untuk memastikan
print('\nStatistik deskriptif:\n', retail_table.describe())

# [4]. Filter hanya 5 province terbesar di pulau Jawa
print('\nFILTER 5 PROVINCE TERBESAR DI PULAU JAWA\n')
java = ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Yogyakarta']
retail_table = retail_table.loc[retail_table['province'].isin(java)]
#      Untuk memastikan kolom provinsi isinya sudah sama dengan java
print(retail_table['province'].unique())

# [5]. Kelompokkan sesuai dengan order_date dan province kemudian aggregasikan
groupby_city_province = retail_table.groupby(['order_date', 'province']).agg({
    'order_id': 'nunique',
    'customer_id': 'nunique',
    'product_id': 'nunique',
    'brand': 'nunique',
    'total_price': sum
})
#      Ubah nama kolomnya menjadi 'order','customer','product','brand','GMV'
groupby_city_province.columns = [
    'order', 'customer', 'product', 'brand', 'GMV']
print('\ngroupby_city_province (10 data teratas):\n',
      groupby_city_province.head(10))

# [6]. Unstack untuk mendapatkan order_date di bagian baris dan province di bagian column
unstack_city_province = groupby_city_province.unstack('province').fillna(0)
print('\nunstack_city_province (5 data teratas):\n', unstack_city_province.head())

# [7]. Slicing data untuk masing-masing measurement, misal: order
idx = pd.IndexSlice
by_order = unstack_city_province.loc[:, idx['order']]
print('\nby order (5 data teratas):\n', by_order.head())

# [8]. Lakukan resampling pada data tersebut untuk dilakukan perhitungan rata-rata bulanan
by_order_monthly_mean = by_order.resample('M').mean()
print('\nby_order_monthly_mean (5 data teratas):\n', by_order_monthly_mean.head())


# [9]. Plot untuk hasil pada langkah #[8]
by_order_monthly_mean.plot(
    figsize=(8, 5),
    title='Average Daily order Size in Month View for all Province'
)
plt.ylabel('avg order size')
plt.xlabel('month')
plt.show()

# Langah 7 s/d 9 yang telah dilakukan baru untuk satu measurement yaitu order.
# Berarti ada empat kali lagi kode seperti ini harus dibuat. Karena struktur code masih sama,
# apat menggunakan perulangan sesuai dengan jumlah measurement yaitu 5, sehingga kelima measurement
# dapat ditampilkan grafiknya dalam satu canvas figure.

# Mari memulai dengan membuat sebuah perulangan dengan dataframe unstack_city_province
# yang digunakan (hasil dari langkah ke 5 di part 2).

# Create figure canvas dan axes for 5 line plots
fig, axes = plt.subplots(5, 1, figsize=(8, 25))

# Slicing index
idx = pd.IndexSlice
for i, measurement in enumerate(groupby_city_province.columns):
    # Slicing data untuk masing-masing measurement
    by_measurement = unstack_city_province.loc[:, idx[measurement]]
    # Lakukan resampling pada data tersebut untuk dilakukan perhitungan rata-rata bulanan
    by_measurement_monthly_mean = by_measurement.resample('M').mean()
    # Plot by_measurement_monthly_mean
    by_measurement_monthly_mean.plot(
        title='Average Daily ' + measurement + ' Size in Month View for all Province',
        ax=axes[i]
    )
    axes[i].set_ylabel('avg ' + measurement + ' size')
    axes[i].set_xlabel('month')

# Adjust the layout and show the plot
plt.tight_layout()
plt.show()
