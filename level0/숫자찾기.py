def solution(num, k):
    answer = str(num).find(str(k))
    return answer if answer == -1 else answer+1
