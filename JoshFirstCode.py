#Using a loop, write a Python program to find the sum of numbers from 1-20
#except numbers (3,8,11,10,19)
for x in range(1,21):
    if x==3 or x==8 or x==11 or x==10 or x==19:
        continue
    else:
        print(x)
#Write a program that asks the user to enter a password 
#If the password is incorrect, keep asking until the correct password is entered.
#Using a while loop
Password=input("Enter a Password:")
Pass_W='Encrypted'
while Password!=Pass_W:
    print("Enter a correct password")
    Password=input("Enter a Password:")
print("You have entered a correct password",Password)