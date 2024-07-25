# array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# def solution(array, commands):
#     answer = []

#     for cmd in commands:
#         # 부분 배열 추출 및 정렬
#         sub_array = sorted(array[cmd[0]-1:cmd[1]])
#         # k번째 숫자 추출 (인덱스가 0부터 시작하므로 -1)
#         answer.append(sub_array[cmd[2]-1])
    
#     return answer

def solution(array, commands):
    return [sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1] for cmd in commands]

# def solution(array, commands):
#     return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]
