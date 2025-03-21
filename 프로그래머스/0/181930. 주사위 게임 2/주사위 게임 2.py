def solution(a, b, c):
    #같은 거 0개
    if a!=b and b!=c and a!=c:
        return a+b+c
    #같은 거 3개
    elif a==b and b==c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    #같은 거 2개
    else:
        return (a+b+c)*(a**2+b**2+c**2)