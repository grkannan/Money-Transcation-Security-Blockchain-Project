import hashlib, json, time

def hash_me(msg):
    return hashlib.sha256(json.dumps(msg, sort_keys=True).encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.pending_transactions = []
        self.chain = []
        # Create Genesis Block (The very first block)
        self.create_block(previous_hash="0000000000000000", message="Genesis Block")

    def add_transaction(self, sender, receiver, amount):
        tx = {"sender": sender, "receiver": receiver, "amount": amount}
        self.pending_transactions.append(tx)
        print(f"\n[+] Transaction added: {sender} -> {receiver} (${amount})")

    def create_block(self, previous_hash=None, message=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.pending_transactions if not message else message,
            "previous_hash": previous_hash or self.chain[-1]["hash"]
        }
        # Fingerprint the block
        block["hash"] = hash_me(block)
        self.chain.append(block)
        self.pending_transactions = [] # Clear the "mempool"
        return block

    def display_chain(self):
        print("\n--- CURRENT BLOCKCHAIN ---")
        for block in self.chain:
            print(f"Block #{block['index']}")
            print(f"  Hash: {block['hash']}")
            print(f"  Prev: {block['previous_hash']}")
            print(f"  Data: {block['transactions']}")
            print("-" * 30)