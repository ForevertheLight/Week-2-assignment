#for add
def sum_number(a,b,c):
    sum=a+b+c
    return sum
#result=sum_number(9,8,6)
#int(result)

def validate(username,password):
    default_username ="admin"
    default_password ="1234"
    if(default_username == username and default_password == password):
        return True
    else:
        return False
#print(validate("admin","1234"))

#for subtraction
def subtraction_number(a,b):
    subtraction=a-b
    return subtraction
# result=subtraction_number(9,2)
# print(result)

# for multiply
def multiply_number(a,b,c):
    multiply=a*b*c
    return multiply
#result=multiply_number(3,4,6)
#print(result)

#to store in element
# for expo
def exponentiation(a,b):
    exponentiation=a**b
    return exponentiation

#for floor division
def floor_division(a,b):
    floor_division=a//b
    return floor_division

#for modulus
def modulus_number(a,b):
    modulus_number=a%b
    return modulus_number

import math 
#for factorial
def factorial_number(a):
    factorial_number=math.factorial(a)
    return factorial_number
    

