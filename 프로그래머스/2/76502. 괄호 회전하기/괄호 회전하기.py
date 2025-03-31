def solution(s):
    answer = 0
    n = len(s)
    for j in range(n): # s를 왼쪽으로 회전
        stack=[ ]
        for i in range(n): #회전한거 내에서 순서대로 비교
            c = s[(i+j)%n]
            
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    break
                    
                if c == ')' and stack[-1] == '(':
                    stack.pop() 
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
                
        else: 
            if not stack:  # 스택이 비어 있으면 올바른 괄호 문자열
                answer += 1
            
    return answer