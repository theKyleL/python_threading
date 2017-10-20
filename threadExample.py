#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
"""
Threading in python
original example by: sentdex

Illustrates python threading with semaphores/locks for making applications thread-safe
"""

import threading
from queue import Queue 
import time


print_lock = threading.Lock()


def exampleJob(worker):
	time.sleep(0.5)

	with print_lock:
		print(threading.current_thread().name, worker)


def threader():
	while True:
		worker = q.get()
		exampleJob(worker)
		q.task_done()


q = Queue()


for x in range(10):
	t = threading.Thread(target = threader)
	t.daemon = True
	t.start()


start = time.time()


for worker in range(20):
	q.put(worker)


q.join()


print("Job took:", time.time()-start)

