def solution(answers):
    # 각 수포자의 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 정답 리스트 길이
    n = len(answers)
    
    # 정답 패턴을 문제 길이만큼 반복
    p1_a = (p1 * (n // len(p1))) + p1[:n % len(p1)]
    p2_a = (p2 * (n // len(p2))) + p2[:n % len(p2)]
    p3_a = (p3 * (n // len(p3))) + p3[:n % len(p3)]

    # 정답 비교 (맞힌 개수 계산)
    num1 = sum([1 for i in range(n) if p1_a[i] == answers[i]])
    num2 = sum([1 for i in range(n) if p2_a[i] == answers[i]])
    num3 = sum([1 for i in range(n) if p3_a[i] == answers[i]])

    # 가장 많이 맞힌 사람 찾기
    max_score = max(num1, num2, num3)
    result = []
    if num1 == max_score:
        result.append(1)
    if num2 == max_score:
        result.append(2)
    if num3 == max_score:
        result.append(3)

    return result
