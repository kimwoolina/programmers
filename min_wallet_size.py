# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 
# 각 명함은 회전할 수 있습니다. 즉, 명함의 가로와 세로를 바꿀 수 있습니다.

def solution(sizes):
    # 최대 가로 길이와 최대 세로 길이를 초기화
    max_width = 0
    max_height = 0
    
    for width, height in sizes:
        # 명함의 가로와 세로를 정렬하여 가로와 세로가 정해지도록 함
        # 즉, 가로는 항상 더 긴 쪽으로, 세로는 짧은 쪽으로
        w, h = max(width, height), min(width, height)
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    
    # 최종 지갑 크기 계산
    return max_width * max_height


# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 테스트
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133
