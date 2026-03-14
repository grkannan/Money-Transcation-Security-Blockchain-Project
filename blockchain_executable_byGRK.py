import hashlib
import json
import time
import Blockchain as blockchain

# --- THE INTERACTIVE MENU ---
def main():
    bc = blockchain.Blockchain();

    while True:
        print("\n[1] Add Transaction")
        print("[2] Mine Block (Process Transactions)")
        print("[3] View Ledger/Chain")
        print("[4] Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            s = input("Sender Name: ")
            r = input("Receiver Name: ")
            a = input("Amount: ")
            bc.add_transaction(s, r, a)
        
        elif choice == '2':
            if not bc.pending_transactions:
                print("\n[!] No transactions to mine!")
            else:
                new_block = bc.create_block()
                print(f"\n[*] Block #{new_block['index']} mined successfully!")

        elif choice == '3':
            bc.display_chain()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()