#Write a program that calculates the factorial of a given number using a for loop.
Sum=0
Num=int(input("Enter a Number:"))
for x in range(Num):
    if x==0:
        continue
    else:
        print(x)
    Sum+=x
print(Sum)