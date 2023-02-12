def solution(s1, s2):
    return sum(1 for s in s1 if s in s2)

# set연산자를 활용한 정답
# len(set(s1)&set(s2));
