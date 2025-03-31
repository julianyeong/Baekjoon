def solution(arr, delete_list):
    return [x for x in arr if x not in set(delete_list)]
