#재귀 dfs..? 개념이 완전히 와 닿지는 않는다 ㅜㅜㅜㅜ
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if idx == N and value == target:
        answer += 1
        return
    elif idx == N:
        return
    
    DFS(idx+1, numbers, target, value + numbers[idx])
    DFS(idx+1, numbers, target, value - numbers[idx])
    
def solution(numbers, target):
    DFS(0, numbers, target, 0)
    return answer