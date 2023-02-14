# 제일 깔끔한 정답
# 내가 푼 방법중 반복되는 메서드를 간단하게 구현
"""
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
"""


def solution(k, score):
    answer = []
    hof = []
    for num in score:
        if k > len(hof):
            hof.append(num)
            answer.append(min(hof))
        else:
            if num > min(hof):
                del hof[hof.index(min(hof))]
                hof.append(num)
                answer.append(min(hof))
            else:
                answer.append(min(hof))
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
