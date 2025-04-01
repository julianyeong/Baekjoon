def solution(list):
    cnt = 0
    
    for n in list:
        while n!=1:
            if n%2 == 0:
                n = n/2
            else:
                n = (n-1)/2
            cnt += 1
    return cnt
