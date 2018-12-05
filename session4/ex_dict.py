dienthoai = {
"ip" :  "iphone",
"ss" : "samsung",
"opp": "oppo",
"hw": "huaweir",
}
while True:
    print(*dienthoai)
    code = str(input("your code? "))
    print(dienthoai[code])
    print()
    update = input("do you want to update(Y/N): ").upper()
    if update == "Y":
        new_translations = input("your translation:  ")
        dienthoai[code] = new_translations
        print("done")
    else:
        print("not found")
        creat = input("Do you want to contribute(Y/N)?  ").upper()
        if creat == "Y":
            translation = input("your translation: ")
            dienthoai[code] = translation
        
