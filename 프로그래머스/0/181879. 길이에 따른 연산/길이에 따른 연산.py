def solution(num_list):
    if(len(num_list)>=11): #10 이상
        sum=0
        for i in range(len(num_list)):
            sum+=num_list[i]
        return sum#리스트 원소 합
    else:
        sum=1
        for i in range(len(num_list)):
            sum*=num_list[i]
        return sum