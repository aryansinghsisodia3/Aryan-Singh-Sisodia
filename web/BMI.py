# This program calculates the Body Mass Index

# Weight
wt=float(input("Enter your Weight in Kilograms: "))

# Height
h=float(input("Enter your Height in metres: "))

#folmula
BMI=wt/(h**2)

# Conditions
if (BMI<18.4):
    print("Underweight")
elif (BMI>=18.5 and BMI<=24.9):
    print("Normal")
else:
    print("Obese")
