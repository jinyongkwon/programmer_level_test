def solution(s):
    s = list(s)
    d = dict()
    for i in range(len(s)):
        if d.get(s[i]) is None:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    answer = sorted([k for k, v in d.items() if v == 1])
    return "".join(answer)


print(solution("abdc"))
