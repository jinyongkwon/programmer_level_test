from collections import deque


def solution(A, B):
    answer = 0
    print(B*2)
    A = deque(A)
    B = deque(B)
    for _ in range(len(A)):
        if A == B:
            break
        A.appendleft(A.pop())
        answer += 1
        if _ == len(A)-1:
            answer = -1
    return answer


A, B = input().split()
print(solution(A, B))
