import socket
from concurrent import futures
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import asyncio
import time
from time import ctime

import qrcode


# def tsfunc(func):
#     def wrappedFunc(*args, **kwargs):
#         start = time.clock()
#         action = func(*args, **kwargs)
#         time_delta = time.clock() - start
#         print('[{0}] {1}() called, time delta: {2}'.format(
#             ctime(), func.__name__, time_delta))
#         return action
#     return wrappedFunc


# def blocking_way():
#     sock = socket.socket()
#     sock.connect(('www.sina.com', 80))
#     request = 'GET / HTTP/1.0\r\nHOST:www.sina.com\r\n\r\n'
#     sock.send(request.encode('ascii'))
#     response = b''
#     chunk = sock.recv(4096)
#     while chunk:
#         response += chunk
#         chunk = sock.recv(4096)
#     return response


# @tsfunc
# def sync_way():
#     res = []
#     for i in range(10):
#         res.append(blocking_way())
#     return len(res)


# @tsfunc
# def process_way():
#     worker = 10
#     with futures.ProcessPoolExecutor(worker) as executor:
#         futs = {executor.submit(blocking_way) for i in range(10)}
#     return len([fut.result() for fut in futs])


# @tsfunc
# def thread_way():
#     worker = 10
#     with futures.ThreadPoolExecutor(worker) as executor:
#         futs = {executor.submit(blocking_way) for i in range(10)}
#     return len([fut.result() for fut in futs])

# sync_way()
# process_way()
# thread_way()

# img = qrcode.make('hello xiaojianzi')
# with open('test.png', 'wb') as f:
#     img.save(f)


# class Fool(object):
#     def test(self):
#         print('object')

#     @classmethod
#     def test2(cls, clss):
#         print('clss')

#     @staticmethod
#     def test3():
#         print('static')
# ff = Fool()
# ff.test()
# Fool.test2(ff)
# Fool.test3()


# class Person(object):
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def speak():
#         print('%s is speaking chinese.' % 'anyone')


# p = Person('bigberg')
# p.speak(p)
# Person.speak()


# class A(object):
#     def go(self):
#         print("go A go!")

#     def stop(self):
#         print("stop A stop!")

#     def pause(self):
#         raise Exception("Not Implemented")


# class B(A):
#     def go(self):
#         super(B, self).go()
#         print("go B go!")


# class C(A):
#     def go(self):
#         super(C, self).go()
#         print("go C go!")

#     def stop(self):
#         super(C, self).stop()
#         print("stop C stop!")


# class D(B, C):
#     def go(self):
#         super(D, self).go()
#         print("go D go!")

#     def stop(self):
#         super(D, self).stop()
#         print("stop D stop!")

#     def pause(self):
#         print("wait D wait!")


# class E(B, C):
#     pass


# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
# # 说明下列代码的输出结果
# a.go()
# # go A go
# b.go()
# # go A go
# # go B go
# c.go()
# # go A go
# # go C go
# d.go()
# # go A go
# # go B go
# # go C go
# # go D go
# e.go()

# a.stop()
# # stop A stop
# b.stop()
# # stop A stop
# c.stop()
# # stop A stop
# # stop C stop
# d.stop()
# # stop A stop
# # stop B stop
# # stop C stop
# # stop D stop
# e.stop()
# a.pause()
# # Not Implement
# b.pause()
# # Not Implement
# c.pause()
# # Not Implement
# d.pause()
# # Not Implement
# e.pause()


profitability_measures_a = [
    {"item": "营业收入", "this": '', "last": '', "change_pct": ''},
    {"item": "毛利率%", "this": '', "last": '', "change_pct": '-'},
    {"item": "归属于挂牌公司股东的净利润", "this": '', "last": '', "change_pct": ''},
    {"item": "归属于挂牌公司股东的扣除非经常性损益后的净利润",
     "this": '', "last": '', "change_pct": ''},
    {"item": "加权平均净资产收益率%（依据归属于挂牌公司股东的净利润计算）",
     "this": '', "last": '', "change_pct": '-'},
    {"item": "加权平均净资产收益率（归属于挂牌公司股东的扣除非经常性损益后的净利润计算）",
     "this": '', "last": '', "change_pct": '-'},
    {"item": "基本每股收益", "this": '', "last": '', "change_pct": ''},
]

# 一、盈利能力
profitability_measures_b = [
    {"item": "营业收dd入", "this": 'asdfad', "last": '', "change_pct": ''},
    {"item": "毛利率%", "this": '12312', "last": '', "change_pct": '-'},
    {"item": "归属于挂牌公司股东的净利润", "this": '', "last": '', "change_pct": ''},
    {"item": "归属于挂牌公司股东的扣除非经常性损益后的净利润",
     "this": '123123', "last": '', "change_pct": ''},
    {"item": "加权平均净资产收益率%（依据归属于挂牌公司股东的净利润计算）",
     "this": '123', "last": '', "change_pct": '-'},
    {"item": "加权平均净资产收益率（归属于挂牌公司股东的扣除非经常性损益后的净利润计算）",
     "this": '', "last": '123123', "change_pct": '-'},
    {"item": "基本每股收益", "this": '', "last": '', "change_pct": ''},
]


# if len(profitability_measures_a) == len(profitability_measures_b):
#     lt = []
#     for i in range(len(profitability_measures_a)):
#         if profitability_measures_a[i]['item'] == profitability_measures_b[i]['item']:
#             print('ok')
#         else:
           
#         if profitability_measures_a[i]['this'] == profitability_measures_b[i]['this']:
#             print('ok')
#         if profitability_measures_a[i]['last'] == profitability_measures_b[i]['last']:
#             print('ok')
#         if profitability_measures_a[i]['change_pct'] == profitability_measures_b[i]['change_pct']:
#             print('ok')

# else:
#     pass
import numpy as np
class My_COntainer():
    data = np.random.randn(3, 2)