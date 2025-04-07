def solution(strArr):
    dic = {}
    for c in strArr:
        c_len = len(c)
        
        if c_len in dic:
            dic[c_len] += 1
        else:
            dic[c_len] = 1
            
    return max(dic.values())