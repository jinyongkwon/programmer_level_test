def solution(s):
    answer = []
    check_dict = {}
    for ch in s:
        if check_dict.get(ch) is None:
            check_dict[ch] = s.index(ch)
            answer.append(-1)
        else:
            index = max(check_dict.values())+1
            result = index - check_dict[ch]
            answer.append(result)
            check_dict[ch] = index
    return answer


print(solution("bananana"))
