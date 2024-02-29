import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title = 'Capstone Project Tetris Batch 4 from DQLab by Maulana Yusuf Ikhsan Robbani-UMKM Jatim'
    ,layout='wide'
)

# Menulis teks

st.title("Mengenal lebih dekat UMKM Jawa Timur: Visualisasi Data UMKM di Jawa Timur :sparkles:")
st.header("Mengapa UMKM memiliki peran penting?")
st.markdown("""     Usaha Mikro Kecil dan Menengah (UMKM) menjadi salah satu pilar  pertumbuhan ekonomi di Indonesia. Terbukti bahwa UMKM berkontribusi menyumbang sebesar 61% terhadap Pendapatan Domestik Bruto (PDB) di Indonesia (Limanseto, 2022). Selain itu, UMKM mampu menyerap tenaga kerja sebanyak 119,6 juta orang pada tahun 2019 (Jayani, 2021). Pada tahun 2010 - 2013, tercatat bahwa pertumbuhan jumlah unit UMKM mengalami peningkatan sebesar 2,6 persen setiap tahunnya (Rahmadita, 2018). Berdasarkan hasil laporan yang dikaji oleh ASEAN, 65,46 juta unit UMKM berdiri di Indonesia pada tahun 2021 menjadikan Indonesia menjadi negara dengan UMKM terbanyak di ASEAN (ASEAN, 2022). Sementara, Dinas Koperasi dan Usaha Mikro Surabaya mencatat dari tahun 2020 sampai 2021 jumlah UMKM Surabaya tumbuh  dari 11.000 sampai  40.000  usaha (Fanani, 2021). Untuk UMKM digital, saat ini telah ada sekitar 20,5 juta berada di naungan Asosiasi E-commerce Indonesia (idEA), dimana pemerintah menargetkan sebanyak 30 juta UMKM digital pada tahun 2030 (Waseso, 2022).""")
st.markdown("""     Walaupun memiliki peran yang sangat penting terhadap pergerakan ekonomi di Indonesia, sebanyak 99% UMKM sulit berkembang salah satunya dikarenakan tidak sesuainya produk dengan kebutuhan pasar (Sarli, 2021). UMKM juga kekurangan informasi bisnis, pengetahuan akan pemasaran, sampai kurang bijak dalam pengelolaan cash flow dan produksi barang (Niode, 2009). Salah satu sektor UMKM yang menjadi perhatian banyak investor adalah UMKM  food and beverage (F&B).  BKPM  telah merilis data mengenai jumlah investasi asing di sektor UMKM terutama   makanan   dan   minuman   Indonesia  berdampak  cukup  besar.  Investasi  di industri  makanan dan  minuman  mencapai  31,4  triliun  rupiah  atau  14,1%  dari  total  semua  sektor  penanaman  modal hingga  kuartal II  tahun  2014. (Angkat, 2022). Harapannya dengan mengetahui kondisi terkini UMKM akan memudahkan beberapa stakeholder menerapkan kebijakan atau program yang dapat membantu UMKM""")
st.subheader(":green[Sehingga penting untuk menelisik lebih dalam kondisi UMKM di Jawa Timur] ")
st.subheader("Penjelasan mengenai dataset")
st.text("Data set yang akan dijadikan bahan analisis berasal dari website Satu Data Jawa Timur pada tab data UKM dengan filter Data Baru/Binaan")
st.text("Pengambilan data dilakukan dengan aplikasi ketiga yaitu Octoparse. Kemudian dilakukan data cleaning dengan memanfaatkan query untuk membuat tabel baru")
st.text("Berikut adalah sumber website ")
st.markdown(
    """
    [Satu Data Jawa Timur](https://data.diskopukm.jatimprov.go.id/satu_data/)
    """
)

st.header('Disclaimer 	:heavy_exclamation_mark:')
st.text('Data diambil berdasarkkan jawaban responden dari pelaku/karyawan UMKM yang memungkinkan diisi tidak sesuai realita')
tabel = pd.read_csv('../projectDQLab/data_umkm_ke4_openrevine_202402171115.csv')
numerik = ['ID_DT_BINAAN_EXCEL','TAHUN_MULAI_USAHA','UMUR',
           'JML_TENAGA_KERJA_2019','JML_TENAGA_KERJA_2020',
           'JML_TENAGA_KERJA_2021','OMSET_2019','OMSET_2020',
           'OMSET_2021','BIAYA_PRODUKSI_2019','BIAYA_PRODUKSI_2020',
           'BIAYA_PRODUKSI_2021','GAJI_KARYAWAN_2019',
           'GAJI_KARYAWAN_2020','GAJI_KARYAWAN_2021','score','row_num']
kategorikal = ['KAB_KOTA', 'KECAMATAN'  , 'JENIS_KEGIATAN'  , 'NAMA_PEMILIK' ,
               'NAMA_USAHA', 'JENIS_KELAMIN', 'PENDIDIKAN', 'STATUS_USAHA',
               'JENIS_LAPANGAN_USAHA',	'SERTIFIKasI', 'KLasIFIKasI_USAHA',
               'DAPAT_KREDIT', 'PERLU_PINJAMAN_PIHAK_LUAR']
#membuat kolom rata-rata terbaru (feature engineering)
#'UMUR', 'TAHUN_MULAI_USAHA','RATA2_JML_TENAGA_KERJA','RATA2_BIAYA_PRO0DUKSI','RATA2_GAJI'
tabel['RATA2_OMSET'] = tabel[['OMSET_2019', 'OMSET_2020', 'OMSET_2021']].mean(axis=1, skipna = True)
tabel['RATA2_JML_TENAGA_KERJA'] = tabel[['JML_TENAGA_KERJA_2019','JML_TENAGA_KERJA_2020','JML_TENAGA_KERJA_2021']].mean(axis=1, skipna = True)
tabel['RATA2_BIAYA_PRO0DUKSI'] = tabel[['BIAYA_PRODUKSI_2019','BIAYA_PRODUKSI_2020','BIAYA_PRODUKSI_2021']].mean(axis=1, skipna = True)
tabel['RATA2_GAJI'] = tabel[['GAJI_KARYAWAN_2019','GAJI_KARYAWAN_2020','GAJI_KARYAWAN_2021']].mean(axis=1, skipna = True)

st.header('Dashboard Usaha Mikro Kecil Menengah Jawa Timur')
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.metric(  
        label=':green[Omset Jawa Timur]',
        value= tabel['RATA2_OMSET'].sum()
    )
with col2:
    st.metric(  
        label=':green[Jumlah UMKM Jawa Timur]',
        value= tabel['ID_DT_BINAAN_EXCEL'].count()
    )
with col3:
    st.metric(  
        label=':violet[Yang Tidak Mendapat Kredit]',
        value= tabel['DAPAT_KREDIT'].value_counts()['TIDAK']
    )
with col4:
    st.metric(  
        label=':violet[Yang Membutuhkan Pinjaman]',
        value= tabel['PERLU_PINJAMAN_PIHAK_LUAR'].value_counts()['YA']
    )
# count_kredit = 
# count_pinjaman = 
st.header('Ringkasan Statistik tabel ber kolom numerikal')
st.dataframe(tabel[numerik].describe())
st.header('Ringkasan Statistik tabel ber kolom kategorikal')
st.dataframe(tabel[kategorikal].describe())

 
# Data Latar Belakang Pendidikan

# 
# Data Jenis Lapangan Usaha

# 
# Data Klasifikasi Usaha

# 
# Perlu diperhatikan bahwa kriteria UMKM adalah memiliki omset per tahun sebanyak 500 juta atau kurang. Sehingga dimungkinkan ada responden tidak relevan dikatakan UMKM.
tab1,tab2,tab3,tab4= st.tabs(['Kabupaten/Kota','Pendidikan','Jenis Lapangan Usaha','Klasifikasi Usaha'])
binary_value = [['TIDAK', 'YA']]

tabel_perlu_pinjaman_pihak_luar = tabel[tabel['PERLU_PINJAMAN_PIHAK_LUAR']=='YA']

with tab1: 
    col1,col2, col3 = st.columns([3,3,2])
    with col1:
        st.header('Kabupaten/Kota')
        st.markdown("""\n\n\n\n""")
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel['KAB_KOTA'],width = 0.2 )
        plt.grid(True)
        plt.xlabel('KAB_KOTA')
        plt.tight_layout()
        st.pyplot(plt)

    with col2:
        st.header('Perlu Pinjaman berdasarkan Kab/Kota ')
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel_perlu_pinjaman_pihak_luar['KAB_KOTA'],width = 0.2, color = 'orange' )
        plt.grid(True)
        plt.xlabel('KAB_KOTA')
        plt.tight_layout()
        st.pyplot(plt)
        
    with col3:
#        st.header('\n\n')
        st.header('Perlu Pinjaman Dalam Bentuk Tabel berdasarkan Kab/Kota ')
        st.dataframe(
        tabel_perlu_pinjaman_pihak_luar.groupby('KAB_KOTA').size().reset_index(name='Count')
        )
        st.markdown("""Terlihat bahwa kabupaten Malang menjadi kabupaten/kota dengan UMKM terdata terbanyak di Jawa Timur dengan jumlah 300 lebih. Sedangkan kabupaten Pacitan yang paling sedikit dibandingkan kabupaten/kota lain""")
with tab2: 
    col1,col2, col3 = st.columns([3,3,2])
    with col1:
        st.header('Pendidikan')
        st.markdown("""\n\n\n\n""")
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel['PENDIDIKAN'],width = 0.2 )
        plt.grid(True)
        plt.xlabel('PENDIDIKAN')
        plt.tight_layout()
        st.pyplot(plt)
        #st.text('Pelaku UMKM di Jawa Timur didominasi oleh lulusan S1/lebih sejumlah 1500 lebih. Sedangkan porsi pelaku yang tidak tamat SD adalah yang paling sedikit')
    with col2:
        st.header('Perlu Pinjaman berdasarkan Pendidikan')
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel_perlu_pinjaman_pihak_luar['PENDIDIKAN'],width = 0.2, color = 'orange' )
        plt.grid(True)
        plt.xlabel('PENDIDIKAN')
        plt.tight_layout()
        st.pyplot(plt)
    with col3:
#        st.header('\n\n')
        st.header('Perlu Pinjaman Dalam Bentuk Tabel berdasarkan Pendidikan')
        st.dataframe(
        tabel_perlu_pinjaman_pihak_luar.groupby('PENDIDIKAN').size().reset_index(name='Count')
        )
        st.markdown("""Pelaku UMKM di Jawa Timur didominasi oleh lulusan S1/lebih sejumlah 1500 lebih. Sedangkan porsi pelaku yang tidak tamat SD adalah yang paling sedikit""")
with tab3: 
    col1,col2, col3 =st.columns([3,3,2])
    with col1:
        st.header('Jenis Lapangan Usaha')
        st.markdown("""\n\n\n\n""")
        st.markdown("""\n\n\n\n""")
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel['JENIS_LAPANGAN_USAHA'],width = 0.2 )
        plt.grid(True)
        plt.xlabel('JENIS_LAPANGAN_USAHA')
        plt.tight_layout()
        st.pyplot(plt)
        st.text('')
    with col2:
        st.header('Perlu Pinjaman berdasarkan Jenis Lapangan Usaha ')
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel_perlu_pinjaman_pihak_luar['JENIS_LAPANGAN_USAHA'],width = 0.2, color = 'orange' )
        plt.grid(True)
        plt.xlabel('JENIS_LAPANGAN_USAHA')
        plt.tight_layout()
        st.pyplot(plt)
    with col3:
#        st.header('\n\n')
        st.header('Perlu Pinjaman Dalam Bentuk Tabel berdasarkan Jenis Lapangan Usaha ')
        st.dataframe(
        tabel_perlu_pinjaman_pihak_luar.groupby('JENIS_LAPANGAN_USAHA').size().reset_index(name='Count')
        )
        st.markdown("""Pelaku usaha kebanyakan terpusat pada industri pengolahan. Sedangkan pengangkutan dan pergudangan yang paling kecil jumlahnya""")

with tab4:
    col1,col2, col3 = st.columns([3,3,2])
    with col1: 
        st.header('Klasifikasi Usaha')
        st.markdown("""\n\n\n\n""")
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel['KLasIFIKasI_USAHA'],width = 0.2 )
        plt.grid(True)
        plt.xlabel('KLasIFIKasI_USAHA')
        plt.tight_layout()
        st.pyplot(plt)
        #st.text('')
    with col2:
        st.header('Perlu Pinjaman berdasarkan Klasifikasi Usaha ' )
        plt.figure(figsize=(12,16))
        sns.countplot(y=tabel_perlu_pinjaman_pihak_luar['KLasIFIKasI_USAHA'],width = 0.2, color = 'orange' )
        plt.grid(True)
        plt.xlabel('KLasIFIKasI_USAHA')
        plt.tight_layout()
        st.pyplot(plt)
    with col3:
        st.header('Perlu Pinjaman Dalam Bentuk Tabel berdasarkan Klasifikasi Usaha')
        st.dataframe(
        tabel_perlu_pinjaman_pihak_luar.groupby('KLasIFIKasI_USAHA').size().reset_index(name='Count')
        )
        st.markdown("""UMKM terbagi beragam macam kategori tergantung dari banyaknya omset yang dimiliki. UMKM dengan omset per tahun kurang dari 150 juta rupiah mendominasi. Sedangkan UMKM beromset menengah yaitu 25 M - 50 M yang paling sedikit. Sedikit sekali pengusaha yang memiliki omset lebih dari 2,5 M bahkan semakin besar omsetnya, semakin sedikit jumlahnya""")

#D:\Local Disk C\Python project\projectDQLab\data_umkm_ke4_openrevine_202402171115.csv

col1, col2 = st.columns(2)
with col1:
    kolom1 = st.selectbox(
    "Pilih Kolom yang ingin diketahui distribusinya",
    ('TAHUN_MULAI_USAHA','UMUR',
           'JML_TENAGA_KERJA_2019','JML_TENAGA_KERJA_2020',
           'JML_TENAGA_KERJA_2021','OMSET_2019','OMSET_2020',
           'OMSET_2021','BIAYA_PRODUKSI_2019','BIAYA_PRODUKSI_2020',
           'BIAYA_PRODUKSI_2021','GAJI_KARYAWAN_2019',
           'GAJI_KARYAWAN_2020','GAJI_KARYAWAN_2021')
    )
    st.title("Distribusi data per Kolom")
    # Visualisasi ke
    plt.figure(figsize=(12,12))
    features = numerik
    #plt.subplot(6, len(features)//6 + 1, i+1)
    sns.kdeplot(x=tabel[kolom1], color='skyblue')
    plt.title("Distribusi data "+kolom1)
    plt.xlabel(kolom1)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()


with col2:
    kolom2 = st.selectbox(
        "Pilih kolom mana yang ingin diketahui visualisasi box plot",
        ('TAHUN_MULAI_USAHA','UMUR',
           'JML_TENAGA_KERJA_2019','JML_TENAGA_KERJA_2020',
           'JML_TENAGA_KERJA_2021','OMSET_2019','OMSET_2020',
           'OMSET_2021','BIAYA_PRODUKSI_2019','BIAYA_PRODUKSI_2020',
           'BIAYA_PRODUKSI_2021','GAJI_KARYAWAN_2019',
           'GAJI_KARYAWAN_2020','GAJI_KARYAWAN_2021')
    )
    st.title("Boxplot per kolom")
    #Visualisasi ke
    plt.figure(figsize=(12,12))
    sns.boxplot(y=tabel[kolom2])
    plt.title('Boxplot '+kolom2 , fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
st.markdown('Terlihat bahwa banyak kolom yang memiliki data tail (data yang ekstrim). Contoh seperti jumlah tenaga kerja yang tembus sejumlah lebih dari 400 orang. Contoh lain adalah tahun mulai usaha yang lebih dari tahun 2019 Jika data yang ekstrim dihapus maka distribusi seluruh kolom mendekati distribusi normal')
st.markdown('Terlihat bahwa banyak outlier yang memiliki jarak yang cukup jauh dibandingkan mayoritas data yang terpusat untuk semua kolom')
col1, col2 = st.columns([2,3])

with col1:
    st.title('Porsi UMKM')
    kolom_biner = st.selectbox(
    'Pilih Kolom',
    ('DAPAT_KREDIT', 'PERLU_PINJAMAN_PIHAK_LUAR', 'JENIS_KELAMIN')
    )
    #plt.figure(figsize=(12,12))
    counts = tabel[kolom_biner].value_counts()
    # Create a pie chart of the counts
    labels = counts.index.astype(str).tolist()
    plt.pie(counts, labels=labels, autopct='%1.1f%%', textprops={'fontsize' : 40})
    st.pyplot(plt)
    plt.clf()
    st.markdown(
        """     Melihat data di atas, ternyata pelaku UMKM di Jawa Timur didominasi oleh jenis kelamin perempuan yang mana porsinya sebesar 58.9% atau lebih dari setengah pelaku UMKM
Setengah pelaku UMKM sebesar 57.1% nya ternyata membutuhkan pinjaman usaha """
    ) 
    st.markdown(
        """     Melihat data di kanan, terlihat kabupaten dengan jumlah responden umkm terbanyak adalah Kabupaten Malang. Terendah jatuh kepada Kabupaten Pacitan
Sedangkan untuk kecamatan dengan jumlah responden umkm terbanyak adalah """
    )  
with col2:

    st.title('Persebaran UMKM di suatu daerah :bar_chart:')
    kolom_daerah_1 = st.selectbox(
    'Kecamatan atau Kab/kota?',
    ('KECAMATAN','KAB_KOTA')
    )
    plt.figure(figsize=(50, 50))
    top_40_kecamatan = tabel[kolom_daerah_1].value_counts().index[:40]
    data_to_plot = tabel[tabel[kolom_daerah_1].isin(top_40_kecamatan)]
    sns.countplot(data=data_to_plot, y=data_to_plot[kolom_daerah_1])
    plt.title('Jumlah UMKM di suatu '+kolom_daerah_1, fontsize=40)
    plt.grid(True)
    plt.yticks(fontsize = 30)
    plt.xticks(fontsize = 30)   
    st.pyplot(plt)
    plt.clf()
     
st.header('Kebutuhan kredit/pinjaman berdasarkan gender :boy: :girl:')     
kolom_biner2 = st.selectbox(
    'Pilih Kolom',
    ('DAPAT_KREDIT', 'PERLU_PINJAMAN_PIHAK_LUAR')
)
plt.figure(figsize=(16,8))
sns.countplot(x=tabel['JENIS_KELAMIN'], hue=tabel[kolom_biner2])
plt.grid(True)
plt.xlabel('JENIS_KELAMIN')
plt.tight_layout()
st.pyplot(plt)
plt.clf()
st.markdown('Ternyata, jumlah pelaku UMKM yang perempuan dan tidak dapat kredit usaha sebanyak 1300 an usaha Bisa dikatakan, 2 dari 3 pelaku UMKM wanita tidak mendapatkan kredit usaha')

feature_scatter = ['UMUR', 'TAHUN_MULAI_USAHA','RATA2_JML_TENAGA_KERJA','RATA2_BIAYA_PRO0DUKSI','RATA2_GAJI']

st.header('Korelasi Rata-Rata Omset dengan data numerik lain')
tab1,tab2,tab3,tab4,tab5 = st.tabs(['Umur','Tahun Mulai Usaha','Rata-rata Jumlah Pekerja','Rata-rata biaya produksi','Rata-rata gaji'])
with tab1:
    plt.figure(figsize=(16,8))
    sns.regplot(data=tabel, x='RATA2_OMSET', y='UMUR')
    plt.ylabel('Umur')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
with tab2:
    plt.figure(figsize=(16,8))
    sns.regplot(data=tabel, x='RATA2_OMSET', y='TAHUN_MULAI_USAHA')
    plt.ylabel('Tahun Mulai usaha')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
with tab3:
    plt.figure(figsize=(16,8))
    sns.regplot(data=tabel, x='RATA2_OMSET', y='RATA2_JML_TENAGA_KERJA')
    plt.ylabel('Rata-rata Jumlah Pekerja')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
with tab4:
    plt.figure(figsize=(16,8))
    sns.regplot(data=tabel, x='RATA2_OMSET', y='RATA2_BIAYA_PRO0DUKSI')
    plt.ylabel('Rata-rata Biaya Produksi')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
with tab5:
    plt.figure(figsize=(16,8))
    sns.regplot(data=tabel, x='RATA2_OMSET', y='RATA2_GAJI')
    plt.ylabel('Rata-rata Gaji')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
st.markdown('Terlihat bahwa korelasi umur dan jumlah tenaga kerja tidak berkorelasi besar terhadap rata-rata omset suatu usaha. Namun, rata-rata biaya produksi dan rata-rata gaji karyawan cukup berkorelasi terhadap rata-rata omset dari suatu usaha. Artinya, semakin besar omset suatu usaha dimungkinkan semakin besar gaji karyawan dan biaya produksi dari suatu usaha tersebut. Dapat dikatakan untuk menilai usaha beromset besar atau tidak dapat melihat dari besar kecilnya gaji karyawan atau besar kecilnya biaya produksi tersebut. Malah, jumlah tenaga kerja dan umur pelaku usaha tidaklah berpengaruh besar terhadap omset suatu usaha')

st.header('Heatmap Korelasi Umur Sampai Rata-Rata Omset 	:fire:')
col1,col2 = st.columns(2)
with col1:
    feature_scatter2 = tabel[['UMUR', 'TAHUN_MULAI_USAHA','RATA2_JML_TENAGA_KERJA','RATA2_BIAYA_PRO0DUKSI','RATA2_GAJI', 'RATA2_OMSET']]
    plt.figure(figsize=(12,12))
    correlation = feature_scatter2.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f")
    st.pyplot(plt)
    plt.clf()
with col2:
    st.markdown('Terlihat bahwa :')
    st.markdown(
        "rata-rata gaji karyawan dengan rata-rata biaya produksi, rata-rata gaji karyawan dengan rata-rata omset,  rata-rata biaya produksi dengan rata-rata omset:"    )
    st.markdown("berkorelasi positif lebih dari 0.5 dan dikatakan sebagai korelasi sedang.  Artinya, semakin tinggi salah satu variabel tersebut maka semakin tinggi variabel lain. *Namun berbeda dengan variabel lain yang mana menunjukan nilai korelasi dibawah 0.5 atau bahkan minus.  Artinya, variabel seperti tahun mulai usaha, dan rata-rata jumlah tenaga kerja tidak benar-benar mempengaruhi variabel keseluruhan")
#Visualisasi ke
st.header('Korelasi 3 Kolom Kategorik dengan Omset')
col1,col2 = st.columns(2)
with col1:
    kolom_kategorik = st.selectbox(
    'Pilih kolom kategorik',
    ('PENDIDIKAN', 'DAPAT_KREDIT','PERLU_PINJAMAN_PIHAK_LUAR')
    )
    plt.figure(figsize=(16,16))
    sns.violinplot(data=tabel, x=kolom_kategorik, y='RATA2_OMSET', inner=None)
    plt.title('Violin Plot Korelasi '+kolom_kategorik+' dengan omset')
    plt.xticks(rotation =45)
    st.pyplot(plt)
    plt.clf()
with col2:
    st.markdown(
        """ Terlihat bahwa latar belakang pendidikan berpengaruh terhadap omset usaha. Semakin tinggi latar belakang pendidikan, semakin besar omset usaha nya. Namun, tidak menutup kemungkinan bahwa pendidikan yang tinggi menjamin omset usaha yang besar. Dapat dilihat frekuensi omset yang dibawah 0.5 lulusan S1/lebih kurang lebih sama dengan jenjang lain."""
    )
    st.markdown(
        """ Terlihat bahwa dapat tidaknya kredit suatu usaha tidak memengaruhi jumlah omset dan perlu tidaknya pinjaman luar juga tidak memengaruhi banyaknya omset yang dimiliki suatu usaha"""
    )

#Visualisasi ke
kolom_omset= st.select_slider(
    'Masukan Tahun',
    ('OMSET_2019','OMSET_2020','OMSET_2021')
)
st.header('Jumlah Omset per Tahun Tiap Daerah 	:bar_chart:')
#plt.figure(figsize=(24,24))
plt.figure(figsize=(24,24))
sns.barplot(data=tabel, y = 'KAB_KOTA',x = kolom_omset)
plt.title('Jumlah omset per tahun tiap daerah')
st.pyplot(plt)
plt.clf()

st.markdown('Tiap daerah cenderung mengalami penurunan omset dari tahun 2019 ke 2021. Kemungkinan besar diakibatkan pandemi pada tahun tersebut sehingga aktivitas perekonomian yang terbatas mengakibatkan penurunan omset. Pada tahun 2019 Lumajang menjadi daerah dengan omset rata-rata tertinggi di Jawa Timur sampai tahun 2020 dan pada akhirnya tahun 2021 beralih ke Pacitan. Jika dilihat seksama, Kota Probolinggo memiliki ketimpangan omset yang jauh besar terlihat selisih nilai maksimum dari omset pelaku UMKM disana dengan rata-rata omset tahunan disana sangat besar')
# Filter the DataFrame
tabel_melted = tabel.melt(id_vars='KAB_KOTA', value_vars=['OMSET_2019', 'OMSET_2020', 'OMSET_2021'], var_name='Year', value_name='OMSET')
#Ngambil nilai unik dr kab/kota di jatim apa aja, trus print ambil taruh multiselect
list_kabkota = tabel['KAB_KOTA'].unique()
kolom_kabkota = st.multiselect(
    'Pilih Kab/Kota',
    ('[19] MADIUN', '[05] BLITAR', '[77] KOTA MADIUN', '[13] PROBOLINGGO', '[02] PONOROGO' ,'[20] MAGETAN' ,'[22] BOJONEGORO' ,'[71] KOTA KEDIRI', '[14] PASURUAN', '[73] KOTA MALANG', '[17] JOMBANG', '[16] MOJOKERTO', '[11] BONDOWOSO', '[15] SIDOARJO', '[07] MALANG', '[18] NGANJUK', '[21] NGAWI', '[78] KOTA SURABAYA', '[06] KEDIRI', '[72] KOTA BLITAR', '[24] LAMONGAN', '[04] TULUNGAGUNG', '[10] BANYUWANGI', '[9] JEMBER', '[76] KOTA MOJOKERTO', '[79] KOTA BATU', '[23] TUBAN', '[75] KOTA PASURUAN', '[25] GRESIK', '[27] SAMPANG', '[29] SUMENEP', '[8] LUMAJANG', '[28] PAMEKASAN', '[03] TRENGGALEK', '[08] LUMAJANG', '[09] JEMBER','[12] SITUBONDO', '[26] BANGKALAN', '[01] PACITAN', '[74] KOTA PROBOLINGGO')
    ,default=('[07] MALANG','[14] PASURUAN','[73] KOTA MALANG') #Tertinggi ke-3
)
st.markdown('Omset per Tahun')
tabel_melted_filtered = tabel_melted[tabel_melted['KAB_KOTA'].isin(kolom_kabkota)]
plt.figure(figsize=(24,12))
sns.lineplot(data=tabel_melted_filtered, x='Year', y='OMSET', hue='KAB_KOTA')
plt.ylim(0, tabel_melted_filtered['OMSET'].max() * 0.5) #0.5 buat stretch smb y
plt.legend(prop={'size': 5})
plt.title('Omset setiap tahun')
st.pyplot(plt)
plt.clf()
st.markdown('Terlihat bahwa keseluruhan omset pelaku UMKM mengalami penurunan dari tahun 2019 ke 2021. Efek pandemi tidak dapat dipungkiri menjadi penyebab penurunan omset. 3 wilayah dengan omset tertinggi adalah kabupaten Pasuruan, kabupaten Malang, dan Kota Malang')

#Visualisasi ke 
st.header('Klasifikasi Usaha UMKM Jawa Timur')
plt.figure(figsize=(18,18))
ax = sns.countplot(x=tabel['KLasIFIKasI_USAHA'])
# Menambah angka diatas bar
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center',
                va = 'center',
                xytext = (0, 10),
                textcoords = 'offset points')
plt.xticks(rotation=60)
plt.grid(True)
st.pyplot(plt)
plt.clf()

#Machine Learning Section
# split data untuk training model dan test
from sklearn.model_selection import train_test_split

#feature = tabel.drop(columns='purchased')
numerik_train = ['RATA2_JML_TENAGA_KERJA', 'RATA2_BIAYA_PRO0DUKSI','RATA2_GAJI']
feature = tabel[numerik_train]
target = tabel[['RATA2_OMSET']]

feature_purchase_train, feature_purchase_test, target_purchase_train, target_purchase_test = train_test_split(feature, target, test_size=0.20, random_state=42)

from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


numerik_train = ['RATA2_JML_TENAGA_KERJA', 'RATA2_BIAYA_PRO0DUKSI','RATA2_GAJI']
feature = tabel[numerik_train]
target = tabel[['RATA2_OMSET']]

# Membuat imputer agar nilai kosong terisi di suatu feature
imputer_feature = SimpleImputer(strategy='mean')  # or median, most_frequent, constant
feature_imputed = imputer_feature.fit_transform(feature)

# Sama seperti diatas namun untuk data test
imputer_target = SimpleImputer(strategy='mean')  # or median, most_frequent, constant
target_imputed = imputer_target.fit_transform(target)


# Split data
feature_train, feature_test, target_train, target_test = train_test_split(feature_imputed, target_imputed, test_size=0.20, random_state=42)

# Pemanggilan model
model = HistGradientBoostingRegressor()

# Train model
model.fit(feature_train, target_train.ravel())

# Model yang sudah siap memprediksi
predictions = model.predict(feature_test)

# Mengukur akurasi model dengan mae, nilai mutlak
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(target_test, predictions)
print("Mean Absolute Error (MAE):", mae)

# mengukur akurasi model dengan R2 score (coeficient of determination)
from sklearn.metrics import r2_score
r2 = r2_score(target_test, predictions)
print("R² Score:", r2)

# Mendefinisikan data poin
# Misalkan rata2 jumlah tenaga kerja sejumlah 7 orang, rata2 biaya produksi sebesar Rp. 5 jt, rata2 gaji karyawan sebesar 15 jt maka berapa rata2 omset usahanya
st.header('Prediksi Omset menggunakan input jumlah tenaga kerja, biaya produksi, dan gaji karyawan ')
st.text('Predikasi menggunakan model Hist Gradient Booster dengan data test jumlah tenaga kerja, biaya produksi, dan gaji karyawan untuk prediksi Omset')
a=st.number_input(
    'Masukan Jumlah tenaga kerja suatu usaha (0 sampai 50)',
    min_value=0,
    max_value=50,
    step=1,
    value=7
)
b=st.number_input(
    'Masukan rata-rata biaya produksi suatu usaha ',
    min_value=0,
    max_value=10000000000,
    value=5000000
)
c=st.number_input(
    'Masukan rata-rata gaji karyawan',
    min_value=0,
    max_value=1000000000,
    value=15000000
)
new_data = [[a, b, c]]

# Use the imputer to handle any potential missing values
new_data_imputed = imputer_feature.transform(new_data)

# Use the model to predict 'RATA2_OMSET' for the new data point
new_prediction = model.predict(new_data_imputed)

st.write("Prediksi nilai rata-rata omset adalah:", new_prediction[0])

#Machine Learning Section 2
st.header('Clustering UMKM berdasarkan Rata-rata Omset dan Klasifikasi Usaha')
tabel_encoded = tabel
#Mengisi nilai kosong di 2 kolom ini
tabel_encoded['RATA2_OMSET'].fillna(tabel_encoded['RATA2_OMSET'].median(), inplace=True)
tabel_encoded['KLasIFIKasI_USAHA'].fillna(tabel_encoded['KLasIFIKasI_USAHA'].mode()[0], inplace=True)

# One-hot encoding
one_hot = pd.get_dummies(tabel_encoded['KLasIFIKasI_USAHA'])
# Join the encoded df
tabel_encoded = tabel_encoded.join(one_hot)

from sklearn.preprocessing import LabelEncoder

# Create a label encoder object, mengubah data kategorik jadi numerik
le = LabelEncoder()

# Fit and transform the 'KLASIFIKASI_USAHA' column
tabel_encoded['KLasIFIKasI_USAHA'] = le.fit_transform(tabel_encoded['KLasIFIKasI_USAHA'])

from sklearn.preprocessing import StandardScaler

# Define the features
features = ['RATA2_OMSET', 'KLasIFIKasI_USAHA']

# Scale the features
scaler = StandardScaler()
tabel_scaled = scaler.fit_transform(tabel_encoded[features])

from sklearn.cluster import KMeans

# Create a KMeans object
kmeans = KMeans(n_clusters=7, random_state=0)

# Fit the model to the data and predict the cluster assignments
tabel_encoded['Cluster'] = kmeans.fit_predict(tabel_scaled)

# Print the size of the clusters
st.write(tabel_encoded['Cluster'].value_counts())

# Print the mean 'RATA2_OMSET' and 'KLASIFIKASI_USAHA' for each cluster
st.write(tabel_encoded.groupby('Cluster')[features].mean())

st.header('Kesimpulan')
st.markdown(
    """* Kebutuhan Pinjaman Luar yang masih tinggi terlepas pendidikan, jenis usaha, klasifikasi usaha(Berdasarkan jumlah Omset) memilikii porsi lebih dari 50%. Sehingga, perlunya akses yang banyak terhadap pinjaman untuk UMKM  """
)
st.markdown(
    """* Kredit masih terbatas dengan terbuktinya 70% UMKM tidak dapat kredit. Artinya, UMKM perlu disediakan media, dibimbing, atau difasilitasi agar usaha mereka layak mendapatkan kredit atau pinjaman untuk mendukung usaha  """
)
st.markdown(
    """* Rata-rata omset dengan rata-rata biaya produksi & rata-rata gaji berkorelasi sedang daripada kolom lain sehingga pengamat UMKM dapat mempertimbangkan omset dengan 2 hal tersebut"""
)
st.markdown(
    """* Melihat pendidikan berkorelasi dengan besarnya omset, sehingga dapat mempertimbangkan pendidikan lebih tinggi untuk para pelaku UMKM"""
)
st.markdown(
    """* Penurunan omset dari 2019-2021 menandakan perlunya UMKM agar mengembalikan kondisi awal omsetnya sebelum pandemi"""
)
st.markdown(
    """* UMKM dengan omset kurang dari 150 juta pertahun mendominasi. Artinya, stakeholder perlu lebih fokus dalam bagaimana pelaku UMKM tersebut bisa berubah menjadi UMKM dengan omset tinggi dan berlaba tinggi"""
)