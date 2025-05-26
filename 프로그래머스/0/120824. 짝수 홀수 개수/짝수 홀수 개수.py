def solution(num_list):
    ev = 0
    odd = 0
    for i in num_list:
        if i%2 == 0:
            ev += 1
        else:
            odd += 1
    return [ev,odd]