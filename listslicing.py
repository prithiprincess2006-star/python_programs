# # list slicing

arr=[10,20,30,40,50,60]        # list[start:stop:step]
print(arr[1:5])
print(arr[:3])
print(arr[3:])
print(arr[::2])

arr1=[10,20,30,20,50]
print(30 in arr1)
print(90 in arr1)
print(arr1.index(20))
print(arr1.count(20))
print(arr1.count(90))