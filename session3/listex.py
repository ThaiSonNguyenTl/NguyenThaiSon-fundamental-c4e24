items = ["com ", "chao ", "pho"]

print(*items,sep=",")
new_items = input("ban an gi them? ")
items.append(new_items)
print(*items,sep = ",") #co * de in ra ko co dau []
# sep = " ," co dau , o giua