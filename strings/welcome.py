arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

new_line = ''
iterator_for_lines = (m - 3) // 2
iterator_for_figures = 1
welcome_stop = n // 2 + 1
for i in range(1, n + 1):
    if welcome_stop != i:
        new_line += ('-' * iterator_for_lines)
        new_line += ('.|.' * iterator_for_figures)
        new_line += ('-' * iterator_for_lines)
        if welcome_stop < i:
            iterator_for_figures -= 2
            iterator_for_lines += 3
        else:
            iterator_for_figures += 2
            iterator_for_lines -= 3
        print(new_line, end='\n')
        new_line = ''
    else:
        new_line += ('-' * ((m - 7) // 2))
        new_line += 'WELCOME'
        new_line += ('-' * ((m - 7) // 2))
        print(new_line, end='\n')
        new_line = ''
        iterator_for_figures -= 2
        iterator_for_lines += 3

