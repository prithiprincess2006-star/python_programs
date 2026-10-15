# while loop

num=int(input())
digits=0
total=0
while num!=0:
    rem=num%10
    digits+=1
    total+=rem
    num=num//10
print("no of digits: ",digits)
print("sum of digitd: ",total)

num=int(input())
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums+=rem
        num=num//10
    num=sums
else:
    print(num) 