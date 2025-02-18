#Write a program that counts the number of even and odd numbers in the list below
#Using a for loop
Even_Count=0
Odd_Count=0
numbers=[1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x%2==0:
        Even_Count+=1
        print(Even_Count)
    else:
         Odd_Count+=1
         print(Odd_Count)