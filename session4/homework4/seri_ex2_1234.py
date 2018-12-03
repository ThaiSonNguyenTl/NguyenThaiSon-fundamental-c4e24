sheep = [5  ,  7  ,  300  ,  90  ,  24  ,  50  ,  75]
print("Hello my name is Hiep and these are my ship sizes \n" ,sheep)
n = max(sheep)
print("Now my biggest sheep has size ",n,"let's shear it",end = " ")
print()
m = sheep.index(n)
sheep.pop(m)
sheep.insert(m,8)
print("After shearing,here is my flock \n ",sheep)
for i in range(len(sheep)):
    sheep[i] = sheep[i] +  50
print("One month has passed, now here is my flock \n",sheep)
    