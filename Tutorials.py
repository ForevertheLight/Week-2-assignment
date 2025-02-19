#Functions 
#print('A value')
#print(input('ask for a value:'))

#Methods - Functions of datatypes
#print('value'.upper())
#print('value'.lower())
#print('value'.replace ('u',''))

#New_Functions
#print(abs(-20))
#print(max([1,2,3,4,5,6,7,8,9,17]))
#print(min([1,2,3,4,5,6,7,8,9,17]))
#print(len([1,2,3,4,5,6,7,8,9,'String']))

#Exercise 
#Create a Pythagoras theorem calculator
#Once it is run, the code should ask the user for two numbers
#That are width and height of a triangle
#It should output the length of the hypotenuse
#Square root is equal to the power of 1/2
Width=int(input('Enter Width of A Triangle:'))
Height=int (input('Enter Height of A Triangle:'))
Hypotenuse= (Width**2) + (Height**2)
Pythagoras_theorem= (Hypotenuse**(1/2)) 
print('Length of the Hypotenuse =',round(Pythagoras_theorem,2))

