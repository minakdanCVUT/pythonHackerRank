def print_rangoli(size):
    new_line = ''
    count_lines = (size * 2) - 2
    without_lines = size - 1
    count_letters = 1
    const_number = 96 + size
    number = 96 + size
    for i in range(size * 2 - 1):
        if i != without_lines:
            new_line += ('-' * count_lines)
            for y in range(1, count_letters + 1):
                new_line += chr(number)
                if number is const_number and y is count_letters:
                    break
                new_line += '-'
                if y < count_letters // 2 + 1:
                    number -= 1
                else:
                    number += 1
            new_line += ('-' * count_lines)
            if i < without_lines:
                count_letters += 2
                count_lines -= 2
            else:
                count_letters -= 2
                count_lines += 2

        else:
            for y in range(1, count_letters + 1):
                new_line += chr(number)
                if number is const_number and y is count_letters:
                    break
                new_line += '-'
                if y < count_letters // 2 + 1:
                    number -= 1
                else:
                    number += 1
            count_letters -= 2
            count_lines += 2
        print(new_line, end='\n')
        new_line = ''


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

