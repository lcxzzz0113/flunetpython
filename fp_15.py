'''
@Date: 2020-08-04 15:56:11
@Author: lcx

@Description: 
'''

# for if else ; else:运行这个成功之后才会做这个事情
# try except else;

# 上下文管理 __enter__, __exit__

# contextmanager
import contextlib

@contextlib.contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
            print('Error!')
    finally:
        print('close')
        f_obj.close()
with file_open('1.txt') as fd:
    fd.write('contextmanager is good!')

# 原地重写
import csv
with inplace('1.csv', 'r', newline='') as(infh, outfh):
    reader = csv.reader(infh)
    writer = csv.reader(outfh)
    for row in reader:
        row += ['new', 'columns']
        writer.writerow(row)
