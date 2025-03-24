def solution(l, r):
    result = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            result.append(n)
        i += 1

    return sorted(result) if result else [-1]
