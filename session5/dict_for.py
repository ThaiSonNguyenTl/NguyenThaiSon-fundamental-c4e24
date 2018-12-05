person = {
    "name":  "H.duc",
    "age" :  23,
    "city": "Hanoi",
    "books": ["sapiens", "Tieu ngao giang ho", "Tam quoc"]
}
# for x in person:
#     print(x, person[x])
# for v in person.values():
#     print(v)
for k,v in person.items():
    print(k,v)
# kieu 1 : dictionnary boc list
# kieu 2 : list boc dictionnary
#3 : 1 +2
# print(person["name"])
# print(person["books"])
# books = person["books"]
# print(books)
# for b in books: #co the vier in person["books"]
#     print(b)
# print(person["books"][1])