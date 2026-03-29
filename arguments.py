##Keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="yaseer"
    mailid="yaseer@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''
def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="ram",mailid="r@gmail.com")
details(id=40,name="mani",mailid="m@gmail.com")
details(60,"likit","l@gmail.com")
details(mailid="y@gmail.com",name="yaseer",id=80)
details("s@gmail.com","siva",90)#only printed in postion when a positional argumnet is passed
'''


##Swapping Task
'''
a=10
b=20
print("a=",b)
print("b=",a)
'''

'''
a=10
b=20
a,b=b,a
print("a:",a)
print("b:",b)
'''

'''
a=10
b=20
temp=a
a=b
temp=b
print("a=",a)
print("b=",b)
'''

##arthematic swapping
'''
a=10
b=20
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)
'''

##Number formatting
'''
a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))
'''


##default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("sugar",100)'''

'''
def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery()
'''

'''
def Grocery(item,price=1000):
    print("item is %s" %item)
    print("price is %d" %price)
Grocery("ghee")
'''

'''
def Grocery(item="dhal",price):
    print("item is %s" %item)
#(non-def arguments follows def arguments here non-def=price,def="item=dhal")
    print("price is %d" %price)                #error
Grocery(100)'''

'''
def Bakery(name,price,quantity):
    print("name of cake: %s" %name)
    print("price of cake: %d" %price)
    print("quantity of cake %s" %quantity)
Bakery("red velvet",800,"1kg")
'''

'''
def Bakery(name="red velvet",price=800,quantity="1kg"):
    print("name of cake: %s" %name)
    print("price of cake: %d" %price)
    print("quantity of cake %s" %quantity)
Bakery()
'''

'''
def Bakery(name,price=800,quantity="1kg"):
    print("name of cake: %s" %name)
    print("price of cake: %d" %price)
    print("quantity of cake %s" %quantity)
Bakery("chocolate moose")
'''

'''
def Bakery(name="red velvet",price,quantity):
    print("name of cake: %s" %name)
    print("price of cake: %d" %price)         #error
    print("quantity of cake %s" %quantity)
Bakery(1000,"2kg")
'''

## *arguments


'''a=[3,4,5,6,7,8,9,10,11]
print(a)
print(*a)
print(type(a))'''

'''
b=(4,5,6,7,8,9)
print(b)
print(*b)
print(type(b))'''

'''
b={4,5,6,7,8,9}
print(b)
print(*b)
print(type(b))'''

'''
b={"name":"yaseer","year":2026,"month":"march"}
print(b)
print(*b)
print(type(b))
'''

'''
a="codegnan"
print(a)
print(*a)
'''

'''
a,b,c=(4,5,6,7,8,9,10,11,12,13)
print(a)
print(b)
print(c)''' #error

'''
a,*b,c=(4,5,6,7,8,9,10,11,12,13)
print(a)
print(*b)
print(c)'''

'''
*a,b,c=(4,5,6,7,8,9,10,11,12,13)
print(*a)
print(b)
print(c)'''

'''
a,*b,c=("codegnan")
print(a)
print(*b)
print(c)'''

'''
*a,b,c=("codegnan")
print(*a)
print(b)
print(c)
'''

##variable length arguments :{variable length arguments are automatically stores in tuple and we use star arguments}


'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8,9)
d=[3,4,5,6,7,8,9]
check(*d)
e={4,5,6,7,8,9}
check(*e)
f={"name":"yaseer","course":"python"}
check(*f)'''


'''
def check1(*a):
    d=1#creating a variable
    print(a)
    print (type(a))
    for i in a:
        if type(i) in (int,float):
            d+=1
            print(d)
check1()
check1 (2,3,4,5,6,7,8,9)
check1(2,3,4,4.5,5.2)
check1(1,3,5,7,9,3.5,4.2,"yaseer",5+10j,True,False)
'''

##** args (kwargs = keyword arguments)
'''
def check2(**a):
    print(a)
    print(type(a))
check2()
details={"idnos":[10,20,30]
         "names":["ajay","vijay","ramesh"]
         "status":["P","A","P"]}
check2(**details)'''

'''
def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"idnos":[10,20,30],
         "names":["ajay","vijay","ramesh"],
         "status":["P","A","P"]}
check2(**details)'''

##both * and ** usage

'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key :",i)
        print("key :",j)
final()
data=(2,3,4,5,6,4.5,3.5)
final(*data)
details={"idnos":[10,20,30],
         "names":["ajay","vijay","ramesh"],
         "status":["P","A","P"]}
final(**details)
final(*data,**details)'''














