#! --*-- coding: utf-8 --*--
__author__ = 'yanyunfei'


class RMM(object):
    """
    逆向最大匹配算法
    """

    def __init__(self, dict_file):
        """
        :param dict_file: 分词词典文件路径
        """
        self.max_len = 0    # 词典中最长词条的长度
        self.dict = set()   # 存储字段到内存，并去重

        with open(dict_file) as f:
            for word in f:
                word = word.strip().decode('utf-8')
                if not word:
                    continue
                self.dict.add(word)
                word_len = len(word)
                if word_len > self.max_len:
                    self.max_len = word_len

    def cut(self, text):
        """
        分词算法
        :param text: 需要分的词
        :return:
        """
        result = []

        index = len(text)
        while index > 0:
            word = None
            for size in range(self.max_len, 0, -1):
                if size > index:
                    continue

                t = text[index - size:index]

                if t in self.dict:
                    result.append(t)
                    word = t
                    break

            if word is None:
                word = text[index-1:index]
                result.append(word)

            index -= len(word)

        return result[::-1]


class MM(object):
    """
    正向最大匹配
    """

    def __init__(self, dict_path):
        """

        :param dict_path: 分词字典文件路径
        """
        self.max_len = 0
        self.dict = set()

        with open(dict_path) as f:
            for word in f:
                word = word.strip().decode('utf-8')
                if not word:
                    continue
                self.dict.add(word)
                if len(word) > self.max_len:
                    self.max_len = len(word)

    def cut(self, text):
        """
        分词算法
        :param text:
        :return:
        """
        result = []

        text_len = len(text)
        index = 0

        while index < text_len:
            word = None
            for size in range(self.max_len, 0, -1):
                if size > text_len-index:
                    continue

                pice = text[index:index+size]

                if pice in self.dict:
                    result.append(pice)
                    index += size
                    word = pice
                    break

            if not word:
                result.append(text[index])
                index += 1

        return result


def main():
    rmm = RMM('./data/cut_dict.utf8')
    cut_result = rmm.cut(u'南京市长江大桥')
    print '逆向最大分词结果：', ','.join(cut_result)

    mm = MM('./data/cut_dict.utf8')
    cut_result = mm.cut(u'南京市长江大桥')
    print '正向最大分词结果：', ','.join(cut_result)

if __name__ == '__main__':
    main()