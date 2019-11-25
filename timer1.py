import time

def worker():
    print(time.time())
    time.sleep(8)

interval = 5
while True:
    worker()
    time.sleep(interval)
