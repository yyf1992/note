#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'

from thrift import Thrift
from thrift.protocol import TBinaryProtocol, TCompactProtocol, TJSONProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from example import HelloWorld


def main():

    try:
        transport = TSocket.TSocket('localhost', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        # protocol = TCompactProtocol.TCompactProtocol(transport)
        # protocol = TJSONProtocol.TJSONProtocol(transport)

        client = HelloWorld.Client(protocol)
        transport.open()

        # print "client - ping"
        # print "server - " + client.ping()

        # print "client - say"
        # msg = client.say("hello!")
        import msgpack
        # import cPickle
        # msg = client.say(cPickle.dumps('1'))
        # print "server - " + msg

        print 'client - bay'
        msg = client.bay({'1': msgpack.dumps(1).encode('zip')})
        print 'server - ' + msg

        transport.close()

    except Thrift.TException, ex:
        print "%s" % (ex.message)


if __name__ == '__main__':
    main()