#Write a program that prints numbers from 1-20, But skips multiples of 3
#Using continue and stops the loop if the number is greater than 15 
#Using Break 
for i in range (1,21):
    if i%3==0:
        continue
    elif i==15:
        break
    else: 
        print(i)