def validate_regon(regon):
    '''
    Checks if regon has correct length and if the control digit is correct, both for 9-digit and 14-digit.
    '''
    if (len(regon) != 9 and len(regon) != 14) or not regon.isdigit():
        print("Regon is incorrect, try again.")
        return False
    digits = [int(digit) for digit in regon]

    if digits[0] in range(0,4) and digits[1] in range(0,10) and digits[1]%2 == 0:
        if digits[0] == 3 and digits[1] in range(0,3):
            pass
        elif digits[0] == 3 and not digits[1] in range(0,3):
            print("Incorrect first 2 digits, try again.")
            return False
        else:
            pass
    else:
        print("Incorrect first 2 digits, try again.")
        return False

    if len(regon) == 9:
        weights = (8, 9, 2, 3, 4, 5, 6, 7)
        is_last_number_valid = sum(digit1 * digit2 for digit1, digit2 in zip(digits, weights)) % 11
        return is_last_number_valid == digits[8]
    elif len(regon) == 14:
        weights = (2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8)
        is_last_number_valid = sum(digit1 * digit2 for digit1, digit2 in zip(digits, weights)) % 11
        return is_last_number_valid == digits[13]

regon = input("Regon: ")
valid_regon = validate_regon(regon)
print(valid_regon)