def solution(clothes):
    from collections import defaultdict

    clothe_dict = defaultdict(list)

    # 딕셔너리화
    for clothe in clothes:
        item, category = clothe
        clothe_dict[category].append(item)
    
    # 조합 수 계산
    answer = 1
    for items in clothe_dict.values():
        answer *= (len(items) + 1)  # 각 카테고리에서 의상을 선택하거나 선택하지 않을 경우의 수
    
    # 아무 의상도 선택하지 않는 경우를 제외
    answer -= 1
    
    return answer


# test
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3