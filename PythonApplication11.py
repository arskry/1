import math

def count_find_num(primes_l, limit):

    all_values = []
    arr = list(primes_l)
    total = math.prod(arr)
    all_values.append(total)
    if total > limit:
        return []

    for num in primes_l:
        for total in all_values:
            value = num * total
            if value <= limit and value not in all_values:
                all_values.append(value)
    return [len(all_values), max(all_values)]

print(count_find_num(list((map(int, input().split()))), (int(input()))))
