print("Enter two numbers one at a time, and this program will find the greatest common factor")
n1 = int(input("What is the first number?"))
n2 = int(input("What is the second number?"))
while(n2 != 0 ):
    carry = n2
    n2 = n1 % n2
    n1 = carry
print(str(n1) + " is the greatest common factor")