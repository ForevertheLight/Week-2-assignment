#Addition Function
def Sum_Function(a:float ,b:float )-> float: 
    return a+b

#Subtraction Function 
def Sub_Function(a:float ,b:float ) -> float: 
    return a-b

#Floor Division Function
def Floor_Division(a:int ,b:int ) -> int:
    return a//b

#Factorial Function 
import math
def Factorial_Function(Num: int )-> int:
    return (math.factorial(Num))

#Modulus Function 
def Modulus_Function(a:int ,b:int)-> int:
    return a%b

#Maximum Value Function
def Max_Value_Function(a,b,c,d,e):
    return(max(a,b,c,d,e))

#Minimum Value Function
def Min_Value_Function(a,b,c,d,e):
    return(min(a,b,c,d,e))

#Exponent Function
def Exponent_Function(a:float ,b:float)-> float:
    return(a**b)

#Compare Function
def Compare_Function(a,b)-> bool:
    return a==b  

#Multiplication Function
def Multiply_Function(a: float,b: float)-> float:
    return(a*b)

#Percentage Function
def Percentage_Function(a,b,c=100):
    return (a/c)*b

#Discount Function
def Discount_Function(Amount):
    if Amount >=5000 and Amount <=7999:
        return (Percentage_Function(3,Amount))
    elif Amount >=8000 and Amount <=9999:
        return (Percentage_Function(5,Amount))
    elif Amount >=10000 and Amount <= 49999:
        return (Percentage_Function(10,Amount))
    elif Amount >=50000:
        return (Percentage_Function(15,Amount))
    else:
        return False

