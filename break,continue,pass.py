#difference between break,continue,pass
'''
break:
the break statement is used to terminate the entire loop
continue:
the continue statemnet is used to skip the current iteration and rest of the code will continue
pass:
a pass ststement is a null statement it does nothing but syntactically we need it'''

##break:
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''a=10
while a>=1:
    print(a)
    a=a-1
    if a==5:
        break'''
'''
for i in range(25):
    if i==15:
        break
    print(i)'''

'''a="python"
if a=="t":
    break    #error code
print()'''


'''a="python"
for i in a:
    if i=="h":
        break
    print(i,end=" ")'''


##continue:
'''a=20
while a>1:
    print(a)
    a=a-1
    if a==10:
        continue'''


'''a=20
while a>1:
    a=a-1
    if a==10:
        continue
    print(a)'''


'''for i in range(15):
    if i==12:
        continue
    print(i)'''


'''a="python"
for i in a:
    if i=="t":
        continue
    print(i)'''

    
##pass:
'''a=20
while a>2:
    print(a)
    a=a-1
    if a==10:
        pass'''


'''for i in range(10):
    if i==5:
        pass
    print(i)'''


a="code"
for i in a:
    if i=="d":
        pass
    print(i)
