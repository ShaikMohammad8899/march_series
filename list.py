Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]
a=[3,5.6,"python",True,False]
print(a)
[3, 5.6, 'python', True, False]
type()a
SyntaxError: invalid syntax
type(a)
<class 'list'>
b=9
type(a)
<class 'list'>
b=[9]
type(b)
<class 'list'>

a=["python","DS","ml","ai"]
a.append("c")
a
['python', 'DS', 'ml', 'ai', 'c']
a.append(["c++","java"])
a
['python', 'DS', 'ml', 'ai', 'c', ['c++', 'java']]

a["html","css"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a["html","css"]
TypeError: list indices must be integers or slices, not tuple
a=["html","css"]
a.extend(["python","java"])
a
['html', 'css', 'python', 'java']
a.insert(1,"ds")
a
['html', 'ds', 'css', 'python', 'java']
a.insert(4,"c")
a
['html', 'ds', 'css', 'python', 'c', 'java']


a=["apple","banana","grapes","mango"]
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes', 'mango']
b=a.copy()
b
['apple', 'banana', 'grapes', 'mango']
a.clear()
a
[]
b=[]
b.append("c")
b
['c']
b.extend(["hi","hello"])
b
['c', 'hi', 'hello']


#pop (to delete a particular element)
a=["hi","hello","how","are","you"]
a.pop()
'you'
a
['hi', 'hello', 'how', 'are']
a.pop(3)
'are'
a
['hi', 'hello', 'how']

#sort
a=["ai","java","c","ml","ds"]
a.sort()
a
['ai', 'c', 'ds', 'java', 'ml']
b=[6,98,34,8,23,9,4,9,0,1]
b.sort()
>>> b
[0, 1, 4, 6, 8, 9, 9, 23, 34, 98]
>>> 
>>> 
>>> #reverse
>>> a=["white","black","red","blue"]
>>> a.reverse()
>>> a
['blue', 'red', 'black', 'white']
>>> b=[3,4,5,6,7,098,5,235,44]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> b=[3,4,5,6,7,98,5,35,44]
>>> b.reverse()
>>> b
[44, 35, 5, 98, 7, 6, 5, 4, 3]
>>> 
>>> 
>>> #remove
>>> a=["html","css","js"]
>>> a.remove("js")
>>> a
['html', 'css']
>>> 
>>> #len()
>>> a=["mango","kiwi","dragon"]
>>> len(a)
3
>>> b="mango"
>>> len(b)
5
>>> c=["mango"]
>>> len(c)
1
>>> c.count("mango")
1
>>> b.count("mango")
1
