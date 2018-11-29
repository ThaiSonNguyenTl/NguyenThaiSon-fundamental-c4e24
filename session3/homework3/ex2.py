from random import randint
x = randint(1,100)
loop = True
while loop:
    n = int(input("Guess my number(1-100)?: "))
    if n > x :
        print("A little too large =(")
    elif n < x :
        print("Too small =(")
    else:
        print("Bingo =))")
        loop = False