'''
@Date: 2020-08-03 15:52:14
@Author: lcx

@Description: 
'''
# 单例模式

func1_txt = """
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, )
        return cls._instance

class MyClass(Singleton):
    a = 1
    def __init__(self, name):
        self.name = name

one = MyClass('egon')
two = MyClass('alex')

print(id(one))
print(id(two))
print(one == two)
print(one is two)
"""
exec(func1_txt)

# 策略模式 : 不同的算法做同一个事情
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customr', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() -discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# 可以采用@abstractmethod抽象基类,然后具体折扣继承基类来实现,但是代码太冗余

# 装饰器版本
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promos(order):
    return max(promo(order) for promo in promos)


# 命令模式 : 将调用者和接受者解耦,不同的命令做不同的事
