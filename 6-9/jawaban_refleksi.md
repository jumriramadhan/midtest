# Jawaban Refleksi — Latihan Blockchain

**Nama:** JUMRI RAMADHAN  
**NIM:** 202355202157  
**Kelas:** TEKNOLOGI BLOCKCHAIN (A)  

> Salin output `python cek_nilai.py` Anda di bawah ini:

```
==============================================================
Level Materi                           Lulus      Status
--------------------------------------------------------------
1     Fungsi hash SHA-256                7/7     SELESAI
2     Blockchain dasar (GfG)             8/8     SELESAI
3     Eksperimen tampering               9/9     SELESAI
4     Transaksi dalam blok             13/13     SELESAI
5     PoW dengan nonce                 10/10     SELESAI
6     Eksperimen difficulty            13/13     SELESAI
7     Tanda tangan digital             10/10     SELESAI
8     Jaringan & konsensus               7/7     SELESAI
9     Reward & saldo                   13/13     SELESAI
--------------------------------------------------------------
TOTAL                                  90/90        100%
==============================================================
```

---

## Level 1 — Fungsi Hash
1. **Mengapa hash disebut "sidik jari digital"? Sebutkan tiga sifat fungsi hash kriptografis.**
   - Disebut sidik jari digital karena memetakan data dengan ukuran sembarang ke dalam nilai ringkasan berukuran tetap (256 bit pada SHA-256) yang unik. Sedikit saja input berubah, hash akan berubah drastis.
   - Tiga sifat utama:
     1. *Pre-image resistance* (Searah / One-way).
     2. *Second pre-image resistance* (Sulit mencari input lain dengan hash yang sama).
     3. *Collision resistance* (Sulit mencari dua input berbeda yang menghasilkan hash kembar).
2. **Berapa persen bit yang berubah ketika Anda mengganti satu huruf? Coba 3 pasangan teks berbeda.**
   - Hasil eksperimen:
     - `"Teknologi Blockchain"` vs `"teknologi Blockchain"`: 48.83% bit berubah.
     - `"Jumri Ramadhan"` vs `"jumri Ramadhan"`: 57.03% bit berubah.
     - `"Sorong 2026"` vs `"Sorong 2027"`: 51.56% bit berubah.
   - Perubahan bit berkisar di ~50%, membuktikan efek longsoran (*avalanche effect*).
3. **Apa yang terjadi jika `hash_dict` tidak memakai `sort_keys=True`? Mengapa itu berbahaya untuk blockchain?**
   - Tanpa `sort_keys=True`, urutan key pada string JSON bergantung pada memori Python. Dua node yang memiliki data transaksi sama bisa menghasilkan hash yang berbeda, memicu *fork* konsensus yang merusak jaringan.

## Level 2 — Blockchain Dasar
1. **Apa fungsi `previous_hash` pada blok genesis, dan mengapa nilainya `"0"`?**
   - `previous_hash` menghubungkan blok saat ini dengan blok sebelumnya. Karena blok genesis adalah blok pertama tanpa pendahulu, nilainya diisi konvensi `"0"` sebagai titik awal rantai (*root of trust*).
2. **Jalankan demo dengan difficulty 3, 4, dan 5. Catat nilai `proof` dan rasakan lamanya mining.**

| Difficulty | Proof blok #2 | Perkiraan waktu |
|---|---|---|
| 3 | 533 | < 0.01 detik |
| 4 | 533 | < 0.01 detik |
| 5 | 632238 | ~1.36 detik |

## Level 3 — Tampering
1. **Saat Anda mengubah data di blok posisi *k*, `cari_tautan_putus` melaporkan posisi *k+1*. Jelaskan mengapa.**
   - Karena blok $k+1$ menyimpan `previous_hash` yang merujuk pada hash asli dari blok $k$. Saat isi blok $k$ berubah, hash blok $k$ tidak cocok lagi dengan yang dicatat pada blok $k+1$.
2. **Mengapa perubahan pada blok terakhir tidak terdeteksi oleh `cari_tautan_putus`?**
   - Karena tidak ada blok $k+1$ sesudahnya yang menunjuk ke blok terakhir tersebut.
3. **Setelah `sambung_ulang`, rantai palsu dianggap valid. Apa kelemahan desain PoW di artikel GfG yang menyebabkannya?**
   - Rumus PoW artikel GfG (`proof**2 - previous_proof**2`) tidak melibatkan data transaksi blok, sehingga penyerang cukup menghitung ulang field `previous_hash` tanpa perlu menambang ulang proof.

## Level 4 — Transaksi
1. **Mengapa transaksi tidak langsung masuk ke blok, tetapi menunggu dulu di `pending_transactions`?**
   - Transaksi harus dikumpulkan di mempool terlebih dahulu sebelum dibundel oleh penambang ke dalam blok baru saat proses mining berhasil.
2. **Mengapa `create_block` harus memakai salinan `list(self.pending_transactions)`? Apa bug yang muncul jika tidak?**
   - Jika memakai referensi langsung tanpa disalin, saat `pending_transactions` dikosongkan (`[]`), daftar transaksi di blok yang sudah dibuat akan ikut terhapus.

## Level 5 — PoW dengan Nonce
1. **Bandingkan Level 3 dan Level 5: mengapa serangan "sambung ulang" gagal di sini?**
   - Di Level 5 seluruh isi blok (termasuk data transaksi dan nonce) di-hash bersama. Mengubah data mengubah hash blok, sehingga penyerang terpaksa menambang ulang seluruh blok sesudahnya.
2. **Jalankan demo. Berapa percobaan hash yang dibutuhkan penyerang untuk memalsukan blok #1 dari 3 blok? Perkirakan biayanya jika rantai berisi 1.000 blok dan difficulty 6.**
   - Diperlukan > 270.000 percobaan hash untuk 3 blok. Untuk 1.000 blok pada difficulty 6, dibutuhkan $\approx 1.000 \times 16^6 \approx 16,78 \text{ miliar}$ percobaan hash, mustahil dilakukan tanpa biaya energi komputasi masif.

## Level 6 — Difficulty
1. **Tampilkan tabel hasil eksperimen (difficulty 1–5). Apakah hasilnya mendekati 16^d? Mengapa 16?**
   - Sistem heksadesimal memiliki 16 kemungkinan nilai per digit (`0`-`f`). Probabilitas memperoleh angka '0' di depan adalah $(1/16)^d$, sehingga nilai harapan teoretis rata-rata percobaannya adalah $16^d$.
2. **Bitcoin menyesuaikan difficulty setiap 2.016 blok agar waktu blok sekitar 10 menit. Mengapa waktu blok perlu dijaga stabil?**
   - Menjaga interval blok stabil mencegah inflasi koin yang tak terkendali saat hashrate naik, memberi waktu propagasi blok ke seluruh dunia untuk mencegah *orphan blocks*, dan menjaga keamanan jaringan terdesentralisasi.

## Level 7 — Tanda Tangan Digital
1. **Apa perbedaan peran kunci privat, kunci publik, dan alamat?**
   - *Kunci privat:* Kunci rahasia untuk menandatangani transaksi (otorisasi belanja).
   - *Kunci publik:* Kunci terbuka untuk memverifikasi keabsahan tanda tangan.
   - *Alamat:* Hash dari kunci publik sebagai nomor rekening tujuan pengiriman dana.
2. **Pada tes `test_mencuri_atas_nama_orang_lain`, tanda tangan penipu valid tetapi transaksinya tidak sah. Jelaskan.**
   - Tanda tangan valid terhadap kunci milik penipu sendiri, tetapi transaksi tidak sah karena pengirim (`sender`) transaksi adalah alamat korban yang berbeda dari kunci penipu.
3. **Apa yang terjadi jika kunci privat Anda hilang? Bagaimana jika dicuri?**
   - *Jika hilang:* Dana terkunci selamanya di blockchain dan tidak bisa dipulihkan oleh siapa pun.
   - *Jika dicuri:* Pencuri memiliki kontrol mutlak untuk memindahkan seluruh saldo dompet.

## Level 8 — Jaringan & Konsensus
1. **Gambarkan kondisi fork pada demo, lalu kondisi setelah `resolve_conflicts`.**
   - Kondisi Fork:
     ```
     [Genesis] -> [Blok 1] -> [Blok 2 (Cabang B)]
                           -> [Blok 2 (Cabang C1)] -> [Blok 3 (Cabang C2)]
     ```
   - Kondisi Setelah `resolve_conflicts`:
     Seluruh node mengadopsi cabang C karena memiliki panjang rantai valid terbesar (panjang 4).
2. **Apa yang terjadi pada transaksi `fork-B` setelah konsensus? Kaitkan dengan anjuran "tunggu 6 konfirmasi" di Bitcoin.**
   - Blok cabang B menjadi *orphan block* dan transaksinya dibatalkan/dibuang dari rantai utama. Anjuran menunggu 6 konfirmasi memastikan blok transaksi telah tertanam cukup dalam sehingga probabilitas terhapus akibat *reorg* mendekati nol.
3. **Demo server Flask di port berbeda.**
   - Setiap node server menjalankan API REST (`/chain`, `/nodes/register`, `/nodes/resolve`) untuk sinkronisasi peer-to-peer.

## Level 9 — Reward & Saldo
1. **Dari mana koin pertama berasal jika semua orang memulai dengan saldo 0?**
   - Berasal dari transaksi *coinbase*, yaitu transaksi khusus yang dicetak oleh sistem (sender `"0"`) sebagai hadiah penambangan (*mining reward*).
2. **Mengapa `validasi_ekonomi` diperlukan walaupun `chain_valid` (validasi hash) sudah ada?**
   - `chain_valid` hanya memeriksa integritas kriptografis hash dan tautan, sedangkan `validasi_ekonomi` memeriksa kepatuhan aturan moneter (saldo tidak negatif, hadiah tidak digelembungkan, dan tidak ada pencetakan koin palsu).
3. **Perbedaan model akun dan model UTXO:**
   - Model akun (Ethereum/Level 9) mencatat saldo seperti rekening bank (saldo bertambah dan berkurang langsung pada alamat). Model UTXO (*Unspent Transaction Output*, Bitcoin) memperlakukan koin seperti uang kertas fisik di mana setiap transaksi menghabiskan output lama dan menghasilkan output baru yang belum terpakai.
