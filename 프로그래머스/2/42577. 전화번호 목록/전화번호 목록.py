#loop
# def solution(phone_book):
#     answer = True
#     i = 0
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return answer

#sorting
#목표는 이중루프 없애는 것
# def solution(phone_book):
#     answer = True
    
#     phone_book.sort()
    
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
#     return answer

#sorting, zip
#python스러운 코딩
# def solution(phone_book):
#     #1. sorting
#     phone_book.sort()
#     #2. zip
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
    
#hash
def solution(phone_book):
    #1. hashmap 만들기
    hashmap = {}
    for num in phone_book:
        hashmap[num] = 1
        
    #2. 접두어가 hash map에 존재하는지 찾기
    for p_num in phone_book:
        jubdoo = ''
        for number in p_num:
            jubdoo += number
            #3. 접두어를 찾아야 함(기존 번호와 같은 경우는 제외한다)
            if jubdoo in hashmap and jubdoo != p_num:
                return False
    return True