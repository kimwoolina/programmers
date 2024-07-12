# 정수 내림차순으로 배치하기

def solution(n):
    # 정수를 문자열로 변환
    str_n = str(n)
    
    # 문자열을 내림차순으로 정렬
    sorted_str_n = ''.join(sorted(str_n, reverse=True))
    
    # 정렬된 문자열을 다시 정수로 변환하여 반환
    return int(sorted_str_n)

# 예제
print(solution(118372))  # 출력: 873211
