from collections import Counter

def solution(X, Y):
    # 각 숫자의 빈도를 계산
    count_x = Counter(X)
    count_y = Counter(Y)
    
    # 공통 숫자와 빈도를 저장할 리스트
    common_digits = []
    
    # 공통 숫자를 빈도에 맞게 추가
    for digit in count_x:
        if digit in count_y:
            common_digits.extend([digit] * min(count_x[digit], count_y[digit]))
    
    # 가장 큰 수로 배열하기
    common_digits.sort(reverse=True)
    
    # 결과가 0으로만 구성된 경우 0 반환
    if common_digits and common_digits[0] == '0':
        return '0'

    # 공통 숫자가 없는 경우 -1 반환
    if not common_digits:
        return '-1'
    
    # 공통 숫자로 가장 큰 수를 생성하여 반환
    return ''.join(common_digits)