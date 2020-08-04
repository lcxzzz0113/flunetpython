'''
@Date: 2020-08-04 15:24:27
@Author: lcx

@Description: 
'''


# 可迭代对象: __iter__ or __getitem__
# 迭代器 : __next__, 调用iter获取, next获取下一个

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return 


# 理解生成器
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():
    print('-->', c)