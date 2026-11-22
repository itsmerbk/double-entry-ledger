class Ledger:
    def __init__(self): self.entries = []
    def post(self, debit_acct, credit_acct, amount):
        if amount <= 0: raise ValueError("Positive amount required")
        self.entries.append((debit_acct, amount)); self.entries.append((credit_acct, -amount))
    def balance(self, acct): return sum(amt for a, amt in self.entries if a == acct)
    def is_balanced(self): return sum(amt for _, amt in self.entries) == 0

if __name__ == "__main__":
    lg = Ledger(); lg.post("cash", "revenue", 1500)
    assert lg.is_balanced() and lg.balance("cash") == 1500
    print("[PASS] 092_double_entry_ledger")
