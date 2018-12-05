from random import randint
favs = ["hexagon" , "champions" , "iphone","samsung"]

for i in range(len(favs)):
    j = int(randint(0,len(favs)-1))
word = favs[j]
character = list(word)
# while True:    
for i in range (len(character)):
    x = int (randint(0,len(character)-1))
    print(character[x],end = " ")
    character.pop(x)
print()
user_guess = input("your guess?")
if user_guess == word:
    print("hura")
else:
    print("=(")