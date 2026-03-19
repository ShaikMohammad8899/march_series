'''LIST COMPREHENSION:
every list comprehension can be rewritten as a for loop but.
every for loop cannot be rewritten in list comprehension'''

'''a=["codegnan","python","course"]'''
'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]

'''b=[i.upper() for i in a]
print(b)'''

'''
a=["vij","hyd","vzg"]
b=[i.title() for i in a]
print(b)
'''

'''
a=[2,4,5,6,8,12,13]
b=[i*i for i in a]
print(b)'''

'''a=[2,4,5,6,8,12,13]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)
'''

#if-usage in list comprehension
'''print([i for i in range(0,16) if i%2==0])

print([i for i in range(0,16) if i%2!=0])

print([i*i for i in range(0,16) if i%2==0])
'''

'''
fruits=["apple","banana","mango","kiwi","berry","grapes"]
b=[i for i in fruits if "a" in i]
print(b)'''


#no-elif usage in list comprehension

#if-else usage in list comprehension

'''a=[i*i if i%2==0  else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
#c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

#max,min,sum
'''print(max(3,5,7,9,12,14,16,25,28,30))'''

'''print(min(3,5,7,9,12,14,16,25,28,30))'''

'''a=(3,5,7,9,12,14,16,25,28,30)
print(sum(a))'''

#task

print("---------Student Marks Analysis Report-----------")
a=int(input("enter the total no.of students:"))

b=[int(input("enter student marks:")) for i in range(a)]
print(b)
print("maximum marks:",max(b))
print("maximum marks:",min(b))

marks=sum(b)
avg=b/a


print("total marks:",marks)
print("average marks:",avg)



'''print("---------Student Marks Analysis Report-----------")
a=int(input("enter the total no.of students:"))
mark=[]
for i in range(a):
        b=int(input("enter student marks:"))
        mark.append(b)
for j in mark:
    print(j)
high=max(mark)
low=min(mark)
total=sum(mark)
avg=total/a


print("maximum marks:",high)
print("maximum marks:",low)
print("total marks:",total)
print("average marks:",avg)







































