from collections import deque

# 정답
"""
def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)
"""


def solution(s):
    answer = ''
    dq = deque(s)
    txt = ""
    txt_list = []
    s = 0
    for _ in range(len(dq)):
        char = dq.popleft()
        if char == " ":
            s += 1
            if txt != "":
                txt_list.append(txt)
            if len(dq) == 0:
                txt_list.append(s)
            txt = ""
        else:
            txt += char
            if s > 0:
                txt_list.append(s)
            if len(dq) == 0:
                txt_list.append(txt)
            s = 0

    for i in range(len(txt_list)):
        txt = txt_list[i]
        if type(txt) == int:
            txt_list[i] = " " * txt
        else:
            if txt != "" and txt[0].isalpha():
                txt_list[i] = txt.title()

    answer = "".join(txt_list)
    # if char == " ":
    #     if txt[0].isalpha():
    #         answer += txt.title() + char
    #         txt = ""
    #     else:
    #         answer += txt + char
    #         txt = ""
    # else:
    #     txt += char

    # s_list = s.split(" ")
    # for i in range(len(s_list)):
    #     if not s_list[i][0].isalpha():
    #         pass
    #     else:
    #         s_list[i] = s_list[i].title()
    # answer = " ".join(s_list)
    print("")
    return answer


s = input()
print(solution(s))
