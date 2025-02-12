#Write a program that asks the user to enter a password. 
#If the password is incorrect, keep asking until the correct password is entered
#Use a while loop
Password=input("Enter a Password:")
Pass_W="Encrypted"
while Password != Pass_W:
    print("Enter a correct Password")
    Password=input("Enter a Password:")
print("Well Done!")
    