# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수 구하기

from itertools import combinations
import math

def primenumber(x):
    # 2부터 x의 제곱근까지의 숫자 (에라토스테네스의 체)
    for i in range (2, int(math.sqrt(x) + 1)):
        # 나눠떨어지는 숫자가 있으면 소수가 아님
        if x % i == 0:
            return False
    return True	


def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        if primenumber(sum(i)):
            answer += 1

    return answer

print(solution([1,2,3,4]))	#1
print(solution([1,2,7,6,4]))	#4