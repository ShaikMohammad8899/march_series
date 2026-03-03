Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatypes
a=4
type(a)
<class 'int'>
b=0.9
type(b)
<class 'float'>
>>> c='coder'
>>> print(c)
coder
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''full stack'''
>>> type(e)
<class 'str'>
>>> f='p'
>>> type(f)
<class 'str'>
>>> d=4j+9
>>> type(d)
<class 'complex'>
>>> e=9+8j
>>> type(e)
<class 'complex'>
>>> f=10j
>>> type(f)
<class 'complex'>
>>> 2+7i
SyntaxError: invalid decimal literal
>>> h=True
>>> type(h)
<class 'bool'>
>>> i-False
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    i-False
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> i=False
>>> type(i)
<class 'bool'>
