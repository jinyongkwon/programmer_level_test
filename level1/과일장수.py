def solution(k, m, score):
    answer = 0
    score.append(0)
    score.sort(reverse=True)
    box = []
    for num in score:
        if len(box) == m:
            answer += min(box) * len(box)
            box.clear()
            box.append(num)
        else:
            box.append(num)
    return answer


print(solution(4, 3,  [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
