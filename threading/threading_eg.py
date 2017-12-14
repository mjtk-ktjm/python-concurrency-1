import threading
from time import sleep

def run_as_thread(sleeper, thread_num):
  """Start a thread, sleep. Print thread identification to stdout."""
  print("Doing some work in thread {}...".format(thread_num))
  # https://stackoverflow.com/questions/4456581/python3-sleep-problem
  # print("Doing some work in thread...", flush=True)
  # sys.stdout.flush()
  sleep(sleeper)
  print("Woke {}!".format(thread_num))
  return

if __name__ == "__main__":
  """demo threading with simple function and time.sleep."""

  i = 1
  sleep_for = 7
  t = threading.Thread(target=run_as_thread, args=(sleep_for, i,))
  t.start()

  i += 1
  sleep_for = 3
  u = threading.Thread(target=run_as_thread, args=(sleep_for, i,))
  u.start()
  t.join()
  u.join()

