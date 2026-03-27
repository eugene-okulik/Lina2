def fun(calc):
    def wrapper():
        a = int(input("Please, input first number: "))
        b = int(input("Please, input first number: "))
        operation = None
        if a < 0 or b < 0:
            operation = "*"
        elif a == b:
            operation = "+"
        elif a > b:
            operation = "-"
        else:
            operation = "/"
        return calc(a, b, operation)

    return wrapper


@fun
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    else:
        return first * second


print(calc())
