items = ["neflix", "teaching"]
cmd = input("what do you want(C,R,U,D)?").upper()
if cmd == "C":
    new_items = input("what you want to add?")
    items.append(new_items)
    print(items)
elif cmd =="R":
    for index , item in enumerate(items):
        print(index,item)
