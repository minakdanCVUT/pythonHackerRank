def mutate_string(string, position, character):
    iterator = 0
    new_line = ''
    for char in string:
        if iterator == position:
            new_line += character
            iterator += 1
        else:
            new_line += char
            iterator += 1
    return new_line

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
