struct Person {
    1: string name,
    2: string address
}

struct Email {
    1: string subject = 'Subject',
    2: string content,
    3: Person sender,
    4: required Person recver,
}

const Email email = {'subject': 'Hello', 'content': 'Long time no see',
    'sender': {'name': 'jack', 'address': 'jack@gmail.com'},
    'recver': {'name': 'chao', 'address': 'chao@gmail.com'}
}
