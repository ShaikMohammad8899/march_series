#generators : no tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generators
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''
a=(i for i in range(16))
print(a)
'''

'''
a=(i for i in range(16))
print(*a)
print(type(a))
'''

'''
a=(i for i in range(16))
#print(*a)
#print(list(a))
#print(tuple(a))
print(set(a))
print(type(a))'''


#generators:
'''A generator is also a function which can be used as an iterator(loop) by producing group of values, where we use 'yield' keyword'''
#Yield  vs return:
'''return will terminate the function where as yield can pass the function and go on with every successive iteration'''


'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''


'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#Yeild v/s Return


'''def mygen():
    #return "python"
    #return "java"
    #return "C"
    return "python","java","c"
print(*mygen())'''

def mygen():
    yield "apple"
    yield "orange"
    yield "banana"

#print(*mygen())

#next()
d=mygen()
    
print(next(d))
print(next(d))
print(next(d))













