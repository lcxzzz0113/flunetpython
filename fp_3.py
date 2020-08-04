'''
@Date: 2020-08-04 13:32:59
@Author: lcx

@Description: 
'''

# defaultdict
from collections import defaultdict
ldict = defaultdict(list)


# dict
from collections import Counter
a = Counter('addffghfgaa')
print(a)
a.update('eedffgfss ')
print(a)

# easydict
from easydict import EasyDict as edict
b = edict()
b.name = 'lcx'
b.age = 12
print(b)


# 间接修改键值
dict ={'a': 1, 'b' : 2}
dict['c'] = dict.pop('a')   #pop返回这个键的值,删除这个键

# set 统计一个集合的元素在另一个出现次数
set1 = {1, 3, 45, 67}
set2 = {3, 67, 234}
print(len(set1 & set2)) 


# 集合 &, |, -, ^
# pop()都是会返回值,这相当于c++ top() and pop(); remove(), add(set特有的),


"""
dict 和 set背后:查找元素特别快,散列表其实是稀疏列表。散列表的单元是表元（键引用,值引用）;因为所有的表元大小一致；
所以可以通过偏移量来读取表元;python 会让1/3的表元是空的,将对象放入散列表时，先计算该元素键的散列值(hash);
通过这个值最低几位的数字当做偏移量，在散列表里查找表元，对查找取key进行匹配，不匹配则换数字进行查找；
需要有两个函数, __hash__, __eq__来检测hash值的相等性；用__slots__将实例属性的存储由dict改成tuple；
set的元素都是散列的，集合很消耗内存,元素的次序取决于添加的次序，往集合里添加元素会改变已有元素的次序;
(越是相似但是不相等的对象,它们的散列值尽可能的大)
"""