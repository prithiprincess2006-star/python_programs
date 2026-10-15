# for loop statement

for i in range(10):
    print("hello bangtan")

for i in range (1,10):
    print(i)

for i in range (1,101,2):
    print(i,end=" ")

for i in range (5,0,-1):
    print(i)

num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

num1=int(input())
num2=int(input())
total=0
for i in range(num1,num2+1):
    if i%2==0:
        total=total+i
print(total)   

num=int(input("enter the num: "))
for i in range(1,11):
    print(num," * ",i," = ",num*i)

num=int(input())
fact=1
for i in range(num,0,-1):
    fact=fact*i
    print(i,end=" ")
    if i!=1:
        print("*",end=" ")
print("=",fact)
