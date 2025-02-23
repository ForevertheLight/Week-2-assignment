#Write a program that asks the user to enter a number
#And keeps asking until the user enters a positive number using a while loop
Number=int(input("Enter a Number:"))
while Number <0:
    print("Please! Enter Positive Number Only")
    Number=int(input("Enter a Number:"))
print("Good Job! You have entered a positive number",Number)
