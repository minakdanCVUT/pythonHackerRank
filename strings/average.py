def average(array):
    array.sort()
    for i in range(len(array)):
        if i + 1 < len(array):
            while True:
                if i + 1 < len(array):
                    if array[i] is array[i + 1]:
                        array.remove(array[i + 1])
                    else:
                        break
                else:
                    break
        else:
            break
    average = float("{:.{}f}".format(sum(array) / len(array), 3))
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

