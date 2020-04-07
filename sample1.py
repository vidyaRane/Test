# default argument for second parameter
def add(num1, num2=1):
    return num1 + num2


sum1 = add(100, 200)
sum2 = add(8)  # used default argument for second param
sum3 = add(100)  # used default argument for second param
print(sum1)
print(sum2)
print(sum3)
