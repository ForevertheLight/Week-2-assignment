#Write a program that asks the user to enter a password. 
#If the password is incorrect, keep asking until the correct password is entered
#Use a while loop
Password=input("Enter a Password:")
Pass_W="Joshua@2025"
while Password != Pass_W:
    print("sorry, password authentication didn't work. please try again. ")
    Password=input("Enter a Password:")
print("Well Done!")
    