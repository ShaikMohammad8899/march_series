'''functions:
1.A function is a block of organized,reusable code and that is used to perform
  a single or multiple tasks
2.Python gives inbuilt functions like print or you can make your own functions also
  and these as=re called user defined functions
3.Function block begin with the keyword "def" followed by name and paranthesis(())'''

#normal code

'''a=10
b=20
print("the sum is:",a+b)
print("the difference is:",a-b)
print("the product is:0",a*b)
'''

#functiona code

'''def cal(a,b):
    print("the sum is:",a+b)
    print("the difference is:",a-b)
    print("the product is:",a*b)
cal(10,20)
cal(20,30)
cal(300,400)'''

'''def cal(a,b):
    print("the integer division is:",a//b)
    print("the modulas is:",a%b)
    print("the power A is:",a**a)
    print("the power B is:",b**b)
cal(10,20)
cal(20,30)
cal(34,44)'''

'''
def add():
    a=int(input("enter A value:"))
    b=int(input("enter B value:"))
    print(a+b)
add()'''


'''while True:
def full_name():
    a=input("first name:")
    b=input("last name:")
    print((a+" "+b).title())
full_name()'''

#print vs return:
'''1.print just shows the human user ouput in a console
1.return is used to terminate the function and give back a value from the function'''


'''def mul(a,b):
    print(a*b)
mul(4,5)'''


'''def mul(a,b):
    return a*b
print(mul(6,3))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,8)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
    #return(c)
    #return(d)
    #return(e)
print(cal(8,7))'''


'''def split():
    a=int(input("no.of friends:"))
    b=int(input("split amount:"))
    return(b/a)
print(split())'''

'''def split():
    a=int(input("no.of friends:"))
    b=int(input("split amount:"))
    return(b//a)
print(split())'''

'''def split():
    a=int(input("no.of friends:"))
    b=int(input("split amount:"))
    #return('perhead bill is :{}'.format(b//a))
    print(f"bill is {b//a}")
    print("per head bill is :{}".format(b//a))
split()
'''


#TASK:

'''def cal():
    a=int(input("enter A value:"))
    b=int(input("enter B value"))
    c=int(input("enter the option:"))
    if c==1:
        print("the sum is:",a+b)
    elif c==2:
        print("the diff is:",a-b)
    elif c==3:
        print("the product is:",a*b)
    elif c==4:
        print("the ans is: ",a//b)
    else:
        print("plz choose the correct option")
cal()'''


'''while True:
    def cal():
        a=int(input("enter A value:"))
        b=int(input("enter B value"))
        c=int(input("enter the option:"))
        if c==1:
            print("the sum is:",a+b)
        elif c==2:
            print("the diff is:",a-b)
        elif c==3:
            print("the product is:",a*b)
        elif c==4:
            print("the ans is: ",a//b)
        else:
            print("plz choose the correct option")
    cal()'''











