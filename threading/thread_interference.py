import threading


class BankAccount:
  def __init__(self):
    self.bal = 0

  def deposit(self, amt):
    balance = self.bal
    self.bal = balance + amt
    print("Remaining Balance is {}".format(self.bal))

  def withdraw(self, amt):
    balance = self.bal
    self.bal = balance - amt
    print("Remaining Balance is {}".format(self.bal))


if __name__ == "__main__":
  b = BankAccount()
  t1 = threading.Thread(target=b.deposit, args=(100,))
  t2 = threading.Thread(target=b.withdraw, args=(50,))

  t1.start()
  t2.start()

