'''
@Date: 2020-08-04 14:28:07
@Author: lcx

@Description: 
'''

# 不要子类化dict, 去子类化UserDict

# 多重继承
class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

if __name__ == "__main__":
    # 通过__mro__属性判断继承顺序
    print(D.__mro__)
    d = D()
    d.pingpong()
    d.ping()
    d.pong()