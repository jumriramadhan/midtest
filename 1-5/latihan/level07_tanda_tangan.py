"""
LEVEL 7 — Kunci Publik/Privat dan Tanda Tangan Digital (LATIHAN)
======================================================================

Di level sebelumnya siapa pun bisa menulis transaksi atas nama orang lain.
Sekarang setiap transaksi harus ditandatangani dengan kunci privat pengirim.
Kurva yang dipakai: SECP256k1 (kurva yang sama dengan Bitcoin dan Ethereum).

Butuh library:  pip install ecdsa

Tujuan belajar:
  * Pasangan kunci privat/publik dan alamat (address).
  * Menandatangani dan memverifikasi transaksi.
  * Mengapa transaksi yang diubah setelah ditandatangani menjadi tidak sah.

Jalankan tes:  python cek_nilai.py 7
"""

import hashlib
import json

from ecdsa import BadSignatureError, SECP256k1, SigningKey, VerifyingKey


def buat_pasangan_kunci():
    """Buat kunci SECP256k1 baru. Kembalikan (kunci_privat_hex, kunci_publik_hex).
    Petunjuk: SigningKey.generate(curve=SECP256k1), .to_string().hex(), .get_verifying_key()
    """
    # TODO: lengkapi fungsi ini
    # Petunjuk: sk = SigningKey.generate(curve=SECP256k1); vk = sk.get_verifying_key()
    raise NotImplementedError("TODO: buat_pasangan_kunci")


def alamat_dari_kunci_publik(kunci_publik_hex: str) -> str:
    """Alamat = 40 karakter pertama dari SHA-256(bytes kunci publik)."""
    # TODO: lengkapi fungsi ini
    # Petunjuk: bytes.fromhex(kunci_publik_hex) lalu sha256, ambil [:40]
    raise NotImplementedError("TODO: alamat_dari_kunci_publik")


def pesan_transaksi(tx: dict) -> bytes:
    """Bytes kanonik yang ditandatangani: JSON (sort_keys=True) dari HANYA key
    'sender', 'recipient', 'amount' (key lain seperti 'signature' diabaikan).
    """
    # TODO: lengkapi fungsi ini
    # Petunjuk: Ambil hanya 3 key, lalu json.dumps(..., sort_keys=True).encode()
    raise NotImplementedError("TODO: pesan_transaksi")


def tanda_tangani(tx: dict, kunci_privat_hex: str) -> str:
    """Tandatangani pesan_transaksi(tx). Kembalikan tanda tangan dalam hex."""
    # TODO: lengkapi fungsi ini
    # Petunjuk: SigningKey.from_string(bytes.fromhex(...), curve=SECP256k1).sign(pesan)
    raise NotImplementedError("TODO: tanda_tangani")


def verifikasi(tx: dict, tanda_tangan_hex: str, kunci_publik_hex: str) -> bool:
    """True jika tanda tangan cocok dengan transaksi dan kunci publik.
    Kembalikan False (jangan melempar exception) jika tidak cocok / format salah.
    """
    # TODO: lengkapi fungsi ini
    # Petunjuk: VerifyingKey.from_string(...).verify(sig_bytes, pesan)
    # Petunjuk: Tangkap BadSignatureError dan ValueError -> return False
    raise NotImplementedError("TODO: verifikasi")


def transaksi_sah(tx: dict, tanda_tangan_hex: str, kunci_publik_hex: str) -> bool:
    """Transaksi sah jika (1) tanda tangan valid DAN
    (2) tx['sender'] sama dengan alamat dari kunci publik tersebut.
    """
    # TODO: lengkapi fungsi ini
    # Petunjuk: Gabungkan alamat_dari_kunci_publik() dan verifikasi()
    raise NotImplementedError("TODO: transaksi_sah")


if __name__ == "__main__":
    priv, pub = buat_pasangan_kunci()
    alamat = alamat_dari_kunci_publik(pub)
    tx = {"sender": alamat, "recipient": "alamat_budi", "amount": 5}
    sig = tanda_tangani(tx, priv)
    print("Alamat Ani :", alamat)
    print("Tanda tangan:", sig[:32], "...")
    print("Sah?", transaksi_sah(tx, sig, pub))
    tx["amount"] = 500
    print("Setelah amount diubah jadi 500, sah?", transaksi_sah(tx, sig, pub))
