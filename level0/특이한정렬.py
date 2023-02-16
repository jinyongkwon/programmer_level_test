def solution(numlist, n):
    result = {}
    for num in numlist:
        result[num] = abs(num - n)
    return sorted(result, key=lambda x: (result[x], -x))

# sorted함수에서 key를 지정할 수 있음.
# 넘어 갈때 tuple로 넘어가며 순서를 지정해주면 순서대로 비교를 함.
print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
