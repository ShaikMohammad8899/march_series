#chr

'''
print(chr(76))
print(chr(65))
print(chr(90))'''

'''print(chr("A"))#error'''

#ord(order)
'''
print(ord("A"))
print(ord("b"))
print(ord("G"))'''

'''print(ord(78))#error'''

'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")
'''

a=input("enter the name:")
for i in a:
    print(i,"-",ord(i))

