#Subtraction of Two Numbers 
import Helper
#print(Helper.Sub_Function(45,5))

#Create List
List=[1,3,6,8,10,20]
FirstValue=List[0]
SecondValue=List[1]
ThirdValue=List[2]
FourthValue=List[3]
FifthValue=List[4]
SixthValue=List[5]

#Multiply two values 
Multiply=Helper.Multiply_Function(FirstValue,ThirdValue)
print('Multiplying', FirstValue, 'by',ThirdValue, '= ',Multiply)

#Exponent two values
Exponent=Helper.Exponent_Function(SecondValue,FourthValue)
print('Exponent of', SecondValue, 'and', FourthValue, '= ', Exponent)

#Subtract two values 
Subtract= Helper.Sub_Function(FifthValue,FourthValue)
print('Subtract',FifthValue, 'From', FourthValue, '= ',Subtract)

#Floor Division of two values
Floor=Helper.Floor_Division(SixthValue,SecondValue)
print('Floor Division of',SixthValue,'and', SecondValue, '= ',Floor)

#Modulus of two Values
Modulus=Helper.Modulus_Function(SixthValue,SecondValue)
print('Modulus of', SixthValue, 'and', SecondValue, '=', Modulus)

#Factorial of a value
Factorial=Helper.Factorial_Function(FourthValue)
print('Factorial of', FourthValue, '=', Factorial)

#Compare two values 
Compare=Helper.Compare_Function(SecondValue,SixthValue)
print(SecondValue, 'greater than', SixthValue,'is ', Compare)

#Minimum of Five Values 
Minimum=Helper.Min_Value_Function(FirstValue,SecondValue,ThirdValue,FourthValue,FirstValue)
print('The Minimum Value of', FirstValue,SecondValue,ThirdValue,FourthValue,FirstValue,'= ',Minimum)

#Maximum of Five Values
Maximum=Helper.Max_Value_Function(FirstValue,SixthValue,FourthValue,SecondValue,ThirdValue)
print('The Maximum Value of', FirstValue,SixthValue,FourthValue,SecondValue, ThirdValue, '=', Maximum)

#Add two values
Addition=Helper.Sum_Function(FifthValue,SixthValue)
print('The Addition of',FifthValue,'and', SixthValue, '= ',Addition)

