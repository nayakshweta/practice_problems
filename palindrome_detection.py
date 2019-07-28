
def palindrome_detector(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        print "This is a palindrome."
    else:
        print "This is not a palindrome."

if __name__ == "__main__":
    string = raw_input("Enter a word:")
    palindrome_detector(string)