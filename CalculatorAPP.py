name = input("Please enter your name: ")
print("Privet " + name + "!")

num1 = float(("Enter x = "))
num2 = float(input("Enter y = "))
oper = input("Choose operator")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "*":
    print(num1 * num2)
else:
    print("Error: there is no such operator")


