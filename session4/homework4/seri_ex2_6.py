sheep = [5  ,  7  ,  300  ,  90  ,  24  ,  50  ,  75]
print("Hello my name is Hiep and these are my ship sizes \n" ,sheep)
n = max(sheep)
print("Now my biggest sheep has size ",n,"let's shear it",end = " ")
print()
m = sheep.index(n)
sheep.pop(m)
sheep.insert(m,8)
print("After shearing,here is my flock \n ",sheep)

month = 1
h = 3
while month < h:
    print("MONTH : ", month )
    for i in range(len(sheep)):
        sheep[i] = sheep[i] +  50
    print("One month has passed, now here is my flock \n",sheep)
    n = max(sheep)
    print("Now my biggest sheep has size ",n,"let's shear it",end = " ")
    print()
    m = sheep.index(n)
    sheep.pop(m)
    sheep.insert(m,8)
    print("After shearing,here is my flock \n ",sheep)
    month += 1
 
print("MONTH : 3 ")
for i in range(len(sheep)):
    sheep[i] = sheep[i] +  50
print("One month has passed, now here is my flock \n",sheep)
sheep_kg = sum(sheep)
print("My flock has size in total:",sheep_kg)
money = 2
sheep_money = sheep_kg * money
print("I would get ", sheep_kg ," * " , money ," $ ","=", sheep_money,"$")