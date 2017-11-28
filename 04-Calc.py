def add(x,y):
    print(x+y)
    print("Add Called...")

def sub(x,y):
    print(x-y)
    print("Sub Called...")

def div(x,y):
    print(x/y)
    print("Division Called..")

def mul(x,y):
    print(x*y)

def errHandler():
    print("Wrong Choice...")

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
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul,
        "5" : quit
        }

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo.get(userInput, errHandler)(num_1, num_2)








