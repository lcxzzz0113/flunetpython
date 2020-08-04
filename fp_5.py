'''
@Date: 2020-08-04 12:17:11
@Author: lcx

@Description: 
'''

# python中函数是一等对象
# 一等对象定义: 1.在运行时创建 2.可以赋值给变量的元素 3.能作为参数传给函数 4.可以作为函数返回的结果
# 高阶函数: 接受函数为参数 or 把函数作为返回的结果

from functools import reduce
from operator import add

print(reduce(add, range(100)))

# 可调用对象: 1.def 2. 内置函数 3. 内置方法 4.方法 5.类 6.类的实例 7.生成器函数

# 定位参数到仅限关键字
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) \
            for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % \
            (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

# functools.paritial
from operator import mul
from functools import partial

triple = partial(mul, 3)
triple(7)