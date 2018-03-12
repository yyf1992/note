import msgpackrpc
import time

class SumServer(object):
    def sum(self, x, y):
        for i in range(10):
            time.sleep(1)
            print 'sleep %s' % i
        return x + y
    def sum2(self, x, y):
        for i in range(10):
            time.sleep(1)
            print 'sleep2222 %s' % i
        return x + y

server = msgpackrpc.Server(SumServer())
server.listen(msgpackrpc.Address("localhost", 18800))
server.start()
