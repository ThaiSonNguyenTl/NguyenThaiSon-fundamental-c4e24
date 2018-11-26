n = int(input("enter n : "))
if n == 0:
    print(n)
elif n == 1:
    print(n)
else:
    m = 1
    for i in range(1,n+1):
        m *= i
    print("n! =", m)
