def solution(s, skip, index):
    answer = []
    a, z = ord("a"), ord("z")
    chars = [i for i in range(a, z+1) if not chr(i) in skip]
    for ch in s:
        count = (chars.index(ord(ch))+index) % len(chars)  # 범위를 벗어나지 않게끔 함.
        answer.append(chr(chars[count]))
    return "".join(answer)


print(solution("aukks", "wbqd", 5))

# ord() => string to ascii
# chr() => ascii(int) to string
