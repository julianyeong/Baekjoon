def solution(participant, completion):
    #hashp
    #participant 모든 사람 false 해시
    #completion 사람 true
    hashDict = {}
    sumHash = 0
    #1. participant list의 hash를 구하고, hash 값 더하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    #2. completion list의 hash를 빼준다
    for comp in completion:
        sumHash -= hash(comp)
    #3. 남은 값이 hash가 됨
    answer = hashDict[sumHash]
    return answer
        
    
#     answer = ''
#     return answer
#sorting
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[(len(participant)-1)]