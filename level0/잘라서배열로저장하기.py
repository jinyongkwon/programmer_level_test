def solution(my_str, n):
    answer = []
    end_index = 0
    while len(my_str) > end_index:
        start_index = end_index
        end_index = start_index+n
        answer.append(my_str[start_index:end_index])
    return answer


solution("abc1Addfggg4556b", 6)
