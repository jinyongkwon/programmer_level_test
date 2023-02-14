# 첫번째 제출 답
"""
    for i in range(1, number+1):
        divisor = [j for j in range(1, i+1) if i % j == 0]
        if len(divisor) > limit:
            answer += power
        else:
            answer += len(divisor)
"""
# 문제는 약수를 구할 num에 대한 모든 수를 하나씩 전체 탐색 해서 시간이 무조건 log(N)
# => 시간초과

# 제곱근(루트) 구하는 식 num ** (1/2)
# 100 의 1승은 100, 100의 0.5승은 10
# math.sqrt(100) == 루트 100 == 100의 0.5승


def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        square_root = int(i ** (1/2))
        count = 0
        for j in range(1, square_root+1):
            if i % j == 0:
                if j == i//j:
                    count += 1
                else:
                    count += 2
        if count > limit:
            count = power
        answer += count
    return answer


print(solution(10, 3, 2))
