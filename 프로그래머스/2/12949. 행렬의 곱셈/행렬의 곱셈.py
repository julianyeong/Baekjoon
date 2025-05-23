def solution(arr1, arr2):
    
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    result = [[0] * c2 for _ in range(r1)]
        
    for i in range(r1): #행 수 만큼
        for j in range(c2): #열 수 만큼
            for k in range(c1):
                result[i][j]+=arr1[i][k]*arr2[k][j]
            
    return result