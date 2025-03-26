def solution(my_strings, parts):
    answer = ''
    order = 0
    
    for s, e in parts:
        answer += my_strings[order][s:e+1]
        order += 1
    return answer

