loop = True #de bien cho de thay doi ,de dung lai
while loop:
    pwd = str(input(" enter password:  "))
    if len(pwd) > 8:
        if (not pwd.islower()) and (not pwd.isupper()) and (not pwd.isdigit()):       
            #khong duoc toan chu hoa va chu thuong va toan so
            loop = False
        else:
            print("password phai chua chu hoa va chu thuong ")
    else:
        print("password phai lon hon 8 ky tu ")
        
print("Ok")
   