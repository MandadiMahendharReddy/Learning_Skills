print("============Multi Thread===========")
import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")

# Creating threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
print("All tasks completed")

# Task A started
# Task B started
# Task A finished
# Task B finished
# All tasks completed

print("============Multi Process===========")

from multiprocessing import Process
import time

def task(name):
    print(f"Process {name} started")
    time.sleep(2)
    print(f"Process {name} finished")

if __name__ == "__main__":
    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All processes completed")
