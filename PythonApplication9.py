def zeros(n):
    n = int(n)
    if n < 5:
        return 0
    return n // 5 + zeros(n // 5)
print (zeros(input()))