
def memoize(func):
    squares_dict = {}
    def inner(x):
        if x in squares_dict:
            print "This operation has been performed earlier."
            return squares_dict[x]
        else:
            print "This is a new operation."
            squares_dict[x] = func(x)
            return func(x)
    return inner
    
@memoize
def square(x):
    return x * x

if __name__ == "__main__":
    while True:
        input = raw_input("Enter number to find the square of:")
        if input == "exit":
            exit(0)
        else:
            print square(int(input))