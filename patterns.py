#right angle triangle

n=int(input("enter the value:"))

for i in range(1, n + 1):
    for j in range(1, i+ 1):
        print("*",end=" ")
    print()

#reverse right angle triangle

n=int(input("enter the value:"))

for i in range(n, 0 ,-1):
    for j in range(i):
       print("*",end=" ")
       #print("*"*i)
    print()

#square

n=int(input("enter the value:"))

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#pyramid

n=int(input("enter the value:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print(" *"*i)









    
