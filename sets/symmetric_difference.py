def return_diff_list(first_set: set, second_set: set) -> list:
    diff_list = []
    for elem in first_set:
        if elem not in second_set:
            diff_list.append(elem)
        else:
            pass
    return diff_list


size_first_set = int(input())
first_set = set(map(int, input().split()))
size_second_set = int(input())
second_set = set(map(int, input().split()))

diff_list = []
diff_list += return_diff_list(first_set, second_set)
diff_list += return_diff_list(second_set, first_set)
diff_list.sort()
for elem in diff_list:
    print(elem, end='\n')


