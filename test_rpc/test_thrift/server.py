#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'

import time

from thrift.protocol import TBinaryProtocol, TCompactProtocol, TJSONProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from example import HelloWorld

class HelloWorldHandler:
    def ping(self):
        time.sleep(10)
        return "pong"

    def say(self, msg):
        ret = "Received: " + msg
        print ret
        return ret

    def bay(self, msg):
        print msg
        return 'ok'

def main():
    handler = HelloWorldHandler()
    processor = HelloWorld.Processor(handler)
    transport = TSocket.TServerSocket("localhost", 9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # pfactory = TCompactProtocol.TCompactProtocolFactory()
    # pfactory = TJSONProtocol.TJSONProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    # server = TServer.TForkingServer(processor, transport, tfactory, pfactory)

    print "Starting thrift server in python..."
    server.serve()
    print "done!"

if __name__ == '__main__':
    main()