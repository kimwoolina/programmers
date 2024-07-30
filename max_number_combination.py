# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수

import functools

def custom_compare(n1, n2):
    num1 = str(n1)
    num2 = str(n2)
    return int(num1 + num2) - int(num2 + num1)

def largest_number(numbers):
    sorted_numbers = sorted(numbers, key=functools.cmp_to_key(custom_compare), reverse=True)
    largest = "".join(map(str, sorted_numbers))
    return largest

def solution(numbers):
    return largest_number(numbers)


# test
print(solution([6, 10, 2]))	# "6210"
print(solution([3, 30, 34, 5, 9]))	# "9534330"