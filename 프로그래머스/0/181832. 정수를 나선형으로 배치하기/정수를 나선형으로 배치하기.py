def solution(n):
    answer = [[0]*n for _ in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    c, r, m = 0, 0, 0
    
    for i in range(1, n**2+1):
        answer[c][r] = i
        nc, nr = c+move[m][0], r+move[m][1]
        
        if nc>=n or nc<0 or nr>=n or nr<0 or answer[nc][nr]!=0 :
            m = (m+1) % 4
            nc, nr = c + move[m][0], r + move[m][1]
        c, r = nc, nr
    return answer
