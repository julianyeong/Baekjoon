def solution(answers):
    
    p=[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    # 정답 리스트 길이
    n = len(answers)
    scores=[0,0,0]
    for i in range (n): #~번째 행에 있는 숫자들과 answer
        for j in range(len(p)):
            if(answers[i]==p[j][i%len(p[j])]):
                       scores[j]+=1
    
    max_score = max(scores)
    
    highest_scores=[]
    for i,score in enumerate(scores):
        if score==max_score:
            highest_scores.append(i+1)
    return highest_scores
   