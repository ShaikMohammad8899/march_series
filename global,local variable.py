#Variables inside and outside the function is called global and local variables
'''A variable define above the function and is accessible to the entire global
space is called gobal variable'''
'''A variable inside the function is called local variable'''

#1.first case of global variables


'''a=3
def check():
    print("inside value is:",a)
check()
print("oytside value is:",a)'''


#2.second case of global variable


'''a=4
def check1():
    a=5
    a=a**2
    print("inside value is:",a)
    a=5
    print("inside value is:",a)
check1()
print("outside value is:",a)'''


#3.third case of both global and local variables


'''a=3
def check():
    a=12
    print("inside value is:",a)
    a=5
    print("updated value is:",a+10)
    b=15
    b=b+a
    print("value of b is:",b)
check()
print("a value is:",a)
print("b value is:",b)

'''

#4.usage of global keyword

a=3
def final():
    global a,b
    print("inside value is:",a)
    a=5
    print("updated value is:",a+10)
    b=15
    b=b+a
    print("value of b is:",b)
final()
print("a value is:",a)
print("b value is:",b)


##Usage Of Global Keyword:
'''when user wants to access the global variable inside the function directly and
carry forword the updated value even outside the function then we need to use global key word''' 






    
    
