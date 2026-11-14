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
6     Eksperimen difficulty             0/13       belum
7     Tanda tangan digital              0/10       belum
8     Jaringan & konsensus               0/7       belum
9     Reward & saldo                    0/13       belum
--------------------------------------------------------------
TOTAL                                  47/90         56%
==============================================================
```

---

## Level 1 — Fungsi Hash
1. **Mengapa hash disebut "sidik jari digital"? Sebutkan tiga sifat fungsi hash kriptografis.**
   - Hash disebut sidik jari digital karena dapat merepresentasikan data berukuran berapa pun ke dalam string acak berukuran tetap (256 bit untuk SHA-256) yang unik bagi data tersebut. Setiap perubahan sekecil apa pun pada data input akan menghasilkan hash yang sangat berbeda.
   - Tiga sifat utama fungsi hash kriptografis:
     1. *Pre-image resistance (One-way):* Sangat sulit secara komputasi untuk mencari input $x$ jika hanya diketahui $h = \text{hash}(x)$.
     2. *Second pre-image resistance (Weak collision resistance):* Jika diberikan input $x$, sangat sulit menemukan input berbeda $y \neq x$ sedemikian sehingga $\text{hash}(x) = \text{hash}(y)$.
     3. *Collision resistance (Strong collision resistance):* Sangat sulit menemukan dua pasangan input sembarang $x$ dan $y$ yang menghasilkan nilai hash yang sama ($\text{hash}(x) = \text{hash}(y)$).
2. **Berapa persen bit yang berubah ketika Anda mengganti satu huruf? Coba 3 pasangan teks berbeda.**
   - Hasil eksperimen:
     - `"Teknologi Blockchain"` vs `"teknologi Blockchain"`: **48.83%** bit berubah.
     - `"Jumri Ramadhan"` vs `"jumri Ramadhan"`: **57.03%** bit berubah.
     - `"Sorong 2026"` vs `"Sorong 2027"`: **51.56%** bit berubah.
   - Rata-rata perubahan bit berada di sekitar **50%**, membuktikan berjalannya *avalanche effect* secara optimal.
3. **Apa yang terjadi jika `hash_dict` tidak memakai `sort_keys=True`? Mengapa itu berbahaya untuk blockchain?**
   - Tanpa `sort_keys=True`, representasi string JSON dari kamus (*dictionary*) bergantung pada urutan penyisipan key di memori runtime. Jika dua node memproses data transaksi yang sama namun urutan key-nya berbeda, `json.dumps()` menghasilkan teks yang berbeda sehingga hash blok menjadi tidak cocok. Ini berbahaya karena dapat menyebabkan percabangan (*fork*) konsensus yang tidak disengaja antar node jaringan.

## Level 2 — Blockchain Dasar
1. **Apa fungsi `previous_hash` pada blok genesis, dan mengapa nilainya `"0"`?**
   - `previous_hash` berfungsi sebagai pengait kriptografis yang menyambungkan blok saat ini dengan blok sebelumnya. Pada blok genesis (blok pertama), tidak ada blok pendahulu di dunia, sehingga `previous_hash` diisi dengan nilai konvensi standar seperti `"0"` (atau 64 angka nol) untuk menandai awal mula berdirinya rantai (*root of trust*).
2. **Jalankan demo dengan difficulty 3, 4, dan 5. Catat nilai `proof` dan rasakan lamanya mining.**

| Difficulty | Proof blok #2 | Perkiraan waktu |
|---|---|---|
| 3 | 533 | < 0.01 detik |
| 4 | 533 | < 0.01 detik |
| 5 | 632238 | ~1.36 detik |

*Catatan:* Pada difficulty 5, pencarian proof memerlukan iterasi lebih dari 600.000 kali pengujian kuadrat dan hash, sehingga waktu eksekusi melonjak signifikan dibandingkan difficulty 3 dan 4.

## Level 3 — Tampering
1. **Saat Anda mengubah data di blok posisi *k*, `cari_tautan_putus` melaporkan posisi *k+1*. Jelaskan mengapa.**
   - Karena blok posisi $k+1$ menyimpan `previous_hash` yang merujuk pada hash asli dari blok $k$. Ketika data pada blok $k$ diubah, nilai hash blok $k$ yang baru tidak lagi cocok dengan nilai `previous_hash` yang sudah tercatat pada blok $k+1$.
2. **Mengapa perubahan pada blok terakhir tidak terdeteksi oleh `cari_tautan_putus`?**
   - Karena blok terakhir belum memiliki blok penerus ($k+1$) yang menyimpan nilai `previous_hash`-nya. Tidak ada blok sesudahnya yang bisa menguji kecocokan hash blok terakhir tersebut.
3. **Setelah `sambung_ulang`, rantai palsu dianggap valid. Apa kelemahan desain PoW di artikel GfG yang menyebabkannya?**
   - Kelemahan desain PoW di artikel GeeksforGeeks adalah rumus Proof of Work-nya (`proof**2 - previous_proof**2`) hanya bergantung pada angka proof antar blok, dan sama sekali **tidak mengikutsertakan isi atau transaksi blok** ke dalam perhitungan hash PoW. Akibatnya, penyerang cukup menghitung ulang field `previous_hash` secara berurutan (*re-link*) tanpa perlu menambang ulang proof.

## Level 4 — Transaksi
1. **Mengapa transaksi tidak langsung masuk ke blok, tetapi menunggu dulu di `pending_transactions`?**
   - Dalam sistem terdesentralisasi, transaksi yang disiarkan oleh pengguna harus dikumpulkan dan diverifikasi terlebih dahulu di mempool (*memory pool*). Blok memiliki batasan ukuran dan interval waktu penambangan, sehingga transaksi menunggu diantrekan sampai penambang (*miner*) memilihnya untuk dibundel ke dalam blok baru saat proses mining berhasil.
2. **Mengapa `create_block` harus memakai salinan `list(self.pending_transactions)`? Apa bug yang muncul jika tidak?**
   - Jika tidak disalin (misalnya hanya merujuk langsung `self.pending_transactions`), blok yang tersimpan di chain akan mereferensikan list memori yang sama. Saat `self.pending_transactions` dikosongkan (`[]`) atau ditambahi transaksi baru, isi transaksi pada blok-blok sebelumnya di chain akan ikut berubah atau terhapus, merusak catatan historis buku besar.

## Level 5 — PoW dengan Nonce
1. **Bandingkan Level 3 dan Level 5: mengapa serangan "sambung ulang" gagal di sini?**
   - Di Level 5, yang di-hash dalam Proof of Work adalah **seluruh isi blok** (termasuk `transactions`, `previous_hash`, dan `nonce`). Jika penyerang hanya menyambung `previous_hash` tanpa menambang ulang, nilai `hash` blok tidak akan diawali oleh sejumlah angka nol target difficulty, dan hash yang tercatat tidak cocok dengan `hash_block(block)`. Rantai seketika ditolak sebagai tidak valid.
2. **Jalankan demo. Berapa percobaan hash yang dibutuhkan penyerang untuk memalsukan blok #1 dari 3 blok? Perkirakan biayanya jika rantai berisi 1.000 blok dan difficulty 6.**
   - Pada demo Level 5, penyerang membutuhkan lebih dari 270.000 percobaan hash untuk menambang ulang hanya 3 blok.
   - Pada difficulty 6, probabilitas suatu hash diawali 6 angka nol heksadesimal adalah $1 / 16^6 = 1 / 16.777.216$. Rata-rata dibutuhkan ~16,78 juta hash untuk satu blok. Jika ada 1.000 blok sesudahnya, penyerang membutuhkan sekitar:
     $$1.000 \times 16.777.216 \approx 16,78 \text{ miliar percobaan hash}.$$
   - Biaya perangkat keras, waktu komputasi, dan energi listrik yang dibutuhkan membuat serangan pengubahan data masa lalu menjadi mustahil secara ekonomis.

---
*(Level 6–9 belum dikerjakan / materi lanjutan)*
