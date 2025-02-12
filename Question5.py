#Write a program that asks the user to enter a number
#And keeps asking until the user enters a positive number using a while loop
Number=int(input("Enter a Number:"))
while Number <0:
    print("Enter a Positive Number")
    Number=int(input("Enter a Number"))
print("You have entered a correct number")