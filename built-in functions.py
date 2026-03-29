'''
print(dir())
print(dir("__builtins__"))
'''


#fromkeys : fromkeys are only used and usable in dictionaries

'''
a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)   #fromkeys is a built-in
print(b)

b=dict.fromkeys(a,"yaseer")
print(b)

b["o"]="python"
print(b)
'''


#eval()
'''
while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
'''

'''
while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)
'''

'''
while True:
    a=input("a value:")
    b=input("b value:")
    print(a+b)
'''

'''
while True:
    a=eval(input("a value:"))         #eval():
    b=eval(input("b value:"))         #eval():
    print(a+b)
'''


#zip() : we can combine multiple connections into one connection

'''
a=[10,20,30,40,50,60]
nam=["crack","jack","stoner","likit","bittu"]
print(a+nam)

b=list(zip(a,nam))
print(b)

b=tuple(zip(a,nam))
print(b)

b=set(zip(a,nam))
print(b)

b=dict(zip(a,nam))
print(b)
'''

#enumerate() : we can give counter to the collection
nam=["crack","jack","stoner","likit","bittu"]
for i in range(len(nam)):
    print(i,nam[i])

b=list(enumerate(nam))
print(b)

b=list(enumerate(nam,100))
print(b)

b=tuple(enumerate(nam))
print(b)

b=set(enumerate(nam))
print(b)

b=dict(enumerate(nam))
print(b)




















    
