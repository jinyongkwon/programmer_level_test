def solution(N, stages):
    answer = {}
    deno = len(stages)
    for i in range(1, N+1):
        mole = stages.count(i)
        answer[i] = mole/deno if mole != 0 else 0
        deno -= mole
    test = sorted(answer.items(), key=lambda stage: stage[1], reverse=True)
    answer = [stage[0] for stage in test]
    return answer

# 문제 해답중 test와 answer을 한번에 처리한 방법
# sorted(result, key=lambda x : result[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
