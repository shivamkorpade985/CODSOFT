def add(s,h):
    return s + h
    
def sub(s,h):
    return s - h
    
def mul(s,h):
    return s * h
    
def div(s,h):
    if h == 0:
        print("Error:Number is not Divisible by 0.")
    return s / h

print("Simple Calculator:")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("Operations:")
print("1.Additon")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operation = int(input("Enter operation:choose(1-4)"))
if operation == 1:
    result = add(num1,num2)
elif operation == 2:
    result = sub(num1,num2)
elif operation == 3:
    result = mul(num1,num2)
elif operation == 4:
    result = div(num1,num2)
else:
    print("Enter Valid Operation.")
    
print("Result is :",result)