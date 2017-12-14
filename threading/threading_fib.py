import threading


class FibThread(threading.Thread):

  def __init__(self, num):
    super().__init__()
    self.num = num

  def run(self):
    fib = [0] * (self.num + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, self.num+1):
      fib[i] = fib[i -1] + fib[i -2]
      print(fib[self.num])


myFib1 = FibThread(7)
myFib2 = FibThread(13)

myFib1.start()
myFib2.start()

myFib1.join()
myFib2.join()

