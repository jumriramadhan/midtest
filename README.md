# Midtest Teknologi Blockchain — Implementasi Blockchain dari Nol

Repositori ini berisi seluruh penyelesaian tugas dan latihan mata kuliah **Teknologi Blockchain** (Semester 7) dari **Level 1 hingga Level 9**, mencakup implementasi teknis Python, pengujian otomatis, serta laporan analisis tugas personal.

**Identitas Mahasiswa:**
- **Nama:** JUMRI RAMADHAN
- **NIM:** 202355202157 (4 digit terakhir: `2157`)
- **Program Studi:** Teknik Informatika
- **Perguruan Tinggi:** Universitas Muhammadiyah Sorong

---

## Struktur Repositori

```
midtest/
├── 1-5/                                      # Materi Level 1 s.d. Level 5
│   ├── latihan/                              # Kode implementasi Level 1–5
│   │   ├── level01_hash.py                   # Fungsi Hash SHA-256 & Avalanche Effect
│   │   ├── level02_blok.py                   # Blockchain Dasar & Validasi Rantai
│   │   ├── level03_tampering.py              # Eksperimen Tampering & Deteksi Tautan Putus
│   │   ├── level04_transaksi.py              # Mempool Transaksi & Riwayat Akun
│   │   └── level05_pow_nonce.py              # Proof of Work Deterministik dengan Nonce
│   ├── tests/                                # Tes unit otomatis pytest
│   ├── tugas_personal/                       # Tugas Personal 1 (Modifikasi 1–5 Data Diri)
│   │   ├── data_saya.py                      # Data profil mahasiswa
│   │   ├── modifikasi.py                     # Implementasi Modifikasi 1–5
│   │   ├── jalankan_tugas.py                 # Runner skenario personal 1
│   │   └── laporan_tugas_personal_2157.md    # Laporan resmi hasil eksekusi data diri
│   ├── cek_nilai.py                          # Skrip penguji otomatis
│   ├── jawaban_refleksi.md                   # Jawaban pertanyaan refleksi materi 1–5
│   └── laporan_tugas_personal_Materi 1 -5.md # Laporan analisis lengkap materi 1–5
│
├── 6-9/                                      # Materi Level 6 s.d. Level 9
│   ├── latihan/                              # Kode implementasi Level 6–9
│   │   ├── level06_difficulty.py             # Tingkat Kesulitan & Difficulty Adjustment
│   │   ├── level07_tanda_tangan.py           # Kunci ECDSA SECP256k1 & Alamat Kriptografis
│   │   ├── level08_jaringan.py               # Node P2P & Konsensus Rantai Terpanjang (Fork)
│   │   ├── level08_server.py                 # Implementasi Web Server Flask Node
│   │   └── level09_reward_saldo.py           # Coinbase Reward, Saldo Akun & Halving
│   ├── tests/                                # Tes unit otomatis pytest
│   ├── tugas_personal_2/                     # Tugas Personal 2 (Modifikasi 6–9 Data Diri)
│   │   ├── data_saya.py                      # Data profil mahasiswa
│   │   ├── modifikasi_2.py                   # Implementasi Modifikasi 6–9
│   │   ├── jalankan_tugas_2.py               # Runner skenario personal 2
│   │   └── laporan_tugas_personal_2_2157.md  # Laporan resmi hasil eksekusi data diri
│   ├── cek_nilai.py                          # Skrip penguji otomatis
│   ├── jawaban_refleksi.md                   # Jawaban pertanyaan refleksi materi 6–9
│   └── laporan_tugas_personal_Materi 6 - 9.md# Laporan analisis lengkap materi 6–9
│
└── README.md                                 # Dokumentasi utama proyek
```

---

## Ringkasan Hasil Pengujian Otomatis

### 1. Materi Level 1 – 5 (`folder 1-5/`)
Status tes otomatis: **47/47 lulus (100% SELESAI)**
- **Level 1 (Fungsi Hash SHA-256):** 7/7 lulus
- **Level 2 (Blockchain Dasar):** 8/8 lulus
- **Level 3 (Eksperimen Tampering):** 9/9 lulus
- **Level 4 (Transaksi dalam Blok):** 13/13 lulus
- **Level 5 (PoW dengan Nonce):** 10/10 lulus
- **Kode Verifikasi Personal 1:** `CEE0EC63CF64`
- **ID Mahasiswa:** `715d9757`

### 2. Materi Level 6 – 9 (`folder 6-9/`)
Status tes otomatis: **90/90 lulus (100% SELESAI)**
- **Level 6 (Eksperimen Difficulty):** 13/13 lulus
- **Level 7 (Tanda Tangan Digital ECDSA):** 10/10 lulus
- **Level 8 (Jaringan & Konsensus):** 7/7 lulus
- **Level 9 (Reward & Saldo):** 13/13 lulus
- **Kode Verifikasi Personal 2:** `193462D2EB9A`
- **Alamat Kriptografis Mahasiswa:** `d4667c33d666547727ecb893db8ebad97ea4dfd5`

---

## Cara Menjalankan

### Persiapan Dependensi
```bash
pip install -r 1-5/requirements.txt
```

### Memeriksa Nilai Tes Unit
```bash
# Menjalankan tes materi 1-5:
cd 1-5
python cek_nilai.py

# Menjalankan tes materi 6-9:
cd ../6-9
python cek_nilai.py
```

### Menjalankan Tugas Personal
```bash
# Tugas Personal 1 (Level 1–5):
python 1-5/tugas_personal/jalankan_tugas.py

# Tugas Personal 2 (Level 6–9):
python 6-9/tugas_personal_2/jalankan_tugas_2.py
```
