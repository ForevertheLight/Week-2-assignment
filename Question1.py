#Using forloop, write a python program to find the sum of numbers from 1-20
#except the numbers (3,8,10,11,19)
for x in range (1,21):
    if x==3 or x==8 or x==10 or x==11 or x==19:
        continue
    else:
        print(x)
        