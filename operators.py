Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Arthematic operators
a=4
b=6
a
4
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a**b)
4096
print(a%b)
4
b
6
a
4


#assignment operators
a=2
b=4
b+=a
b
6
b*=a
b
12
b-=a
b
10
b//=a
b
5
b/=a
b
2.5
b**=a
b
6.25
b5=a
b%=a
b
0.25
a
2


#comparison operators
a=8
b=15
a<b
True
a>b
False
b<a
False
b>a
True
a<=b
True
a>=b
False
b<=a
False
b>=a
True
b!=a
True
a!=b
True
a==b
False
b==a
False


#logical operators
a=9
b=19
a<=b and b>=a
True
a<b and b>a
True
a!=b
True
a!=b and a==b
False
a<b or b>a
True
a,+b or b>=a
(9, 19)
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True


#identify operators
a=3
if type(a) id int:
    
SyntaxError: invalid syntax
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is float:
    print("it is float")

    
if type(a) is not float:
    print("it is int")

    
it is int


#membership operators
a=2,3,4,5,6,7,8,9
if 8 in a:
    print("true")

    
true
if 10 not in a:
    print(10)

    
10
if 11 not in a:
    print("true")

    
true


#bitwise operator
a=5
b=7
a&b
5
bin(a)
'0b101'
bin(b)
'0b111'
>>> a=3
>>> b=7
>>> a%b
3
>>> bin(a)
'0b11'
>>> bin(b)
'0b111'
>>> a=7
>>> b=9
>>> c=5
>>> a&b&c
1
>>> bin(a)
'0b111'
>>> bin(b)
'0b1001'
>>> bin(c)
'0b101'
>>> 
>>> 
>>> #OR
>>> a=3
>>> b=5
>>> a|b
7
>>> a=8
>>> b=11
>>> a|b
11
>>> 
>>> 
>>> #XOR
>>> a=9
>>> b=7
>>> a^b
14
