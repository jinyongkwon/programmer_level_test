def solution(babbling):
    answer = 0
    baby_languages = ['aya', 'ye', 'woo', 'ma']
    for txt in babbling:
        for language in baby_languages:
            if language in txt:
                txt = txt.replace(language, "*")
        txt = set(txt)
        if len(txt) == 1 and "*" in txt:
            answer += 1
    return answer


# babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))
