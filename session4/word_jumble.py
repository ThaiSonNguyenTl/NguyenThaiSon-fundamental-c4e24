from random import randint
word = "hexagon"
character = list(word) #chuyen doi kiu du lieu 
print(character)
#1.select character ramdomly
#1.1 random => number0 => len -1
#1.2 number =>index


while len(character ) >0:

    for i in range (len(character)):
        x = int (randint(0,len(character)-1))
        print(character[x],end = " ")
        character.pop(x)

    #   i = randint(0,len(character)-1)
    #   ch = character[i]
    #   print(ch,end ="")
    #   character.pop(i)
    print()
    user_guess = input("your guess?")
    if user_guess == word:
        print("hura")
    else:
        print("=(")