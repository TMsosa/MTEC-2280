print("A: Add")
print("S: Subtract")
print("M: Multiply")
print("D: Div")

select = input("Enter option: ")

if select == "A":
    num1 = input("num1: ")
    num2 = input("num2: ")
    ans = int(num1) + int(num2)
    print(ans)

elif select == "S":
    num1 = input("num1: ")
    num2 = input("num2: ")
    ans = int(num1) - int(num2)
    print(ans)

elif select == "M":
    num1 = input("num1: ")
    num2 = input("num2: ")
    ans = int(num1) * int(num2)
    print(ans)

elif select == "D":
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    ans = float(num1) / float(num2)
    print(ans)
