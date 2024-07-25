#  3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 
# 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

def solution(number):
    answer = 0
    length = len(number)
    
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer


# from itertools import combinations

# def solution(number):
#     return sum([1 for c in list(combinations(number,3)) if not sum(c)])

# 테스트 케이스
print(solution([-2, 3, 0, 2, -5])) # 출력: 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 출력: 5
print(solution([-1, 1, -1, 1])) # 출력: 0