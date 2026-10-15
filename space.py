# # space complexity describes how the memory required by an algorithm grows as its input size increases
# #extra space means the additional memory used excluding the existing input 

# # constant speed = o(1)

listone=[1,2,3,4,5,6,7,8,9,10,100]
total=0
for value in listone:
    total+=value
print(total)

# #linear space = o(n)

listtwo=[1,2,3,4,5]
temp=[]
for values in listtwo:
    temp.append(values*values)
print(temp)

n=int(input())
listone=[]
for i in range(n):
    data=int(input())
    listone.append(data)
left=0
right=len(listone)-1
while left<right:
    temp=listone[left]
    listone[left]=listone[right]
    listone[right]=temp
    left+=1
    right-=1
print(listone)