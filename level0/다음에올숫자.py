# 정답
# 3개의 값을 가지고 등비수열인지, 등차수열인지만 구하면 됨.
"""
def solution(common):
    a=[]

    if (common[1] - common[0]) == (common[2] - common[1]) :

        b = common[1] - common[0]
        answer = common[len(common) -1 ] + b

    elif (common[1] / common[0]) == (common[2] / common[1]) :

        b = common[1] / common[0]

        answer = common[len(common) -1 ] * b
    return answer
"""


def solution(common):
    answer = 0
    common.reverse()
    nums = set()
    for i in range(len(common)-1):
        nums.add(str(common[i] - common[i+1]))
    if len(nums) == 1:
        answer = common[0] + int(nums.pop())
    else:
        num = 0
        while True:
            num = nums.pop()
            if len(nums) == 0:
                break
        if int(num) > -1:
            answer = common[0] * int(num)
        else:
            answer = int(common[0] / abs(int(num)))
    return answer


# common = [1, 2, 3, 4]
# common = [4, 3, 2, 1]
# common = [2, 4, 8]
common = [8, 4, 2]
print(solution(common))
