from collections import Counter

count_sizes = int(input())
sizes = list(map(int, input().split()))
key_items = dict(Counter(sizes))
count_customers = int(input())
salary = 0
for _ in range(count_customers):
    i = list(map(int, input().split()))
    if key_items.get(i[0]) is not None:
        salary += i[1]
        key_items[i[0]] -= 1
        if key_items[i[0]] == 0:
            key_items[i[0]] = None
print(salary)

