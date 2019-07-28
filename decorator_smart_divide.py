
def smart_divide(func):
    def inner(x, y):
        print "Dividing", x, "and", y
        if y == 0:
            print "Cant divide by zero"
            return
        else:
            return func(x, y)
    return inner


def get_custom_decorator(msg1, msg2):
    def smart_divide(func):
        def inner(x, y):
            print msg1, x, "and", y
            if y == 0:
                print msg2
                return
            else:
                return func(x, y)
        return inner
    return smart_divide

@smart_divide
def divide1(x, y):
    result = x / y
    print result

@get_custom_decorator("Dividing", "Can't divide by zero.")
def divide2(x, y):
    result = x / y
    print result

if __name__ == "__main__":
    x = int(raw_input("Enter first number for division: "))
    y = int(raw_input("Enter second number for division: "))
    divide2(x, y)
