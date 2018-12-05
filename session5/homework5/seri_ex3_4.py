print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4(x+3) ? ")
result = {
    "1": 35,
    "2": 36,
    "3": 40,
    "4": 44
}
for p in result:
    print(p,result[p],sep = ".")
landung = 0
m = int(input("Your choice: "))
if m==4:
    print("Bingo")
    landung += 1
else:
    print("=((")
print("Estimate this answer (exact calculation not needed) :")
print("Jack scored these marks in 5 math test: 49, 81, 72, 66 and 52.what is the mean? ")
DiemTB = {
    "1": "About 55",
    "2": "About 65",
    "3": "About 75",
    "4": "About 85"
}
for i in DiemTB:
    print(i,DiemTB[i],sep =".")
n = int(input("Your choice: "))
if n == 2:
    print("Bingo")
    landung += 1

print("Your correctly answer", landung,"out of 2 question",end =" " )