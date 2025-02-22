#Re-write the following for loop using list comprehension:
# Squares=[]
# for i in range (10):
#     Squares.append(i**2)
# print (i)
Squares=[i**2 for i in range (10)]
print(Squares)
