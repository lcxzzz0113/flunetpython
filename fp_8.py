'''
@Date: 2020-08-03 21:17:16
@Author: lcx

@Description: 
'''
# 变量特性:将变量的分配给对象,变量是标签
class Gizon:
    def __init__(self):
        print('Gimzo id: %d' % id(self))

x = Gizon()
print(dir())

# 对象身上多个标签,就是别名
list1 = [1, 2 ,3]
list2 = list1
print(list1 is list2)

# x is None

# str, bytes, array.array 序列是扁平, 它们保存的不是引用, 而是在连续内存保存数据的本身

# list(a1) or a2 = a1[:] 创建副本:浅复制 副本的元素是源容器中的元素中引用
l1 = [2, [3, 4, 5], (3, 4, 45)]
l2 = list(l1)
l3 = l1[:]

# copy浅复制, deepcopy是深复制
# 当默认实参是[],然后再定义引用,会去改变默认形参,所以一般默认实参都是None
def __init__(self, a = None):
    if a is None:
        self.a = []
    else:
        self.a = list(a)

# del 垃圾回收
import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye) # 对象注销时调用
del s1
print(ender.alive)
s2 = 'sss'
print(ender.alive)

# 弱引用
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
a_set = {2, 3, 4}
print('weakref')
print(wref())
print(wref() is None)
count = 0
print(wref() is None)


# tuple创建的是同一个
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 is t2)

# 驻留性质，比较字符串和整数是否相等用 == 