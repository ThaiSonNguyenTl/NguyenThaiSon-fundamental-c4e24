# person = {}
# print(person)
# print(type(person))

# person = {
# "name": "H.Duc" ,
# }
# print(person)

person = {
"name": "H.Duc",
"city": "Hai Phong",
"age" : 25
}
person["age"] = 18
print(person["age"])
print (person)
# if "status" in person:  #check xem mot thu co nam trong mot thu khac hay ko if "..." in .....
#     print("yes")
# else:
#     print("no")
person["age"] += 1
print(person ["age"])
person["status"] = False  # 
print(person)
#xoa
# del person["city"]
# print(person)