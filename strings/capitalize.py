def solve(s) -> str:
    new_line = ''
    first_letter = False
    for char in s:
        if 'A' <= char <= 'z':
            if not first_letter:
                new_line += char.upper()
                first_letter = True
            else:
                new_line += char
        elif '0' <= char <= '9':
            if not first_letter:
                new_line += char
                first_letter = True
            else:
                new_line += char
        else:
            new_line += char
            first_letter = False
    return new_line


if __name__ == '__main__':
    s = input("Enter some words in lowercase: ")
    result = solve(s)
    print(result)

