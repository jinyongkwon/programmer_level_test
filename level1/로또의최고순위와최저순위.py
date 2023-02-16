def solution(lottos, win_nums):
    count = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            count += 1
    return [rank[count + zero_count], rank[count]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
