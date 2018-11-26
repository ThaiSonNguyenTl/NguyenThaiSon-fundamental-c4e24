h = int(input("enter the height(cm)? "))
h1 = h / 100 
m = int(input("enter the weight(kg)?  " ))
BMI = m / (h1 * h1)
print( "BMI = ", BMI)
if BMI < 16:
    print(" Severely underweight ")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")