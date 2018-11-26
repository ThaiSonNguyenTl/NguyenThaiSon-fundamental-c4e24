a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

delta = b*b - 4*a*c
a2 = 2*a
if delta < 0:
    print("phuong trinh vo nghiem")
elif delta == 0:
    x = -b/(a2)
    print("phuong trinh co nghiem kep x1 = x2 =",x)
else:
    delta_sqrt = delta ** 0.5
    x1 = (-b + delta_sqrt)/(a2)
    x2 = (-b - delta_sqrt)/(a2)
    print("phuong trinh co hai nghiem phan biet:x1 =",x1,"x2 =",x2 )