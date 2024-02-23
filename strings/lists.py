if __name__ == '__main__':
    N = int(input())
    end_list = []
    for _ in range(1, N + 1):
        list_operations = input().split()
        if len(list_operations) == 3:
            end_list.insert(int(list_operations[1]), int(list_operations[2]))
        elif len(list_operations) == 2:
            if list_operations[0] == 'remove':
                end_list.remove(int(list_operations[1]))
            else:
                end_list.append(int(list_operations[1]))
        else:
            if list_operations[0] == 'print':
                print(end_list)
            elif list_operations[0] == 'sort':
                end_list.sort()
            elif list_operations[0] == 'pop':
                end_list.pop()
            elif list_operations[0] == 'reverse':
                end_list.reverse()


