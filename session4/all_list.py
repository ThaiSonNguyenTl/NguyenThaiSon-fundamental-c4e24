cmd = str(input("what do you want (C,R,U,D)?")).upper()
fav = ["com" , "pho" ,"bun"]
if cmd == "C":
    n = str(input("ban muon them j ?"))
    fav.append(n)
    print(fav)
elif (cmd == "R"):
    print(*fav, sep =" ")
elif cmd == "U":
    j = int(input("vi tri ban muon sua?"))
    m = str(input("ban muon sua j?  "))
    fav[j] = m
    print(fav)
else:
    k = int(input("ban muon xoa j ?"))
    fav.pop(k)
    print(fav)


