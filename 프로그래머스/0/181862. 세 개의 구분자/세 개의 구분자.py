def solution(myStr):
    answer = []
    myStr = myStr.replace('a',' ')
    myStr = myStr.replace('b',' ')
    myStr = myStr.replace('c',' ')
    ans = myStr.split()
    return ans if ans else ["EMPTY"]
