def solution(array, commands):
    answer = []
    for i in commands:
        temp = array[i[0] - 1:i[1]]
        temp.sort()
        temp = temp[i[2] - 1]
        answer.append(temp)
    return answer