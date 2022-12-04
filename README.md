# Prediksi Kesuksesan Kelahiran Bayi Tabung
Project ini dibuat untuk melakukan prediksi apakah program bayi tabung akan berhasil berdasarkan variabel-variabel yang ada sesuai kriteria pasien.

## Deskripsi Project
In-Vitro Fertilisation (IVF) atau lebih sering dikenal bayi tabung adalah metode atau proses pembuahan sel telur oleh sel sperma di luar tubuh wanita. Bayi tabung merupakan salah satu solusi bagi orang yang memiliki berbagai masalah sehingga susah untuk mendapatkan keturunan baik dikarenakan penyakit genetik, masalah antibody, jumlah sel sperma rendah, kualitas sel telur kurang baik, endometriosis (infeksi Rahim), dll.
Meski demikian, bayi tabung tidak selalu berhasil meskipun telah mengeluarkan biaya yang sangat tinggi. Sehingga diperlukan suatu metode untuk melakukan prediksi tingkat kesuksesan kelahiran bayi tabung yang dapat dijadikan acuan apakah perlu mengambil program bayi tabung atau tidak sebelum mengeluarkan biaya yang cukup tinggi. Jadi, produk yang diharapkan adalah prediksi tingkat kesuksesan kelahiran bayi tabung berdasarkan kondisi pasien sehingga dapat meminimalkan biaya untuk mendapatkan keturunan.

![Alt text](/main/assets/ML%20workflow.jpg?raw=true "Optional Title")


## Cara Menggunakan

![Alt text](main/assets/interface.jpg?raw=true "Optional Title")

## Dataset
Fitur yang digunakan adalah sebagai berikut:

    patient_age_at_treatment : int
    total_number_of_previous_ivf_cycles : int
    total_number_of_ivf_pregnancies : int
    total_number_of_live_births_conceived_through_ivf : int
    type_of_infertility_female_primary : int
    type_of_infertility_female_secondary : int
    type_of_infertility_male_primary : int
    type_of_infertility_male_secondary : int
    type_of_infertility_couple_primary : int
    type_of_infertility_couple_secondary : int
    cause_of_infertility_tubal_disease : int
    cause_of_infertility_ovulatory_disorder : int
    cause_of_infertility_male_factor : int
    cause_of_infertility_patient_unexplained : int
    cause_of_infertility_endometriosis : int
    cause_of_infertility_cervical_factors : int
    cause_of_infertility_female_factors : int
    cause_of_infertility_partner_sperm_concentration : int
    cause_of_infertility_partner_sperm_morphology : int
    causes_of_infertility_partner_sperm_motility : int
    cause_of_infertility_partner_sperm_immunological_factors : int
    stimulation_used : int
    fresh_cycle : int
    frozen_cycle : int
    eggs_thawed : int
    fresh_eggs_collected : int
    eggs_mixed_with_partner_sperm : int
    embryos_transfered : int


## Kesimpulan
Dari metriks Machine Learning F1-Score yang dihasilkan hanya berkisar di 45%, hal ini perlu dilakukan analisa lebih mendalam terkait fitur-fitur yang penting, skala data, dan sebagainya untuk meningkatkan performa model. 

## Referensi

Machine learning predicts live‐birth
occurrence before in‐vitro
fertilization treatment.
Ashish Goyal, Maheshwar Kuchana & Kameswari Prasada Rao Ayyagari*
