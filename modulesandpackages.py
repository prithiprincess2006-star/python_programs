# modules and packages

import math
import calculator
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

result=calculator.add(5,6)
print(result)

try:
    a=int(input())
    b=int(input())
    print(a//b)
except ValueError:
    print("please enter integer only")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("jungkook")