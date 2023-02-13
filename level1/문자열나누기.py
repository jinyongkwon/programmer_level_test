# 정답 풀이 중 제일 깔끔했던 코드
"""
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
    """


def solution(s):
    answer = 0
    check = {"choice": {"ch": s[0], "count": 1}, "etc": 0}  # 초기 상태
    i = 1
    while True:
        if len(s) == i:
            answer += 1
            break
        if check['choice']['count'] == check['etc']:  # 다시 초기상태로 설정.
            answer += 1
            check['choice']['ch'] = s[i]
            check['choice']['count'] = 1
            check['etc'] = 0
            i += 1
            continue
        if s[i] == check['choice']['ch']:  # 같을 경우
            check['choice']['count'] += 1
        else:  # 다를경우
            check['etc'] += 1
        i += 1

    return answer


print(solution("a"))
