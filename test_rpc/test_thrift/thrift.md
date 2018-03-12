# Thrift相关文档
## Thrift脚本可定义的数据类型：
- 基本类型
    - bool：布尔值，true 或 false，对应 Java 的 boolean
    - byte：8 位有符号整数，对应 Java 的 byte
    - i16：16 位有符号整数，对应 Java 的 short
    - i32：32 位有符号整数，对应 Java 的 int
    - i64：64 位有符号整数，对应 Java 的 long
    - double：64 位浮点数，对应 Java 的 double
    - string：未知编码文本或二进制字符串，对应 Java 的 String

- 结构体类型
    - struct：定义公共的对象，类似于 C 语言中的结构体定义，在 Java 中是一个 JavaBean

- 容器类型
    - list：对应 Java 的 ArrayList
    - set：对应 Java 的 HashSet
    - map：对应 Java 的 HashMap

- 异常类型
    - exception：对应 Java 的 Exception

- 服务类型
    - service：对应服务的类


## Thrift 协议
- TBinaryProtocol     —— 二进制编码格式进行数据传输
- TCompactProtocol    —— 高效率的、密集的二进制编码格式进行数据传输
- TJSONProtocol       —— 使用 JSON 的数据编码协议进行数据传输
- TSimpleJSONProtocol —— 只提供 JSON 只写的协议，适用于通过脚本语言解析


## Thrift 传输层
- TSocket                 —— 使用阻塞式 I/O 进行传输，是最常见的模式
- TFramedTransport        —— 使用非阻塞方式，按块的大小进行传输，类似于 Java 中的 NIO，若使用 TFramedTransport 传输层，其服务器必须修改为非阻塞的服务类型
- TNonblockingTransport   —— 使用非阻塞方式，用于构建异步客户端，使用方法请参考 Thrift 异步客户端构建

## Thrift 服务端类型
- TSimpleServer       —— 单线程服务器端使用标准的阻塞式 I/O, 单线程单进程，并发处理得排队。
- TThreadedServer     —— 多线程服务器端使用标准的阻塞式 I/O，每个连接产生一个线程
- TThreadPoolServer   —— 多线程服务器端使用标准的阻塞式 I/O, 固定大小线程池,处理能力受限于线程池的工作能力
- TNonblockingServer  —— 单线程服务器端使用非阻塞式 I/O，使用方法请参考 Thrift 异步客户端构建
- TForkingServer      -- fork新进程处理每个请求

## Thrift 异步客户端构建
        Thrift 提供非阻塞的调用方式，可构建异步客户端。我们可以构建一个 TNonblockingServer 服务类型的服务端，
    在客户端构建一个 TFramedTransport 传输层的同步客户端和一个 TNonblockingTransport 传输层的异步客户端，
    那么一个服务就可以通过一个 socket 端口提供两种不同的调用方式。