# def solution(clothes):
#     answer = 1
#     #1. 의상종류로 hashmap 만들기, value += 1
#     hashmap = {}
#     for i in range(len(clothes)):
#         hashmap[clothes[i][1]] = 1
#     for j in range(len(clothes)):
#         hashmap[clothes[j][1]] += 1
        
#     #2. return value 값들의 곱 -1 
#     for z in hashmap:
#         answer *= hashmap[z]
#     return answer-1

#간결ver
def solution(clothes):
    answer = 1
    
    types = {}
    for c, t in clothes:
        if t not in types:
            types[t] = 2
        else:
            types[t] += 1
            
    for cnt in types.values():
        answer *= cnt
    return answer-1