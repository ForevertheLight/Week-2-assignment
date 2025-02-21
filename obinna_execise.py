import obinna
list = [8,3,5,20]
first_value=list[0]
second_value=list[1]
third_value=list[2]
fourth_value=list[3]

# for expo
Exponent=obinna.exponentiation(first_value,second_value)
print("exponentiation of ",first_value," and ",second_value," = ",Exponent)

# for floor_division
floor=obinna.floor_division(fourth_value,first_value)
print("floor_division of ",fourth_value," and ",first_value," = ",floor)

# for modulus_number
number=obinna.modulus_number(fourth_value,second_value)
print("modulus_number of",fourth_value," and ",second_value," = ",number)

#for factorial
number=obinna.factorial_number(third_value)
print("factorial of",third_value," = ",number)