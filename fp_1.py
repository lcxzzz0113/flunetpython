'''
@Date: 2020-08-03 20:39:34
@Author: lcx

@Description: 
'''

from collections import namedtuple
from random import choice


# namedtuple
User = namedtuple('User', 'name sex age')
user1 = User(name='lcx', sex='male', age=21)
user2 = User._make(['lcx', 'male', 21])
print(user2)

user2 = user2._replace(age=23)
print(user2._asdict())  # namedtuple转dict

# __repr__ , __str__(str())