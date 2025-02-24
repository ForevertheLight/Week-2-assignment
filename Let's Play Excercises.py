#The manager of XYZ Supermarket has approached you, a software developer, 
#to design a discount system for their upcoming Christmas campaign. 
#The system should apply discounts based on the following conditions 
#using Python functions and if statements:
# A 3% discount for sales greater than or equal to 5,000.
# A 5% discount for sales greater than or equal to 8,000.
# A 10% discount for sales greater than or equal to 10,000.
# A 15% discount for sales greater than or equal to 50,000.
import Helper 
Amount=int(input('Enter Amount of Goods:'))
print('Amount of Goods','is','equal to', Amount)
Discount=Helper.Discount_Function(Amount)
print('Your Discount is ',Discount)


