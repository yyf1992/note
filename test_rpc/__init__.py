#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'

'''
py-server请求cpp-server的 rpc 调用流程：

1.py-server 每个进程维护一个rpc-client(与rpc-server建立连接),通过rpc-client调用rpc-server中的接口

2.rpc-server 维护一个r2c-client池(rpc-server与cpp-server建立连接)，从r2c-client池中选择一个client调用cpp-server中的接口

3.cpp-server 提供rpc服务，需要支持并发操作

#########################################################################################
#    py-server(rpc-client)     --->       rpc-server x N        --->     cpp-server     #
#                                        (r2c-client pool)              (rpc-server)    #
#    py-server(rpc-client)     --->                                                     #
#                                                                                       #
#    py-server(rpc-client)     --->                                                     #
#            .                                                                          #
#            .                                                                          #
#########################################################################################


cpp-server请求战前数据：
 cpp-server     --->        rpc-server x N
(rpc-client)


'''