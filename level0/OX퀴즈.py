def solution(quiz):
    answer = []
    for quiz_check in quiz:
        checks = quiz_check.split()
        if checks[1] == "-":
            if int(checks[0]) - int(checks[2]) == int(checks[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(checks[0]) + int(checks[2]) == int(checks[4]):
                answer.append("O")
            else:
                answer.append("X")

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
