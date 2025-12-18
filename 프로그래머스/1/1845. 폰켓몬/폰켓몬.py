# def solution(nums):
#     hashDict = {}
#     #1. hashDict로 다 저장하고
#     hashDict = {}
#     for num in nums:
#         hashDict[hash(hum)] = 
#     #2. key/2가 return
    
#     answer = 0
#     return answer

from collections import Counter

def solution(nums):
    hashCounter = Counter(nums)
    if len(nums)//2 < len(hashCounter):
        return len(nums)//2
    else:
        return len(hashCounter)