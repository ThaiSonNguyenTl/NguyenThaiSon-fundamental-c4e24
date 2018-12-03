items = ["T-Shirt", "Sweater"]

while True:
    cmd = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()
    if cmd == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items:",*items ,sep=", ")
    elif cmd =="R":
        for index, item , in enumerate(items):
            print(index +1 , item ,sep = ".")
    elif cmd == "U":
        n = int(input("Update position? "))
        while True:
            if n > len(items):
               n = int(input("enter again :"))
            else:
               m = str(input("New item? "))
               items[n-1] = m
               print("Our items:",*items ,sep=", ")
               break
    elif cmd == "D":
        h = int(input("Delete position? "))
        while True:
            if h > len(items):
                h = int(input("enter again: "))
            else:
                items.pop(h-1)
                print("Our items:",*items ,sep=", ")
                break
    else: 
       break