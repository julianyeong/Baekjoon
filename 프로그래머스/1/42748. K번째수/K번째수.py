def solution(array, commands):
    answer = []
    #1. i-1부터 j-1까지 자르고
    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        #sliced = array[i-1:j].sort()
        #TypeError: 'NoneType' object is not subscriptable
        sliced = array[i-1:j]
        sliced.sort()
        
        #3. k 번쨰 선택해서 answer에 담고 반환
        answer.append(sliced[k-1])
    return answer