def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        num = t[i:len(p)+i]
        if int(num) <= int(p):
            answer += 1
    return answer


print(solution("10203", "15"))
