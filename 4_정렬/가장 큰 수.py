def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) #lambda 인자 : 표현식
    #lambda식과 문자열 sorting을 활용한 방법. 
    #number의 원소는 0이상 1000이하의 숫자이기 때문에 문자형으로 변환한 리스트 원소에 *3을 하게 되면 
    #['666', '101010', '222']를 가지게 되고, 
    #문자열 sorting시 각 원소의 0번째 인덱스의 ascii 값으로 비교하므로 
    #결과는 ['6', '2', '10']이 나오게 됨.
    return str(int(''.join(numbers)))