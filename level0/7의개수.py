def solution(array):
    answer = 0
    for num in array:
        for char in str(num):
            if char in "7":
                answer += 1
    return answer


print(solution([7, 77, 17]))
