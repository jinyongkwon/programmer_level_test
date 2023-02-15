def solution(food):
    answer = []
    for i in range(1,len(food)):
        if food[i] %2 != 0:
            food[i] -=1
        for _ in range(food[i]//2):
            answer.append(i)
    answer = list(map(str, answer))
    fisrt = "".join(answer)
    answer.sort(reverse=True)
    last = "".join(answer)
    return f"{fisrt}0{last}"


print(solution([1,3,4,6]))