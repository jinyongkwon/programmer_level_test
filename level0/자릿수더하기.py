def solution(n):
    answer = 0
    n = str(n)
    for num in n:
        answer += int(num)
    return answer

# list없이 sum만 사용한 정답
# answer = sum(int(i) for i in str(n))

# map과 sum을 사용한 정답
# answer = sum(list(map(int, list(str(n)))))
