
def dec_to_hex(decimal_number):
    temp = decimal_number
    hex_number = ""
    hex_dict = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    quotient = 1
    while quotient:
        quotient = temp / 16
        remainder = temp % 16
        if remainder <= 9:
            hex_number = str(remainder) + hex_number
        else:
            hex_number = hex_dict[remainder] + hex_number
        temp = quotient
    return hex_number

if __name__ == "__main__":
    decimal_number = raw_input("Enter a decimal number:")
    print dec_to_hex(int(decimal_number))
