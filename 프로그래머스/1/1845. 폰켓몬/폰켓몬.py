from collections import Counter

def solution(nums):
    hashCounter = Counter(nums)
    if len(nums)//2 < len(hashCounter):
        return len(nums)//2
    else:
        return len(hashCounter)
    