from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)  #将Vector分量保存在一个数组中

    def __iter__(self):
        # return (i for i in (self, self.y))
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self.components[pos]
        msg = '{.__name__!r} object has no attibute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {atrr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value) # 动态访问超类的

    def __hash__(self):
        hashes = (hash(x) for x in self._components)  # 创建一个生成器表达式,惰性计算每个分量的散列值
        hashes1 = map(hash, self._components) # py3，map是惰性的，它会创建一个生成器
        return functools.reduce(operator.xor, hash, 0)


    def __eq__(self, other):
        # if len(self) != len(self):
        #     return False
        # 使用for循环迭代元素,不用处理索引,zip并行迭代多个可迭代对象
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True
        
        # 将for循环换成all
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))


    def __repr__(self):
        components = reprlib.repr(self._components)  #来获取有限长度表示形式
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # ord函数是显示字符的ascii码
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __abs__(self):
        # 计算平方根
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets): # 从字节转换为Vector2d实例
        typecode = chr(octets[0]) #与ord相反，是返回整数对应ascii字符
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self), self.angles()])  # chain迭代返回数,如果用a+b则消耗内存
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))
        


    