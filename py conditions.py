#conditions in python

#if condition using comparison operator
'''a=2
b=5
if a<b:
    print("true")
'''
'''
a=2
b=5
if a>b:
    print("true")
'''
'''a=20
b=25
if a<=b:
    print("true")
'''
'''
a=12
b=15
if a>=b:
    print("false")
'''
'''a=17
b=15
if a>=b:
    print("true")
'''

'''a=12
b=15
if a!=b:
    print("not equal")'''

'''
a=50
b=50
if a==b:
    print("equal")'''

'''a=20
b=15
if a>=b:
    print("a is greater")'''

#run time
'''a=int(input("A value:"))
b=int(input("B value:"))
if a<b:
    print("lesser")'''

'''a=int(input("A value:"))
if a>20:
    print("greater")'''

'''a="python"
if a=="python":
    print("correct")'''

'''a=input("Data:")
if a=="python":
    print("true")'''

'''a="python"
b="java"
if a!=b:
    print("true")'''

'''a="python"
b="python"
if a==b:
    print("true")'''


#if - conditions using logical operators
# and, or, not
'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=3
b=6
if a<=b and b>=a:
    print("true")'''
    
'''a=3
b=6
if a!=b and b==a:
    print("true")'''
    
'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if a!=b or b==a:
    print("true")'''


'''a=3
b=6
if not a!=b or b>a:
    print("true")'''

'''a=3
b=6
if a<b or b<a:
    print("true")'''

'''a=3
b=6
if a<=b or b>=a:
    print("true")'''

'''a=int(input("A value:"))
b=int(input("B value:"))
if a<b and b>a:
    print("true")'''

'''a=str(input("data 1:"))
b=str(input("data 2:"))
if a==b and b==a:
    print("true")'''

'''a=str(input("data 1:"))
b=str(input("data 2:"))
if not a!=b or b==a:
    print("true")'''

'''a=str(input("data A:"))
b=str(input("data B:"))
if a!=b and b!=a:
    print("true")'''

'''a=str(input("data A:"))
b=str(input("data B:"))
if not a==b and b!=a:
    print("true")'''


#if - condition by using identify opeators
#is, is not

'''a=5
if type(a) is int:
    print("it is int")'''

'''a=6
if type(a) is not int:
    print("it is int")'''


'''a=6.85
if type(a) is not int:
    print("it is int")'''

'''a=6.85
if type(a) is float:
    print("it is float")'''

'''a=6.85
if type(a) is not float:
    print("it is int")'''

'''a=input("data")
if type(a) is str:
    print("it is string")'''

'''a=input("data")
if type(a) is not str:
    print("it is string")'''

'''a=3+4j
if type(a) is complex:
    print("it is complex")'''

'''a=True
if type(a) is bool:
    print("it is boolean")'''

'''a=False
if type(a) is not bool:
    print("it is boolean")'''

#if - condition using membership opearator
#in, not in

'''a=[2,3,4,5,6,7,8,9]
if 8 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9]
if 8 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9]
if 1 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9]
b=int(input("value:"))
if b in a:
    print("true")'''

#if-else conditions using comparison operators
'''a=5
b=10
if a<b:
    print("true")
else:
    print("false")'''

'''
a=5
b=10
if a>=b:
    print("true")
else:
    print("false")'''

'''a=5
b=10
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=10
if a<b and b<a:
    print("true")
else:
    print("false")'''

'''a=5
b=10
if a<b or b<a:
    print("true")
else:
    print("false")'''

'''a=5
b=10
if a>b and b<a:
    print("true")
else:
    print("false")'''

'''a=5
b=10
if not a<b and b>a:
    print("true")
else:
    print("false")'''


'''a=5
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=5
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7,8,9
if 7 in a:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7,8,9
if 7 not in a:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7,8,9
if 10 not in a:
    print("true")
else:
    print("false")'''

#if-elif
'''a=4
b=9
if a!=b:
    print("not equal")
elif a<b:
    print("less")'''

'''a=4
b=9
if a==b:
    print("not equal")
elif a<=b:
    print("less")'''

'''a=4
b=9
if a>b and b>a:
    print("not equal")
elif a<b and b>a:
    print("true")
else:
    print("False")'''

'''a=4
b=9
if a>b or b<a:
    print("not equal")
elif a<b or b<a:
    print("true")
else:
    print("False")'''

'''a=4
b=9
if not a<b and b>a:
    print("not equal")
elif not a>b or b<a:
    print("true")
else:
    print("False")'''

'''a=4.5
if type(a) is int:
    print("true")
elif type(a) is float:
    print("true float")
else:
    print("False")'''

'''
a=4
if type(a) is not int:
    print("true")
elif type(a) is not float:
    print("true int")
else:
    print("False")
'''

'''a=2,3,4,5,6,7,8,9,4.5,6.8
if 8 in a:
    print("true")
elif 6.8 in a:
    print("true float")
else:
    print("False")
'''
'''
a=2,3,4,5,6,7,8,9,4.5,6.8
if 10 in a:
    print("true")
elif 6.8 in a:
    print("true float")
else:
    print("False")
'''

'''a=2,3,4,5,6,7,8,9,4.5,6.8
if 8 not in a:
    print("true")
elif 6.8 not in a:
    print("true float")
elif 6 in a:
    print("true int")
else:
    print("False")'''

#if-elif-else conditions

'''a=10
b=20
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

''''a=10
b=20
if a>b:
    print("less")
elif b==a:
    print("greater")
else:
    print("true")
'''

'''a=4
b=9
if not a<b and b>a:
    print("not equal")
elif a>b or b<a:
    print("true")
else:
    print("False")'''

'''a=4
if type(a) is not int:
    print("true")
elif type(a) is complex:
    print("true int")
else:
    print("False")'''

'''a=2,3,4,5,6,7,8,9,4.5,6.8
if 8 not in a:
    print("true")
elif 6.8 not in a:
    print("true float")
elif 10 in a:
    print("true int")
else:
    print("False")'''

'''a=9
b=12
if a<=b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''


#multiple if
'''a=9
b=12
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

a=4
b=9
if  a<b and b>a:
    print("not equal")
if a<b or b<a:
    print("true")
if not a==b:
    print("False")






















