# def solution(arr):
#     answer = []
#     l_a = len(arr) #6
#     needed0 = 0
#     for i in range(11):
#         if l_a <=2**i:
#             needed0 = 2**i - l_a
#             answer = arr + [0]*needed0
#             return answer

def solution(arr):
    needed0 = 0
    for i in range(11):
        if len(arr) <=2**i:
            needed0 = 2**i - len(arr)
            return arr + [0]*needed0
