def solution(num, total):
    answer = []
    middle = int(total/num)
    count = int(num/2)
    answer.append(middle)
    if num % 2 == 0:
        for i in range(1, count+1):
            if i != count:
                answer.append(middle-i)
            answer.append(middle+i)

    else:
        for i in range(1, count+1):
            answer.append(middle+i)
            answer.append(middle-i)
    answer.sort()
    return answer


num, total = map(int, input().split())
print(solution(num, total))
