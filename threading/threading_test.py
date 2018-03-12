#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'

import threading, time, random

count = 0


class Counter(threading.Thread):
    def __init__(self, lock, threadName):
        '''@summary: 初始化对象。

        @param lock: 琐对象。
        @param threadName: 线程名称。
        '''
        super(Counter, self).__init__(name=threadName)  # 注意：一定要显式的调用父类的初始 化函数。
        self.lock = lock

    def run(self):
        '''@summary: 重写父类run方法，在线程启动后执行该方法内的代码。
        '''
        print self.getName(), self.ident
        global count
        self.lock.acquire()
        self.lock.acquire()
        for i in xrange(10000):
            count = count + 1
        self.lock.release()
        self.lock.release()


lock = threading.RLock()
for i in range(5):
    a = Counter(lock, "thread-" + str(i))
    a.start()
    # a.join()
    # print a.getName()
print 11111
time.sleep(2)  # 确保线程都执行完毕
print count

# import threading, time
# def doWaiting():
#     print 'start waiting:', time.strftime('%H:%M:%S')
#     time.sleep(3)
#     print 'stop waiting', time.strftime('%H:%M:%S')
# thread1 = threading.Thread(target = doWaiting)
# thread1.start()
# time.sleep(1)  #确保线程thread1已经启动
# print 'start join'
# thread1.join()	#将一直堵塞，直到thread1运行结束。
# print 'end join'


# ---- Condition
# ---- 捉迷藏的游戏
import threading, time


class Seeker(threading.Thread):
    """
    找
    """
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)  # 确保先运行Hider中的方法

        self.cond.acquire()  # b
        print self.name + ': 我已经把眼睛蒙上了'
        self.cond.notify()
        self.cond.wait()  # c
        # f
        print self.name + ': 我找到你了 ~_~'
        self.cond.notify()
        self.cond.release()
        # g
        print self.name + ': 我赢了'  # h


class Hider(threading.Thread):
    """
    藏
    """
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()  # a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
# d
        print self.name + ': 我已经藏好了，你快来找我吧'
        self.cond.notify()
        self.cond.wait()  # e
        # h
        self.cond.release()
        print self.name + ': 被你找到了，哎~~~'

cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()