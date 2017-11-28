def calc(ch,x,y):
    if ch == "1":
        return x + y
    elif ch == "2":
        return x - y
    elif ch == "3":
        return x / y
    elif ch == "4":
        return x * y
    else:
        return "Wrong choice"

def errHandler(x,y,z):
    quit()

main = True

while main:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    5. Quit
    """)

    userInput = input("Enter your choice : ")

    todo = {
        "1" : calc,
        "2" : calc,
        "3" : calc,
        "4" : calc,
        }

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    result = todo.get(userInput, errHandler)(userInput,num_1, num_2)
    print(result)








