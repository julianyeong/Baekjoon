while True: 
    sentence = input()
    if sentence == ".":  # 종료 조건
        break

    check = []
    answer = "yes"
    
    for s in sentence[:-1]:  # 마지막 '.' 제외
        if s == "(" or s == "[":  # 여는 괄호 push
            check.append(s)
        elif s == ")" or s == "]":  # 닫는 괄호 검사
            if not check:  # 스택이 비어 있으면 짝이 안 맞음
                answer = "no"
                break
            top = check.pop()  # 마지막 여는 괄호 꺼내기
            if (s == ")" and top != "(") or (s == "]" and top != "["):
                answer = "no"
                break  # 괄호 짝이 맞지 않음
    
    if check:  # 스택에 남은 괄호가 있으면 균형X
        answer = "no"
    
    print(answer)
