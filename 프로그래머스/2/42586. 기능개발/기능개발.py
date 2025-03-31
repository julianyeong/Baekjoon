from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)  
    speeds = deque(speeds)
    answer = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        num = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            num += 1

        if num > 0:
            answer.append(num)

    return answer