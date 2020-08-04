'''
@Date: 2020-04-07 10:54:07
@Author: lcx

@Description: 
'''
from array import array
import math


class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        # 一个下划线, 把属性标记为私有的, 还有一点就是让向量(key)不可改
        self._x = float(x)
        self._y = float(y)

    @property #把读值方法标记为特性
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    def __iter__(self):
        # return (i for i in (self, self.y))
        yield self.x, self.y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # ord函数是显示字符的ascii码
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    # 没有解决Vector(3, 4) == [3, 4]的问题
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 计算平方根
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets): # 从字节转换为Vector2d实例
        typecode = chr(octets[0]) #与ord相反，是返回整数对应ascii字符
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            out_fmt = '<{}, {}>'
        else:
            coords = self
            out_fmt = '({}, {})'

        components = (format(c, fmt_spec) for c in self)
        return out_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        retrun hash(self.x) ^ hash(self.y)




# __slot__ 方法的优势
# import importlib
# import sys 
# import resource

# NUM_VECTOR = 10 ** 7

# if len(sys.argv) == 2:
#     module_name = sys.argv[1].replace('.py', '') # replace
#     module = importlib.import_module(module_name)
# else:
#     print('Usage: {} <vector-module-to-test>'.format())
#     sys.exit(1)

# mem = resource.getrusage(resource.RUSAGE_SELF)
# mem1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
