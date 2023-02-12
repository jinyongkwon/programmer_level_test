def solution(my_string):
    li = my_string.split()
    nums = list(map(int, (filter(lambda c: c.isnumeric(), li))))
    symbols = list(filter(lambda c: not c.isnumeric(), li))
    if symbols[0] == "+":
        init = nums[0]+nums[1]
    else:
        init = nums[0]-nums[1]
    for i in range(1, len(nums)-1):
        if symbols[i] == "+":
            init += nums[i+1]
        else:
            init -= nums[i+1]
    return init


print(solution("153 - 153 + 154 - 154 - 1555"))

# 문제 난이도가 0단계는 아닌거 같은데 의도가 eval을 노린거같다.
# 하지만 eval을 사용하지 않고 풀어본 답.
