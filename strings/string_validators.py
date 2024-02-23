def ifAlphaNumeric(s) -> bool:
    for char in s:
        if char.isalnum():
            return True
    return False

def isHasAplhas(s) -> bool:
    for char in s:
        if char.isalpha():
            return True
    return False

def ifHasDigits(s) -> bool:
    for char in s:
        if char.isdigit():
            return True
    return False

def ifHasLower(s) -> bool:
    for char in s:
        if char.islower():
            return True
    return False

def ifHasUpper(s) -> bool:
    for char in s:
        if char.isupper():
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(ifAlphaNumeric(s))
    print(isHasAplhas(s))
    print(ifHasDigits(s))
    print(ifHasLower(s))
    print(ifHasUpper(s))
