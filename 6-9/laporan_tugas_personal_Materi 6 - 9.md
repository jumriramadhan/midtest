# Laporan Tugas Personal 2 — Blockchain Level 6–9

- **Nama:** JUMRI RAMADHAN
- **NIM (4 digit terakhir):** 2157
- **Dibuat:** 2026-11-15 01:49  (waktu proses 0.2 detik)
- **Kode verifikasi:** `193462D2EB9A`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 6 — Mining data pribadi dan jejak difficulty

Data yang ditambang: `JUMRI RAMADHAN|2157|2004-11-20`

| Difficulty | Nonce | Percobaan | Teori 16^d | Hash |
|---|---|---|---|---|
| 1 | 2 | 3 | 16 | `0218d576eb883b9286da…` |
| 2 | 132 | 133 | 256 | `009effdb6c690e717e98…` |
| 3 | 3929 | 3.930 | 4.096 | `000d2b89b28b55835c8a…` |
| 4 | 110696 | 110.697 | 65.536 | `0000280e136ee9401a54…` |

- Difficulty awal (dari NIM): **2**, target waktu blok 10 detik
- Waktu blok simulasi (dari NIM + tanggal + bulan lahir): 8, 4, 20, 28, 8, 0, 4, 4 detik
- Jejak difficulty (Modifikasi 6): **2, 3, 3, 2, 2, 3, 4, 5**

## Level 7 — Kunci dan tanda tangan dari data pribadi

- Kunci publik (32 karakter awal): `8cc5ccc8383e06191aad45ac4f19ed50…`
- Alamat Anda: `d4667c33d666547727ecb893db8ebad97ea4dfd5`
- Transaksi: kirim **20** ke TEMAN_A
- Tanda tangan: `5dc1d971e1ce30a7d8daa60448311caa754a1c687cf5f3ef…`
- Tanda tangan selalu sama saat diulang: True
- Transaksi sah: **True**; setelah amount diubah: **False**
- Penipu memakai alamat Anda: tanda tangannya valid dengan kuncinya = True, transaksinya sah = **False**

## Level 8 — Jaringan dan fork pribadi

- Jumlah node: **3**; blok pribadi tiap node: [3, 2, 3]
- Panjang rantai saat fork: [5, 4, 5]
- Setelah resolve_conflicts: [5, 5, 5], sepakat = **False**
- Setelah blok pemecah seri: [6, 6, 6], sepakat = **True**
- Pemenang fork: **JUMRI-1**; blok terbuang (orphan): **5**
- Hash ujung rantai: `00afa0c7cf917bc31c20c174…`

## Level 9 — Ekonomi dengan halving

- Hadiah awal: **47**, halving setiap **2** blok
- Hadiah blok 1–6 (Modifikasi 9): **47, 47, 23, 23, 11, 11**

| Alamat | Saldo |
|---|---|
| JUMRI RAMADHAN | 116.0 |
| TEMAN_A | 32.0 |
| TEMAN_B | 14.0 |

- Total suplai: **162.0**
- Belanja melebihi saldo ditolak: True
- Validasi ekonomi: **True**; setelah hadiah blok 1 dicurangi: **False**

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 6.** Bandingkan kolom Percobaan dengan Teori 16^d pada tabel Anda. Mengapa bisa berbeda jauh? Lalu jelaskan jejak difficulty Anda (2, 3, 3, 2, 2, 3, 4, 5): pada langkah mana difficulty naik, tetap, dan turun, dan mengapa?

   _Jawaban:_
   - **Perbandingan Percobaan Empiris vs Teori $16^d$:**
     Kolom Teori $16^d$ menunjukkan nilai harapan rata-rata teoretis (*expected value*) dari proses penambangan yang memodelkan distribusi geometrik (proses Bernoulli). Dalam sistem heksadesimal, probabilitas setiap karakter bernilai '0' adalah $1/16$. Maka probabilitas menghasilkan $d$ angka nol berurutan di awal hash adalah $p = (1/16)^d$, sehingga rata-rata percobaan teoretisnya adalah $1/p = 16^d$.
     Namun, pencarian nonce pada satu kali proses penambangan bersifat acak murni tanpa memori (*memoryless stochastic process*). Pada sampel tunggal:
     - Pada difficulty 1, nonce ditemukan hanya dalam 3 percobaan (jauh lebih cepat dari teori 16).
     - Pada difficulty 2, butuh 133 percobaan (teori 256).
     - Pada difficulty 3, butuh 3.930 percobaan (sangat mendekati teori 4.096).
     - Pada difficulty 4, butuh 110.697 percobaan (jauh lebih tinggi dari teori 65.536).
     Variasi ini wajar dalam teori probabilitas, dan jika penambangan diulang ratusan kali lalu dirata-ratakan, rata-rata empiris akan konvergen tepat ke angka $16^d$.
   - **Analisis Jejak Difficulty `[2, 3, 3, 2, 2, 3, 4, 5]`:**
     Target waktu blok adalah 10 detik. Berdasarkan aturan `sesuaikan_difficulty`:
     - Jika waktu aktual $< 5$ detik ($\text{target}/2$) $\rightarrow$ penambangan terlalu cepat, difficulty **naik (+1)**.
     - Jika waktu aktual $> 20$ detik ($\text{target} \times 2$) $\rightarrow$ penambangan terlalu lambat, difficulty **turun (-1)**, minimal 1.
     - Jika $5 \le \text{waktu} \le 20$ detik $\rightarrow$ waktu penambangan ideal, difficulty **tetap**.
     Penjelasan langkah demi langkah:
     1. Langkah 1 (waktu 8s): $5 \le 8 \le 20 \rightarrow$ **Tetap di 2**.
     2. Langkah 2 (waktu 4s): $4 < 5 \rightarrow$ Blok ditemukan terlalu cepat, difficulty **Naik ke 3**.
     3. Langkah 3 (waktu 20s): Tepat di batas atas $\le 20 \rightarrow$ **Tetap di 3**.
     4. Langkah 4 (waktu 28s): $28 > 20 \rightarrow$ Penambangan terlalu lama/berat, difficulty **Turun ke 2**.
     5. Langkah 5 (waktu 8s): $5 \le 8 \le 20 \rightarrow$ **Tetap di 2**.
     6. Langkah 6 (waktu 0s): $0 < 5 \rightarrow$ Penambangan instan/super cepat, difficulty **Naik ke 3**.
     7. Langkah 7 (waktu 4s): $4 < 5 \rightarrow$ Blok terlalu cepat, difficulty **Naik ke 4**.
     8. Langkah 8 (waktu 4s): $4 < 5 \rightarrow$ Blok kembali terlalu cepat, difficulty **Naik ke 5**.
     Mekanisme penyesuaian dinamis ini menjaga agar interval penerbitan blok tetap stabil dan terprediksi meskipun kekuatan komputasi (*hashrate*) jaringan berubah-ubah.

2. **Level 7.** Mengapa tanda tangan Anda selalu sama setiap kali program dijalankan, padahal di Level 7 asli berubah-ubah? Mengapa transaksi penipu tidak sah walaupun tanda tangannya valid?

   _Jawaban:_
   - **Penyebab Tanda Tangan Selalu Sama:**
     Pada implementasi ECDSA standar di Level 7 asli, algoritma penandatanganan memilih bilangan acak rahasia (*random nonce* $k$) yang digenerate secara acak setiap kali fungsi dipanggil ($s = k^{-1}(z + r \cdot d_A) \pmod n$). Karena nilai $k$ selalu berbeda di setiap eksekusi, pasangan nilai $(r, s)$ tanda tangan selalu berubah.
     Sebaliknya, pada Modifikasi 7 digunakan metode penandatanganan deterministik berstandar **RFC 6979** (`sign_deterministic`). Standar ini menurunkan nilai $k$ secara deterministik menggunakan fungsi HMAC dari kunci privat dan hash pesan ($k = \text{HMAC}(d_A, H(m))$). Karena pesan transaksi kanonik dan kunci privat saya bersifat tetap, nilai $k$ yang dihasilkan selalu identik secara matematis, sehingga tanda tangan heksadesimal yang dihasilkan selalu sama persis di setiap run program. Ini juga melindungi sistem dari kebocoran kunci akibat generator bilangan acak yang bias atau cacat.
   - **Mengapa Transaksi Penipu Tidak Sah:**
     Fungsi verifikasi tanda tangan kriptografis (`verifikasi(tx, sig, pub_penipu)`) bernilai `True` karena penipu menandatangani pesan menggunakan kunci privat miliknya sendiri yang memang berpasangan secara matematis dengan `pub_penipu`.
     Namun, aturan konsensus blockchain mewajibkan pemeriksaan ganda melalui fungsi `transaksi_sah`: penandatangan wajib membuktikan kepemilikan atas dana yang dikirim dengan mencocokkan `tx['sender'] == alamat_dari_kunci_publik(pub)`. Karena alamat pengirim pada transaksi adalah alamat milik saya (`d4667c33...`), sedangkan kunci publik yang dilampirkan penipu menghasilkan alamat yang berbeda, sistem mendeteksi bahwa penipu mencoba mengotorisasi transaksi dari dompet orang lain tanpa izin. Oleh karena itu, transaksi dinyatakan **tidak sah (False)**.

3. **Keamanan kunci.** Kunci privat Anda dibuat dari nama, NIM, dan tanggal lahir. Mengapa cara ini SANGAT BERBAHAYA di dunia nyata? Siapa saja yang bisa mencuri dana alamat Anda? (Cari tahu istilah *brain wallet*.)

   _Jawaban:_
   - **Bahaya Fatal Metode Brain Wallet:**
     Metode pembuatan kunci privat dengan mengubah teks atau kata-kata yang mudah diingat manusia menjadi hash disebut sebagai **Brain Wallet**. Dalam ekosistem kriptografi dunia nyata, pendekatan ini terbukti sebagai salah satu kerentanan terburuk dengan risiko kehilangan dana 100%.
     1. *Entropi yang Sangat Rendah:* Kunci privat kurva eliptik SECP256k1 membutuhkan ruang keacakan sebesar 256 bit ($\approx 1.15 \times 10^{77}$ kemungkinan). Kombinasi `NIM:NAMA:TANGGAL_LAHIR` hanya memiliki variasi yang sangat sempit dan dapat ditebak (*low entropy*).
     2. *Bukan Rahasia Pribadi:* Data seperti Nama Lengkap, NIM, dan Tanggal Lahir berstatus data publik atau semi-publik yang tercatat di portal kampus (SIAKAD), pangkalan data Dikti, daftar presensi, dokumen beasiswa, KTP/KTM, dan media sosial.
     3. *Pihak yang Berpotensi Mencuri Dana:* Teman sekelas, civitas akademika, staf administrasi kampus, pihak ketiga yang memiliki akses basis data akademik, atau penyerang siber mana pun yang memperoleh kebocoran data (*data breach*) kampus.
     4. *Ancaman Bot Penjarah Otomatis (Brainwallet Sweeper Bots):* Di jaringan blockchain publik (seperti Bitcoin dan Ethereum), ribuan bot penjarah beroperasi 24/7 memindai mempool dan blok baru. Bot-bot ini telah mempra-komputasi tabel hash (*rainbow tables/dictionary attacks*) dari pola nama orang, format tanggal lahir, dan struktur identitas. Begitu ada koin yang dikirim ke alamat bertipe *brain wallet*, bot penjarah akan langsung menyapu bersih (*sweeping*) seluruh saldo dalam hitungan milidetik sebelum pemilik sempat memindahkannya.
   Kunci privat wajib selalu dibuat menggunakan generator bilangan acak berkekuatan kriptografis (*CSPRNG*) atau frasa pemulihan standar industri BIP-39 (12/24 kata acak).

4. **Level 8.** Jaringan Anda punya 3 node dan pemenangnya JUMRI-1 dengan 5 blok terbuang. Jelaskan mengapa node itu menang. Mengapa jaringan Anda sempat tidak sepakat, dan bagaimana blok pemecah seri menyelesaikannya?

   _Jawaban:_
   - **Mengapa Jaringan Sempat Tidak Sepakat (*Fork Tie*):**
     Saat terjadi percabangan jaringan (*fork*), Node JUMRI-1 menambang 3 blok lokal (panjang total 5 blok), Node JUMRI-2 menambang 2 blok (panjang 4 blok), dan Node JUMRI-3 menambang 3 blok (panjang 5 blok).
     Aturan konsensus Nakamoto menyatakan bahwa sebuah node hanya akan mereorganisasi rantainya jika ada rantai dari peer yang **valid dan lebih panjang secara ketat** (`len(peer.chain) > len(self.chain)`).
     Ketika fungsi `resolve_conflicts` dipanggil:
     - Node 2 (panjang 4) melihat Node 1 (panjang 5) dan mengadopsi rantai Node 1.
     - Namun, Node 1 dan Node 3 sama-sama memiliki panjang 5 blok dengan isi blok pribadi yang berbeda (`JUMRI-1#2157` vs `JUMRI-3#2157`). Karena panjangnya seri/identik (5 vs 5), tidak ada rantai yang *lebih panjang*, sehingga kedua node mempertahankan rantainya masing-masing.
     - Akibatnya, panjang seluruh node menjadi `[5, 5, 5]`, tetapi status kesepakatan jaringan bernilai `False` (`sepakat_setelah_resolve = False`). Jaringan berada dalam kondisi kebuntuan konsensus (*consensus deadlock / tie*).
   - **Peran Blok Pemecah Seri:**
     Kebuntuan seri terpecahkan ketika Node JUMRI-1 berhasil menambang 1 blok baru tambahan (blok pemecah seri), sehingga panjang rantai JUMRI-1 bertambah menjadi 6 blok.
     Saat siaran blok dilakukan, Node 2 dan Node 3 mendeteksi bahwa rantai milik JUMRI-1 kini memiliki panjang 6 (lebih panjang dari rantai mereka yang hanya 5 blok). Sesuai aturan konsensus, seluruh node secara serentak beralih mengadopsi rantai milik JUMRI-1 (`[6, 6, 6]`, `sepakat_setelah_pemecah_seri = True`).
   - **Mengapa JUMRI-1 Menang dan Blok Terbuang (*Orphan Blocks*):**
     JUMRI-1 keluar sebagai pemenang karena merupakan node yang pertama kali membangun rantai terpanjang yang didukung akumulasi Proof of Work terbesar.
     Blok-blok yang sebelumnya ditambang oleh Node 2 dan Node 3 pada cabang yang kalah ditinggalkan oleh jaringan dan menjadi blok yatim (*orphan/stale blocks*). Terdapat total **5 blok terbuang**. Inilah alasan fundamental mengapa sistem seperti Bitcoin menyarankan menunggu minimal 6 konfirmasi transaksi untuk memastikan transaksi tidak terhapus akibat reorganisasi rantai (*chain reorganization*).

5. **Level 9.** Dengan hadiah awal 47 dan halving setiap 2 blok, berapa batas total suplai jika mining berjalan selamanya? Tunjukkan perhitungannya, lalu kaitkan dengan batas 21 juta Bitcoin.

   _Jawaban:_
   - **Perhitungan Total Suplai Maksimal (Menggunakan Integer Division `//`):**
     Implementasi sistem `BlockchainHalving` menggunakan operator pembagian bilangan bulat Python (`//`), sehingga hadiah blok dipotong tanpa koma desimal:
     - Era 0 (Blok 1–2, $\text{index } 1..2$): Hadiah = $47$ per blok $\rightarrow 2 \times 47 = 94$ koin.
     - Era 1 (Blok 3–4, $\text{index } 3..4$): Hadiah = $47 // 2 = 23$ per blok $\rightarrow 2 \times 23 = 46$ koin.
     - Era 2 (Blok 5–6, $\text{index } 5..6$): Hadiah = $23 // 2 = 11$ per blok $\rightarrow 2 \times 11 = 22$ koin.
     - Era 3 (Blok 7–8, $\text{index } 7..8$): Hadiah = $11 // 2 = 5$ per blok $\rightarrow 2 \times 5 = 10$ koin.
     - Era 4 (Blok 9–10, $\text{index } 9..10$): Hadiah = $5 // 2 = 2$ per blok $\rightarrow 2 \times 2 = 4$ koin.
     - Era 5 (Blok 11–12, $\text{index } 11..12$): Hadiah = $2 // 2 = 1$ per blok $\rightarrow 2 \times 1 = 2$ koin.
     - Era 6 (Blok 13 ke atas, $\text{index } \ge 13$): Hadiah = $1 // 2 = 0$ per blok $\rightarrow$ Hadiah mining habis permanen.
     Maka batas total suplai absolut koin yang dapat beredar di blockchain ini adalah:
     $$\text{Total Suplai Maksimal} = 94 + 46 + 22 + 10 + 4 + 2 + 0 = \mathbf{178}\text{ koin}.$$
     *(Sebagai catatan perbandingan: jika dihitung dengan deret geometri murni tanpa pembagian bulat, $\sum = 2 \times 47 \times \frac{1}{1 - 1/2} = 188$; namun secara kode pemrograman yang dieksekusi, pemotongan integer menghasilkan tepat 178 koin).*
   - **Kaitan dengan Batas 21 Juta Bitcoin:**
     Mekanisme di atas adalah miniatur persis dari arsitektur kebijakan moneter Bitcoin:
     1. Bitcoin dirancang dengan hadiah awal 50 BTC per blok dan mengalami *halving* setiap 210.000 blok ($\approx 4$ tahun sekali).
     2. Total suplai Bitcoin mengikuti penjumlahan deret geometri konvergen:
        $$\text{Total Bitcoin} = 210.000 \times 50 \times \sum_{i=0}^{\infty} \left(\frac{1}{2}\right)^i = 210.000 \times 50 \times 2 = 21.000.000\text{ BTC}.$$
     3. Dalam kode sumber Bitcoin (C++), hadiah blok disimpan dalam satuan terkecil yaitu Satoshi ($1 \text{ BTC} = 10^8 \text{ Satoshi}$) dan dipotong menggunakan operasi pergeseran bit (*bit-shift right* `reward >>= 1`). Setelah 33 kali halving (sekitar tahun 2140), nilai hadiah bergeser menjadi 0 Satoshi. Mekanisme ini menciptakan kelangkaan absolut (*digital scarcity*) yang melindungi nilai mata uang dari hiperinflasi yang umum terjadi pada uang fiat.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "tugas": "personal-2 (Level 6-9)",
  "profil": {
    "nama": "JUMRI RAMADHAN",
    "nim4": "2157",
    "tanggal_lahir": "2004-11-20",
    "kota_asal": "SORONG",
    "hobi": "CODING"
  },
  "level6": {
    "data_ditambang": "JUMRI RAMADHAN|2157|2004-11-20",
    "mining": [
      {
        "difficulty": 1,
        "nonce": 2,
        "hash": "0218d576eb883b9286da46c67bd6fe55edb21e6e99d25af33c0d764c26216ed5",
        "percobaan": 3,
        "teori": 16
      },
      {
        "difficulty": 2,
        "nonce": 132,
        "hash": "009effdb6c690e717e98d6fc1ae6ad1ac08407f43d938dc8e8ad8c4c450a6b3a",
        "percobaan": 133,
        "teori": 256
      },
      {
        "difficulty": 3,
        "nonce": 3929,
        "hash": "000d2b89b28b55835c8aba62e331e6db5b3904455f6f78a42f1a0170d6c24b1c",
        "percobaan": 3930,
        "teori": 4096
      },
      {
        "difficulty": 4,
        "nonce": 110696,
        "hash": "0000280e136ee9401a54d8ebbbf46b1a52ada62ff08a886908f7762bdcba4484",
        "percobaan": 110697,
        "teori": 65536
      }
    ],
    "difficulty_awal": 2,
    "daftar_waktu_detik": [
      8,
      4,
      20,
      28,
      8,
      0,
      4,
      4
    ],
    "target_detik": 10,
    "jejak_difficulty": [
      2,
      3,
      3,
      2,
      2,
      3,
      4,
      5
    ]
  },
  "level7": {
    "kunci_publik_awal": "8cc5ccc8383e06191aad45ac4f19ed50",
    "alamat": "d4667c33d666547727ecb893db8ebad97ea4dfd5",
    "transaksi": {
      "sender": "d4667c33d666547727ecb893db8ebad97ea4dfd5",
      "recipient": "TEMAN_A",
      "amount": 20
    },
    "tanda_tangan": "5dc1d971e1ce30a7d8daa60448311caa754a1c687cf5f3ef5149482522669ac227610a24d6df236d79d7b60aab0f6036fd0167213d6ac29ba4773b2cfee6e842",
    "tanda_tangan_selalu_sama": true,
    "sah": true,
    "sah_setelah_amount_diubah": false,
    "ttd_penipu_valid_dengan_kuncinya": true,
    "transaksi_penipu_sah": false
  },
  "level8": {
    "jumlah_node": 3,
    "blok_pribadi_per_node": [
      3,
      2,
      3
    ],
    "panjang_saat_fork": [
      5,
      4,
      5
    ],
    "panjang_setelah_resolve": [
      5,
      5,
      5
    ],
    "sepakat_setelah_resolve": false,
    "perlu_pemecah_seri": true,
    "panjang_setelah_pemecah_seri": [
      6,
      6,
      6
    ],
    "sepakat_setelah_pemecah_seri": true,
    "pemenang_fork": "JUMRI-1",
    "blok_terbuang": 5,
    "hash_ujung": "00afa0c7cf917bc31c20c174a18910450f8ae81a90d2a89cccea1da461984c6b"
  },
  "level9": {
    "hadiah_awal": 47,
    "interval_halving": 2,
    "hadiah_per_blok": [
      47,
      47,
      23,
      23,
      11,
      11
    ],
    "saldo": {
      "JUMRI RAMADHAN": 116.0,
      "TEMAN_A": 32.0,
      "TEMAN_B": 14.0
    },
    "total_suplai": 162.0,
    "belanja_melebihi_saldo_ditolak": true,
    "validasi_ekonomi": true,
    "hash_ujung": "00700d464792fb689cff5db4f2f2489d7e64b3ac1a35c5f83dc5c6dc0799e47c",
    "validasi_setelah_hadiah_dicurangi": false
  },
  "kode_verifikasi": "193462D2EB9A"
}
```
