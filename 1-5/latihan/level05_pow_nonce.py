"""
LEVEL 5 — Proof of Work yang Benar: Hash Seluruh Isi Blok + Nonce (LATIHAN)
=================================================================================

Di Level 3 kita melihat kelemahan: proof GfG tidak bergantung pada isi blok,
sehingga penyerang cukup menyambung ulang previous_hash tanpa menambang ulang.

Perbaikan (seperti Bitcoin): yang di-hash adalah SELURUH isi blok, termasuk
`nonce`. Penambang mengubah nonce sampai hash blok diawali N angka nol.
Hash hasil mining disimpan di field `hash`.

Tujuan belajar:
  * Nonce dan target difficulty.
  * Mengapa mengubah satu blok memaksa penyerang menambang ulang
    SEMUA blok sesudahnya (immutability).

Jalankan tes:  python cek_nilai.py 5
"""

import datetime
import hashlib
import json


class Blockchain:
    def __init__(self, difficulty: int = 3):
        self.difficulty = difficulty
        self.chain = []
        genesis = {
            "index": 0,
            "timestamp": str(datetime.datetime.now()),
            "transactions": [],
            "previous_hash": "0" * 64,
            "nonce": 0,
        }
        self.proof_of_work(genesis)
        self.chain.append(genesis)

    # ---------- BAGIAN YANG DIKERJAKAN (isi semua TODO) ----------
    @staticmethod
    def hash_block(block: dict) -> str:
        """SHA-256 dari blok (JSON, sort_keys=True) TANPA menyertakan key 'hash'.
        Jangan mengubah dict asli.
        """
        clean = {k: v for k, v in block.items() if k != "hash"}
        return hashlib.sha256(json.dumps(clean, sort_keys=True).encode()).hexdigest()

    def proof_of_work(self, block: dict) -> int:
        """Mulai dari block['nonce'] = 0, naikkan nonce sampai hash_block(block)
        diawali `difficulty` angka nol. Simpan hasilnya di block['hash'].
        Kembalikan JUMLAH PERCOBAAN (nonce terakhir + 1).
        """
        block["nonce"] = 0
        target = "0" * self.difficulty
        while True:
            h = self.hash_block(block)
            if h.startswith(target):
                block["hash"] = h
                return block["nonce"] + 1
            block["nonce"] += 1

    def new_block(self, transactions: list) -> dict:
        """Buat blok baru {index, timestamp, transactions, previous_hash, nonce},
        dengan previous_hash = hash blok terakhir dan index = index terakhir + 1.
        Tambang dengan proof_of_work(), tambahkan ke chain, lalu kembalikan blok.
        """
        block = {
            "index": self.chain[-1]["index"] + 1,
            "timestamp": str(datetime.datetime.now()),
            "transactions": list(transactions),
            "previous_hash": self.chain[-1]["hash"],
            "nonce": 0,
        }
        self.proof_of_work(block)
        self.chain.append(block)
        return block

    def chain_valid(self) -> bool:
        """Untuk SETIAP blok (termasuk genesis):
          * block['hash'] == hash_block(block)
          * block['hash'] diawali `difficulty` angka nol
        Untuk setiap blok selain genesis:
          * block['previous_hash'] == chain[i-1]['hash']
        """
        target = "0" * self.difficulty
        for i, block in enumerate(self.chain):
            h = block.get("hash")
            if not h or h != self.hash_block(block):
                return False
            if not h.startswith(target):
                return False
            if i > 0:
                if block.get("previous_hash") != self.chain[i - 1].get("hash"):
                    return False
        return True

    def tambang_ulang_dari(self, posisi: int) -> int:
        """Simulasi penyerang: tambang ulang blok chain[posisi] sampai blok terakhir
        secara berurutan (perbarui previous_hash lalu proof_of_work).
        Kembalikan total jumlah percobaan hash.
        """
        total_percobaan = 0
        for i in range(posisi, len(self.chain)):
            if i > 0:
                self.chain[i]["previous_hash"] = self.chain[i - 1]["hash"]
            total_percobaan += self.proof_of_work(self.chain[i])
        return total_percobaan


if __name__ == "__main__":
    bc = Blockchain(difficulty=4)
    for tx in (["Ani->Budi 5"], ["Budi->Citra 2"], ["Citra->Dodi 1"]):
        b = bc.new_block(tx)
        print(f"Blok #{b['index']} nonce={b['nonce']} hash={b['hash'][:16]}...")
    print("Valid?", bc.chain_valid())

    bc.chain[1]["transactions"] = ["Ani->Budi 500"]
    print("Setelah diubah valid?", bc.chain_valid())
    usaha = bc.tambang_ulang_dari(1)
    print(f"Penyerang menambang ulang dengan {usaha} percobaan hash. Valid?", bc.chain_valid())
