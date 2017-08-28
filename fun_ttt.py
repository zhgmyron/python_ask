# -*- coding: UTF-8 -*-
import time
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-03-25')


def foo():
    print 'in foo()'
def timeit(func):
    def wrapper(*args,**kw):
        start = time.clock()
        func()
        end = time.clock()
        print('used:',end- start)
    return wrapper
foo= timeit(foo)
foo()
