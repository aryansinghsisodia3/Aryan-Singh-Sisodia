# THIS PROGRRAM GIVES THE SUM OF FIRST n NUMBERS , WHERE n IS PROVIDED BY THE USER

# ASSIGNING THE VALUES
a=1
d=1
n=float(input("Enter Number of Terms: "))

# FORMULA n/2 {2A + (N-1) D }
abc=(n*(2*a+n*d-d)/2)

# FINAL OUTCOMES
print("sum", "of" ,"terms", "is :",(abc))