# -*- coding: UTF-8 -*-
def say_hello():
    print ("hello!")

def say_goodbye():
    '''good'''
    print("bye!")

def debug(func):
    def wrapper():
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper
def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"



# 输出：
# <b class='bold_css'><i class='italic_css'>hello world</i></b>
if __name__== '__main__':
    # say_goodbye()
    # say_hello()
   # say_hello= debug(say_hello())
   print(hello())