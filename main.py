def calc():
    a = float(input("a: "))
    b = float(input("b: "))
    op = input("+, -, *, /: ")

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)

calc()
