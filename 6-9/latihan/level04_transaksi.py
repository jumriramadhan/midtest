"""
LEVEL 4 — Menambahkan Transaksi ke dalam Blok (LATIHAN)
=============================================================

Blok di artikel GfG tidak berisi data apa pun. Di sini kita menambahkan
"mempool" (daftar transaksi tertunda) yang akan dimasukkan ke blok saat mining.

Tujuan belajar:
  * Konsep transaksi tertunda (pending / mempool).
  * Validasi input transaksi.
  * Menelusuri riwayat transaksi di seluruh rantai.

Jalankan tes:  python cek_nilai.py 4
"""

import datetime
import hashlib
import json


class Blockchain:
    def __init__(self, difficulty: int = 3):
        self.difficulty = difficulty
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=1, previous_hash="0")

    # ---------- SUDAH DISEDIAKAN ----------
    def hash(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def valid_proof(self, previous_proof, proof):
        h = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
        return h.startswith("0" * self.difficulty)

    def proof_of_work(self, previous_proof):
        proof = 1
        while not self.valid_proof(previous_proof, proof):
            proof += 1
        return proof

    def last_block(self):
        return self.chain[-1]

    # ---------- BAGIAN YANG DIKERJAKAN (isi semua TODO) ----------
    def create_block(self, proof: int, previous_hash: str) -> dict:
        """Buat blok yang berisi key: index, timestamp, transactions, proof, previous_hash.
        `transactions` = salinan list pending_transactions saat ini.
        Setelah blok ditambahkan ke chain, kosongkan pending_transactions.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "transactions": list(self.pending_transactions),
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount) -> int:
        """Tambahkan transaksi {'sender','recipient','amount'} ke pending_transactions.

        Lempar ValueError jika:
          * sender atau recipient bukan string atau string kosong
          * sender == recipient
          * amount bukan angka (int/float, BUKAN bool) atau amount <= 0
        Kembalikan index blok yang AKAN memuat transaksi ini (index blok terakhir + 1).
        """
        if not isinstance(sender, str) or not sender.strip():
            raise ValueError("Sender tidak valid")
        if not isinstance(recipient, str) or not recipient.strip():
            raise ValueError("Recipient tidak valid")
        if sender == recipient:
            raise ValueError("Sender dan recipient tidak boleh sama")
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount harus berupa angka positif")

        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        })
        return self.last_block()["index"] + 1

    def mine_block(self) -> dict:
        """Tambang blok baru yang memuat semua transaksi tertunda."""
        prev_block = self.last_block()
        proof = self.proof_of_work(prev_block["proof"])
        previous_hash = self.hash(prev_block)
        return self.create_block(proof, previous_hash)

    def riwayat(self, nama: str) -> list:
        """Kembalikan list tuple (index_blok, transaksi) untuk setiap transaksi
        di dalam CHAIN (bukan pending) yang melibatkan `nama` sebagai sender atau recipient,
        berurutan dari blok paling awal.
        """
        hasil = []
        for block in self.chain:
            for tx in block.get("transactions", []):
                if tx.get("sender") == nama or tx.get("recipient") == nama:
                    hasil.append((block["index"], tx))
        return hasil


if __name__ == "__main__":
    bc = Blockchain()
    bc.add_transaction("Ani", "Budi", 5)
    bc.add_transaction("Budi", "Citra", 2)
    bc.mine_block()
    bc.add_transaction("Citra", "Ani", 1)
    bc.mine_block()
    print(json.dumps(bc.chain, indent=2))
    print("Riwayat Budi:", bc.riwayat("Budi"))
