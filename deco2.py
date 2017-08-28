# -*- coding: UTF-8 -*-
def makeHtmlTag(tag,*args,**kwds):
    def real_decorator(fn):
        css_class= " class='{0}'".format(kwds["css_class"])\
                                    if "css_class" in kwds else ""

        def wrapped(*args,**kwds):
            return "<" + tag+css_class+">"+fn(*args,**kwds)+ "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag="b",css_class="bold_css")
@makeHtmlTag(tag="a")
def hello():
    return "hello world"

class myDecorator(object):
    def __init__(self,fn):
        print ("inside myDecorator.__init__()")
        self.fn=fn
    def __call__(self, *args, **kwargs):
        self.fn()
        print("inside myDecorator.__call__")

@myDecorator
def aFunction():
    print("inside aFunction()")

class makeHtmlTagClass(object):
    def __init__(self,tag,css_class):
        self._tag= tag
        self._css_class=" class='{0}'".format(css_class)\
                                        if css_class !="" else ""
    def __call__(self,fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class+">"  \
                       + fn(*args, **kwargs) + "</" + self._tag + ">"
        return wrapped
@makeHtmlTagClass(tag="b",css_class="bold_css")
@makeHtmlTagClass(tag="a",css_class="italic_css")
def hello(name):
    return "hello,{}".format(name)


def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function

@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args +(str,)
        return function(*args, **kwargs)
    return wrap_function

class Printer:
    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function

@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

def decorate_B(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        return function(str, *args, **kwargs)
    return wrap_function

@decorate_B
def print_message_B(str, *args, **kwargs):
    print(str)

from functools import wraps
def hello(fn):
    @wraps(fn)
    def wrapper():
        print ("hello, %s" % fn.__name__)
        fn()
        print ("goodby, %s" % fn.__name__)
    return wrapper

@hello
def foo():
    '''foo help doc'''
    print ("i am foo")
    pass

class SomeClass(object):
    @wraps_decorator
    def method(self, x, y):
        pass

obj = SomeClass()
for name, func in getmembers(obj, predicate=inspect.ismethod):
    print "Member Name: %s" % name
    print "Func Name: %s" % func.func_name
    print "Args: %s" % getargspec(func)[0]