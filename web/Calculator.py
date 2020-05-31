#  Calculator

#  ADD FUNC()
def add(x, y):
   return x + y 

#  SUBTRACT FUNC()
def subtract(x, y):
   return x - y

#  MULTIPLY FUNC()
def multiply(x, y):
   return x * y

#  DIVIDE FUNC() 
def divide(x, y):
   return x / y

#  SELECTION OF OPERATORS
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

#  CHOICE
choice = input("Enter choice(1/2/3/4): ")

#  INPUT
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#  CHOICES CONDITION
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   try:
         print(num1,"/",num2,"=", divide(num1,num2))
   except: #ZeroDivisionError
      ZeroDivisionError:print("You cannot divide it with zero")      
else:
   print("Invalid input")