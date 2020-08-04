'''
@Date: 2020-08-03 21:02:39
@Author: lcx

@Description: 
'''

# iter(x) 背后是x.__iter__() -->getitem()

# str类型 a[4:5] = a[4] ；list类型的 b[4:5]是list，b[4]是元素

# *表示剩下的元素
a, b, *rest = range(5)


# slice切片函数的使用

# ord返回字符的ASCII码
s = 'sdfggvadfg'
print(ord('A'))
ss = list(filter(lambda c: c > 70, map(ord, s)))
print(ss)

# ('%s %s' % (a, b))
print('{} {}'.format('helo', 'world'))
print('{:.2f}'.format(3.142233))

l = [1, 2, 3]
print(l * 5)

board = [['_'] * 3 for i in range(3)] # [['_'] * 3] * 3

# sort and sorted(copy)
students = [('aaa', 'A', 23), ('awe', 'B', 12), ('asd', 'C', 53)]
print(sorted(students, key=lambda student: student[0]))

list1 = [('d', 2), ('a', 5), ('d', 2), ('c', 3), ('d', 2)]
print(sorted(list1, key=lambda x: (x[1], x[0]))) # 先按第二个元素排序

# bisect
print('bisert...')
from bisect import bisect_left, bisect_right, insort_left, insort_right
a = [1, 2, 3, 5, 6, 8 ,12]
# bisect_left返回x的最左边, bisect_right返回是x的最右边
print(bisect_left(a, 3))
print(bisect_right(a, 3))
print(bisect_left(a, 4))
print(bisect_right(a, 4))

print(insort_left(a, 4))
print(insort_right(a, 5))

# list方法: append, clear, copy, count, extend, index, insert(p, e), pop(删除并返回), remove(删除第一次出现的这个值), reverse(), sort()

# deque
from collections import deque

d = deque([1, 2, 3, 4])
d.rotate(1) # 顺指针旋转 [4, 1, 2, 3]
d.rotate(-1) # 逆时针旋转

d.appendleft(1)
d.extendleft([1, 2, 3])
d.popleft()
print(d)

# queue : push, get, full, empty
from queue import Queue, LifoQueue, PriorityQueue
q = Queue(maxsize=5) #先进先出
lq = LifoQueue(maxsize=6) #后进先出
pq = PriorityQueue(maxsize=5) #优先级队列

# 生成者消费模式 : 生产者和消费者之间设置缓冲区

import time,threading
q=Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        q.put('气球兵{}'.format(count))
        print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(5)
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done() # 完成工作发出一个信号
t1=threading.Thread(target=product,args=('wpp',))
t2=threading.Thread(target=consume,args=('ypp',))
t3=threading.Thread(target=consume,args=('others',))
 
t1.start()
t2.start()
t3.start()

# multiprocess 

# process
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))

p = Process(target=run_proc, args=('test', ))
p.start()
p.join()

# pool
from multiprocessing import Pool
import os, time, random

p = Pool()
for i in range(5):
    p.apply_async(run_proc, args=(i, ))

# 多进程通信
# Process 版本
import multiprocessing
from multiprocessing import Process, Queue,  Pool
import os, time, random

def write(q, lock):
    lock.acquire() #加锁
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' %value)
        q.put(value)
    lock.release() #释放锁

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue...' %value) 
            time.sleep(random.random())
        else:
            break

if __name__ == "__main__":
    # q = Queue()
    # pw = Process(target=write, args=(q, ))
    # pr = Process(target=read, args=(q, ))
    # pw.start()
    # pw.join()
    # pr.start()
    # pr.join()
    # print('End')


    # 用Manager实现pool进程间通信
    manager = multiprocessing.Manager()
    q = manager.Queue()
    lock = manager.Lock() #初始化一把锁
    p = Pool()
    pw = p.apply_async(write, args=(q, lock))
    time.sleep(4)
    pr = p.apply_async(read, args=(q, ))
    p.close()
    p.join()
    print('End')


# heapq : heapify, heappush, heapop(弹出最小的), heapreplace(弹出最小的,并将x压入)
import heapq

# 建立小顶锥
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)

# 建立大顶锥
a = list(map(lambda x : -x, a))
heapq.heapify(a)
print([-x for x in a])

print(heapq.nlargest(3, li1)) #前n个最小的