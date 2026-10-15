
# #linear search 

listtwo=[5,1,4,2,8]
find=200
found=False
for i in range(len(listtwo)):
    if listtwo[i]==find:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")
