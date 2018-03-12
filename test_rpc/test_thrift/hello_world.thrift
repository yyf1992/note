#namespace go inft
#
#typedef i32 int;
#typedef i64 long;
#
#enum Player {
#    JAVA = 0;
#    FLASH = 1;
#}
#struct Person {
#    1: required string name;
#    2: optional map<string, long> tel;
#}
#struct MediaRp {
#    1: required string uri;
#    2: optional string title;
#    3: required int width;
#    4: required int height;
#    5: required list<Person> person;
#    6: required Player player;
#}
#struct MediaRq {
#    1: required string uri;
#}
#
#service media {
#    MediaRp media(1: MediaRq mediaRq);
#}


namespace py example    # 代码生成目录，默认与thrift文件前缀相同
struct Data {           # 对应python的类，会在namespace.ttypes.py中生成对应的类
    1: string text,
    2: i32 num,
}

service format_data {   # 对应服务的类，生成对应文件，服务端和客户端对应处理接口
    Data do_format(1:Data data),
}

service HelloWorld {
    string ping(),
    string say(1:string msg)
}
