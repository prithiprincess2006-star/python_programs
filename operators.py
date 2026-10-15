
# task arithmetic operator

total_minutes=int(input("enter minutes: "))
print("hour: ",total_minutes//60)
print("minutes: ",total_minutes%60)

# task comparsion operator

mark=int(input("enter mark: "))
print(mark >=40)

# task logical operators

mark=int(input())
attendance=int(input())
print(mark >=40 and attendance >=70)

# task assignment operator

initial_balance=float(input("enter initial balance: "))
deposit_amount=float(input("enter deposit amount: "))
expense_amount=float(input("enter expense amount: "))
initial_balance += deposit_amount 
initial_balance -= expense_amount
print("final balance :",initial_balance)

# task membership operator

fruits=["apple","banana","grapes","kiwi"]
fruit=input("enter fruit name: ")
print(fruit in fruits)

# task identity operator

marks1=["80","90","100"]
marks2=marks1
marks3=["80","90","100"]
print(marks1 is marks2)
print(marks1 is not marks3)
print(marks1 == marks3)

# task  bitwise operator

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
a=(num1&num2)
b=(num1|num2)
c=(num1^num2)
d=(num1<<num2)
e=(num1>>num2)
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(num1<<num2)
print(num1>>num2)

# task tenery operator

mark=int(input())
result="Even" if num%2==0 else "Odd"
print(result)
