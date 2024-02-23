

def split_and_join(line):
    new_line = ''
    for char in line:
        if char == ' ':
            new_line += '-'
        else:
            new_line += char
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

