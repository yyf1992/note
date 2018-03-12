import msgpackrpc
import time
import thread
import threading

Num = 1

def run_call():
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800), timeout=20)
    before = time.time()
    for x in range(Num):
        client.call('sum', 1, 2)
    after = time.time()
    diff = after - before

    print("call: {0} qps".format(Num / diff))

def run_call_async():
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800), timeout=20)
    before = time.time()
    for x in range(Num):
        # TODO: replace with more heavy sample
        print 11111
        future = client.call_async('sum', 1, 2)
        future.get()
    after = time.time()
    diff = after - before

    print("async: {0} qps".format(Num / diff))


def run_call_async2():
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800), timeout=20)
    before = time.time()
    for x in range(Num):
        # TODO: replace with more heavy sample
        print 333333
        future = client.call_async('sum2', 1, 2)
        future.get()
    after = time.time()
    diff = after - before

    print("async: {0} qps".format(Num / diff))

def run_notify():
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))
    before = time.time()
    for x in range(Num):
        client.notify('sum', 1, 2)
    after = time.time()
    diff = after - before

    print("notify: {0} qps".format(Num / diff))

# for i in range(2):
#     t = threading.Thread(target=run_call)
#     t.start()
#     t.join()

# run_call()
# run_call_async()
# run_notify()

import sys
a = sys.argv[1]
globals()[a]()
