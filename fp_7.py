'''
@Date: 2020-08-03 22:13:59
@Author: lcx

@Description: 
'''

# 装饰器, 重复函数使用
import time

def time_calc(func):
    print('running register(%s)' % func) # python加载模块就会执行
    def warpper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        exec_time = time.time() - start_time
        print('{}函数, 花费的时间是: {}'.format(str(func), exec_time))

    return warpper

@time_calc
def add(a, b):
    print(1111)
    return a + b 

add(1, 3)


# dis.dis查看字节码
from dis import dis
print(dis(add))

# 闭包: 保留定义函数存在自由变量的绑定，这样调用函数虽定义域不可用了，但是仍能使用那些绑定
# 自由变量: 未在本地作用域中绑定的变量
def make_average():
    series = []
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average


# nonlocal 将变量声明为自由变量
# 对于不可变类型(元组，数字): a += 1 等价于 a = a + 1, 在函数类会使之成为一个局部变量
# list append不会存在这样问题

def make_average1():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += 1
        total += new_value
        return total / count
    return averager

# 装饰器例子
import time 
import functools

def clock(func): 
    @functools.wraps(func) # 使用functools.wraps将装饰器的相关属性从func复制到clock
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

# 标准库中装饰器
functools.lru_cache #备忘录 

# 叠加式装饰器,最靠近先应用


# 参数化装饰器(装饰器工厂函数)
import time
DEFAULT_FMT = '[{elapsed : 0.8f}s] {name}({args}) -> {result}'

def clock1(fmt = DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _results = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_results)
            print(fmt.format(**locals())) #local()返回是dict
            return _results
        return clocked
    return decorate 

@clock1('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(0.123)


