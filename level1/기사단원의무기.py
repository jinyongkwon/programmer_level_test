# 첫번째 제출 답
"""
    for i in range(1, number+1):
        divisor = [j for j in range(1, i+1) if i % j == 0]
        if len(divisor) > limit:
            answer += power
        else:
            answer += len(divisor)
"""
# 문제는 약수를 구할 num에 대한 모든 수를 하나씩 전체 탐색 해서 시간이 무조건 O(N)
# => 시간초과

# 제곱근(루트) 구하는 식 num ** (1/2)
# 100 의 1승은 100, 100의 0.5승은 10
# math.sqrt(100) == 루트 100 == 100의 0.5승
# 약수를 구할 때 루트값 이하의 수들로 약수를 구하면 O(루트N)의 시간복잡도를 가짐
# 1 ~ int(루트값)까지만 기존의 수에 대한 약수를 구한다.
# 약수는 대칭성을 가지기 때문에 루트값으로 값을 구하는게 가능하다.
# 루트값으로 구한 약수의 갯수는 대칭성을 가짐으로 2개이고
# 약수의 마지막 값과 기존수/약수의 마지막값이 일치할경우 1개이다.
# ex1 ) 16의 약수 = 1, 2, 4, 8 , 16
# 16의 루트값 = 4 => 1,2,3,4로 약수를 구함
# 1,2 가능 마지막 값이 아니므로 2개
# 3 불가능
# 4 가능, 마지막 값이면서 16/4와 동일 그러므로 1개
# 총 5개의 약수 갯수를 가짐


def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        square_root = int(i ** (1/2))
        count = 0
        for j in range(1, square_root+1):
            if i % j == 0:
                count += 2
                if j == i//j:
                    count -= 1
        if count > limit:
            count = power
        answer += count
    return answer


print(solution(10, 3, 2))
