import sys

def smart_divide(divide):
    def inner(x, y):
        print "I am going to divide", x, "and", y
        if y == 0:
            print "This is operation is invalid!"
            return
        else:
            return divide(x, y)
    return inner

@smart_divide
def divide(x, y):
    result = x / y
    print result

if __name__ == "__main__":
    x = int(raw_input("Enter first number for division: "))
    y = int(raw_input("Enter second number for division: "))
    divide(x, y)
