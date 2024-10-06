import sys 
from bank_account import BankAccount

def main():
    account = BankAccount(100)   # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')