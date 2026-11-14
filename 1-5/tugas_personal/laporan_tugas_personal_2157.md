# Laporan Tugas Personal Blockchain Level 1–5

- **Nama:** JUMRI RAMADHAN
- **NIM (4 digit terakhir):** 2157
- **Dibuat:** 2026-11-15 01:31  (waktu proses 2.6 detik)
- **Kode verifikasi:** `CEE0EC63CF64`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 1 — Hash data pribadi

| Hasil | Nilai |
|---|---|
| SHA-256 nama | `c2ddc3ac51b43909930a72af29ce6e4686fa68ebb15cf8743827727a979323bc` |
| hash_dict profil | `2d3216eb85b91254c8ec7c6ffdda5d6f0728674ecb3b42a006018e1f298e8a7c` |
| hash_dict profil (urutan key dibalik) | `2d3216eb85b91254c8ec7c6ffdda5d6f0728674ecb3b42a006018e1f298e8a7c` |
| Bit berubah: tanggal lahir vs tanggal lahir + 1 hari | 53.91% |
| ID mahasiswa (Modifikasi 1) | `715d9757` |

## Level 2 — Blockchain personal

- Proof genesis: **2157** (dari NIM)
- Proof blok 2, 3, 4: **49896, 828, 17404**
- Pemilik setiap blok: `715d9757`
- Rantai valid: True

## Level 3 — Pemalsuan data pribadi

- Posisi yang dipalsukan: **2**
- Data asli: `JUMRI RAMADHAN berasal dari SORONG`
- Data palsu: `JUMRI RAMADHAN berasal dari SORONG (DIPALSUKAN)`
- Valid sebelum dipalsukan: True
- Tautan putus di indeks: **3**
- Valid setelah dipalsukan: **False**
- Valid setelah disambung ulang: **True**

## Level 4 — Transaksi dari data pribadi

| Blok | Pengirim | Penerima | Jumlah |
|---|---|---|---|
| 2 | JUMRI RAMADHAN | TEMAN_A | 20 |
| 2 | TEMAN_A | JUMRI RAMADHAN | 11 |
| 3 | JUMRI RAMADHAN | DOSEN | 8 |

- Ringkasan saldo (Modifikasi 4): masuk **11**, keluar **28**, bersih **-17**
- Kirim ke diri sendiri ditolak: True
- Amount 0 ditolak: True

## Level 5 — Proof of Work dengan nonce (deterministik)

| Blok | Nonce | Hash |
|---|---|---|
| 0 | 10056 | `0000a727c5bedd9178ae8e5f…` |
| 1 | 2267 | `00004bfa77978843e6962188…` |
| 2 | 52451 | `000045d3020eba8500efe775…` |
| 3 | 102944 | `00009fc31ac3c37c320e4c0d…` |

- Valid: True → setelah blok 1 dipalsukan: **False**
- Percobaan hash untuk menambang ulang blok 1–3: **67.100**
- Valid setelah ditambang ulang: True

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 1.** Bandingkan SHA-256 nama Anda dengan milik seorang teman. Apakah ada pola yang mirip? Jelaskan juga mengapa dua hash profil Anda sama, dan mengapa hanya menambah 1 hari pada tanggal lahir mengubah 53.91% bit.

   _Jawaban:_
   - **Pola Kemiripan SHA-256:** Tidak ada pola kemiripan sama sekali antara SHA-256 nama saya (`c2ddc3ac51b43909930a72af29ce6e4686fa68ebb15cf8743827727a979323bc`) dengan milik teman. Meskipun input memiliki kemiripan struktur huruf atau panjang karakter yang setara, keluaran fungsi hash SHA-256 tampak sepenuhnya acak (*pseudorandom*) dan terdistribusi seragam di seluruh ruang 256-bit. Hal ini membuktikan sifat *pre-image resistance* dan ketiadaan korelasi linear antara teks input dan digest heksadesimal.
   - **Alasan Dua Hash Profil Sama:** Hash profil asli dan profil dengan urutan key dibalik bernilai identik (`2d3216eb85b91254c8ec7c6ffdda5d6f0728674ecb3b42a006018e1f298e8a7c`) karena implementasi fungsi `hash_dict` menerapkan serialisasi kanonik melalui parameter `json.dumps(..., sort_keys=True)`. Sebelum diubah menjadi bytes dan di-hash, kamus (*dictionary*) selalu diurutkan menurut kunci secara alfabetis. Dalam arsitektur blockchain terdistribusi, serialisasi kanonik ini bersifat mutlak agar node-node dengan implementasi internal bahasa atau memori yang berbeda tetap menghasilkan hash blok yang seragam.
   - **Avalanche Effect 53.91%:** Mengubah tanggal lahir dari `2004-11-20` menjadi `2004-11-21` hanya mengubah tepat 1 karakter ASCII pada posisi terakhir ('0' bernilai biner `00110000` menjadi '1' bernilai biner `00110001`, yaitu selisih 1 bit saja). Namun, SHA-256 menggunakan struktur putaran kompresi Davies-Meyer dengan 64 ronde yang melibatkan operasi rotasi bit, pergeseran (*shift*), fungsi non-linear boolean, dan penjumlahan modular $2^{32}$. Akibatnya, satu bit perubahan di awal menyebar dan mengacaukan seluruh blok data (*avalanche effect* / efek longsoran), menghasilkan perubahan sebesar 53.91% bit (mendekati target acak ideal 50%).

2. **Level 2.** Kode Anda dan teman sama persis, tetapi proof Anda (49896, 828, 17404) berbeda. Jelaskan penyebabnya.

   _Jawaban:_
   Penyebab perbedaan tersebut berakar dari mekanisme Proof of Work yang bersifat berantai dan penggunaan NIM pribadi sebagai bibit (*seed*):
   - Pada blok genesis (blok #1), nilai `proof` ditentukan langsung oleh 4 digit terakhir NIM saya, yaitu **2157**, sedangkan teman menggunakan 4 digit NIM miliknya sendiri.
   - Algoritma PoW GeeksforGeeks mencari integer terkecil `new_proof` yang memenuhi kondisi: `SHA-256(str(new_proof**2 - previous_proof**2))` diawali oleh 4 angka nol (`0000`).
   - Karena `previous_proof` untuk blok #2 adalah NIM saya (2157), rumus kuadrat yang dievaluasi menjadi unik bagi saya. Nilai terkecil yang lolos target adalah `49896`.
   - Selanjutnya terjadi efek kaskade: `49896` menjadi `previous_proof` saat menambang blok #3, menghasilkan proof `828`. Lalu `828` menjadi basis pencarian proof blok #4, menghasilkan `17404`. Karena setiap blok bergantung secara deterministik pada proof blok pendahulunya, variasi nilai awal pada genesis menghasilkan urutan proof yang unik bagi setiap mahasiswa.

3. **Level 3.** Anda memalsukan posisi 2 dan tautan putus terdeteksi di indeks 3, sedangkan valid setelah dipalsukan = False. Jelaskan hasil ini, lalu bandingkan dengan teman yang posisi pemalsuannya berbeda.

   _Jawaban:_
   - **Tautan Putus di Indeks 3:** Dalam struktur blockchain, setiap blok $i$ menyimpan field `previous_hash` yang berisi sidik jari kriptografis dari seluruh blok $i-1$. Ketika data pada blok posisi 2 diubah (dari `"JUMRI RAMADHAN berasal dari SORONG"` menjadi `"JUMRI RAMADHAN berasal dari SORONG (DIPALSUKAN)"`), nilai `hash_blok(chain[2])` berubah secara radikal. Sementara itu, blok indeks 3 masih menyimpan `previous_hash` lama. Oleh karena itu, pemeriksaan integritas mendeteksi inkonsistensi pertama kali pada blok 3: `chain[3]["previous_hash"] != hash_blok(chain[2])`. Tautan putus selalu terdeteksi pada indeks penerus ($k+1$).
   - **Valid Setelah Dipalsukan = False:** Blockchain mendeteksi adanya manipulasi data karena rantai hash pointer terputus, sehingga status validitas rantai menjadi `False`.
   - **Kelemahan Desain GfG:** Setelah dijalankan fungsi `sambung_ulang`, `previous_hash` pada blok 3 dan 4 diperbarui mengikuti hash blok sebelumnya. Karena pada desain PoW GfG perhitungan proof (`proof**2 - previous_proof**2`) sama sekali tidak mengikutsertakan transaksi/data blok, nilai proof yang lama masih sah! Rantai palsu langsung dianggap valid (`valid_setelah_disambung_ulang = True`) tanpa perlu melakukan komputasi penambangan ulang.
   - **Perbandingan dengan Teman:** Teman yang posisi pemalsuannya berada di blok 1 akan mendeteksi tautan putus di blok 2. Namun, jika ada teman yang memalsukan data pada blok terakhir, fungsi `cari_tautan_putus` akan menghasilkan `None` (tidak ada tautan putus) karena tidak ada blok penerus yang mengacu pada blok terakhir. Hal ini membuktikan kelemahan fatal jika validasi hanya bertumpu pada pointer mundur tanpa validasi hash keseluruhan blok.

4. **Level 4.** Jelaskan dari mana angka masuk 11, keluar 28, dan bersih -17 berasal. Mengapa transaksi ke diri sendiri perlu ditolak?

   _Jawaban:_
   - **Asal-usul Angka:**
     Berdasarkan skenario transaksi personal:
     1. Transaksi 1 (Blok 2): JUMRI RAMADHAN mengirim ke TEMAN_A sejumlah hari kelahiran saya, yaitu tanggal **20** (Keluar: 20).
     2. Transaksi 2 (Blok 2): TEMAN_A mengirim ke JUMRI RAMADHAN sejumlah bulan kelahiran saya, yaitu bulan **11** (Masuk: 11).
     3. Transaksi 3 (Blok 3): JUMRI RAMADHAN mengirim ke DOSEN sejumlah formula `(NIM % 50) + 1` = $(2157 \pmod{50}) + 1 = 7 + 1 =$ **8** (Keluar: 8).
     - **Total Masuk:** 11
     - **Total Keluar:** $20 + 8 = 28$
     - **Saldo Bersih:** $11 - 28 = -17$.
   - **Urgensi Penolakan Transaksi ke Diri Sendiri (`sender == recipient`):**
     1. *Pencegahan Serangan DoS dan Bloat Mempool:* Transaksi tanpa pertukaran nilai riil dapat dieksploitasi untuk membanjiri antrean transaksi tertunda (*mempool*), menghabiskan kapasitas ruang blok (*block space*), dan menyebabkan kemacetan jaringan.
     2. *Pencegahan Manipulasi Volume (Wash Trading):* Aktor jahat dapat memalsukan aktivitas likuiditas dengan mentransfer koin bolak-balik ke alamatnya sendiri untuk mengelabui investor pasar atau algoritma bursa.
     3. *Beban Status Buku Besar (State Bloat):* Setiap transaksi yang masuk ke blok disimpan secara permanen di seluruh node jaringan. Menolak transaksi ke diri sendiri menjaga efisiensi penyimpanan dan menghindari operasi akuntansi tanpa makna ekonomi.

5. **Level 5.** Penyerang butuh 67.100 percobaan hash untuk memalsukan rantai Anda. Mengapa nonce Anda selalu sama setiap kali program dijalankan, padahal di demo Level 5 asli nonce berubah-ubah?

   _Jawaban:_
   - **Penyebab Nonce Selalu Sama:**
     Pada implementasi standar Level 5, setiap blok memuat `datetime.datetime.now()` sebagai komponen `timestamp`. Nilai waktu ini selalu berganti setiap kali kode dijalankan (sampai fraksi mikrodetik), sehingga data blok yang di-hash selalu berbeda dan nilai `nonce` yang lolos target difficulty bervariasi secara acak.
     Sebaliknya, pada kelas `BlockchainDeterministik` (Modifikasi 5), komponen waktu digantikan oleh string statis berbasis data pribadi: `f"{tanggal_lahir} #{index}"` (misalnya `"2004-11-20 #1"`). Karena seluruh komponen blok (index, timestamp statis, transactions tetap, dan previous_hash) bersifat konstan dan SHA-256 adalah fungsi deterministik murni, proses *brute-force* yang dimulai dari `nonce = 0, 1, 2, ...` akan selalu menempuh lintasan matematika yang identik. Akibatnya, nilai nonce pemenang dan hash yang dihasilkan selalu sama persis pada setiap eksekusi program.
   - **Tingkat Kesulitan Menambang Ulang:** Diperlukan total **67.100** percobaan hash untuk merekayasa blok #1 sampai blok #3. Hal ini mendemonstrasikan perbaikan desain dari Level 3: karena hash blok mencakup seluruh transaksi dan diikat oleh proof-of-work berbasis nonce, penyerang tidak bisa sekadar menyambung pointer hash; mereka wajib mengulang seluruh komputasi penambangan untuk setiap blok berikutnya (*immutability through work*).

6. **Etika data.** Anda baru saja menyimpan nama dan tanggal lahir di dalam blockchain. Jika ini blockchain publik, apa risikonya? Kaitkan dengan sifat immutability dan UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, terutama hak untuk menghapus data.

   _Jawaban:_
   - **Risiko Keamanan dan Privasi pada Blockchain Publik:**
     Blockchain publik bersifat terbuka (*permissionless*), dapat diakses oleh siapa saja di seluruh dunia, dan didistribusikan ke ribuan node. Menyimpan data pribadi sensitif seperti Nama Lengkap dan Tanggal Lahir (Data Pribadi Spesifik/Umum) secara terbuka (*plaintext*) menimbulkan risiko kebocoran data permanen, ancaman pencurian identitas (*identity theft*), *profiling* tanpa persetujuan, penipuan rekayasa sosial (*social engineering*), serta *doxxing*. Sekali data tersebut tercatat, data tersebut tersimpan selamanya.
   - **Pertentangan dengan Sifat Immutability dan UU No. 27 Tahun 2022 (UU PDP):**
     1. *Hak untuk Menghapus Data (Right to Erasure / Right to be Forgotten):* Berdasarkan Pasal 8 UU PDP, subjek data pribadi memiliki hak untuk menarik persetujuan, mengakhiri pemrosesan, serta menuntut **penghapusan dan/atau pemusnahan data pribadi** miliknya. Karakteristik fundamental blockchain adalah **immutability** (ketetapan permanen tanpa fasilitas penghapusan rekaman). Jika data pribadi disimpan langsung di dalam blok, pengendali data secara teknis mustahil memenuhi kewajiban penghapusan data tanpa melakukan *hard fork* yang merusak integritas seluruh jaringan.
     2. *Kewajiban Pengendali Data Pribadi:* Pasal 35 dan 39 UU PDP mewajibkan pengendali data menjamin kerahasiaan dan menerapkan langkah-langkah teknis keamanan untuk mencegah akses yang tidak sah. Menyimpan PII mentah secara publik melanggar prinsip *privacy by design* dan *data minimization*.
   - **Solusi Arsitektur yang Patuh Hukum:**
     Data pribadi tidak boleh disimpan secara on-chain (*off-chain storage*). Data pribadi seharusnya disimpan dalam basis data terenkripsi yang mematuhi kontrol akses dan retensi data, sedangkan yang disimpan di dalam blockchain hanyalah bukti kriptografis berupa hash sidik jari, *Zero-Knowledge Proofs* (ZKP), atau tautan berenkripsi di mana kuncinya dapat dimusnahkan (*crypto-shredding*) ketika subjek data menggunakan hak penghapusan datanya.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "profil": {
    "nama": "JUMRI RAMADHAN",
    "nim4": "2157",
    "tanggal_lahir": "2004-11-20",
    "kota_asal": "SORONG",
    "hobi": "CODING"
  },
  "level1": {
    "hash_nama": "c2ddc3ac51b43909930a72af29ce6e4686fa68ebb15cf8743827727a979323bc",
    "hash_profil": "2d3216eb85b91254c8ec7c6ffdda5d6f0728674ecb3b42a006018e1f298e8a7c",
    "hash_profil_urutan_terbalik": "2d3216eb85b91254c8ec7c6ffdda5d6f0728674ecb3b42a006018e1f298e8a7c",
    "avalanche_tanggal_persen": 53.91,
    "id_mahasiswa": "715d9757"
  },
  "level2": {
    "proof_genesis": 2157,
    "proof_blok": [
      49896,
      828,
      17404
    ],
    "pemilik_semua_blok": [
      "715d9757"
    ],
    "valid": true
  },
  "level3": {
    "posisi_dipalsukan": 2,
    "data_asli": "JUMRI RAMADHAN berasal dari SORONG",
    "data_palsu": "JUMRI RAMADHAN berasal dari SORONG (DIPALSUKAN)",
    "valid_asli": true,
    "tautan_putus_di": 3,
    "valid_setelah_dipalsukan": false,
    "valid_setelah_disambung_ulang": true
  },
  "level4": {
    "riwayat": [
      [
        2,
        {
          "sender": "JUMRI RAMADHAN",
          "recipient": "TEMAN_A",
          "amount": 20
        }
      ],
      [
        2,
        {
          "sender": "TEMAN_A",
          "recipient": "JUMRI RAMADHAN",
          "amount": 11
        }
      ],
      [
        3,
        {
          "sender": "JUMRI RAMADHAN",
          "recipient": "DOSEN",
          "amount": 8
        }
      ]
    ],
    "ringkasan_saldo": {
      "masuk": 11,
      "keluar": 28,
      "bersih": -17
    },
    "kirim_ke_diri_sendiri_ditolak": true,
    "amount_nol_ditolak": true,
    "jumlah_blok": 3
  },
  "level5": {
    "nonce": [
      10056,
      2267,
      52451,
      102944
    ],
    "hash": [
      "0000a727c5bedd9178ae8e5f2ad1f7f0a5c6e1092052f241adcd1e270ad22ef8",
      "00004bfa77978843e69621884774674b856ea13c8d88a67b56070465dc327072",
      "000045d3020eba8500efe7751350cc8caff108eb2a846d98ebc7b858b8d149e4",
      "00009fc31ac3c37c320e4c0d1f41931ec840363e492bfb49204fe280acbc11c1"
    ],
    "valid": true,
    "valid_setelah_dipalsukan": false,
    "percobaan_tambang_ulang": 67100,
    "valid_setelah_tambang_ulang": true
  },
  "kode_verifikasi": "CEE0EC63CF64"
}
```
