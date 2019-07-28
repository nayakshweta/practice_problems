
def anagram_detector(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        print "These are anagrams."
    else:
        print "These are not anagrams."

if __name__ == "__main__":
    string1 = raw_input("Enter first word:")
    string2 = raw_input("Enter second word:")

    anagram_detector(string1, string2)