# Arithmetic Operators
# +, -, *, **, /, //, %
num1 = 20
num2 = 3
num3 = num1+num2
print("Result", num3)

import math
# math.pow(), math.sqrt()
print(math.pow(10,2))
print(math.sqrt(99))

# ==, !=, >, >=, <, <=
res = num1 == num2
print(res)
res = num1 != num2
print(res)
res = num1 > num2
print(res)
res = num1 >= num2
print(res)
res = num1 < num2
print(res)
res = num1 <= num2
print(res)

# and, or, not
res = (num1>num2) and (num1>num3)
print(res)

res = (num1>num2) or (num1>num3)
print(res)

print(not res)
print(not not res)

# in, not in, like , not like