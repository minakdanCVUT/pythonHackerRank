def count_substring(string, sub_string):
    count = 0
    const_len_of_substring = len(sub_string)
    for i in range(len(string) + 1):
        if i + const_len_of_substring <= len(string):
            new_line = ''
            for temp_i in range(i, i + const_len_of_substring):
                new_line += string[temp_i]
            if new_line == sub_string:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
