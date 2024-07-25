# 문자열 리스트를 특정 인덱스 기준으로 정렬하는 함수

def solution(strings, n):
    # 문자열 리스트를 n번째 문자와 전체 문자열을 기준으로 정렬
    sorted_strings = sorted(strings, key=lambda x: (x[n], x))
    return sorted_strings

# 테스트
print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
