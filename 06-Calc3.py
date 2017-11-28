def calc(opr,x,y):
    return eval(x + opr + y)

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
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*",
        }

    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")

    result = calc(todo.get(userInput), num_1, num_2)
    print(result)

##    result = todo.get(userInput, errHandler)(userInput,num_1, num_2)
##    print(result)








