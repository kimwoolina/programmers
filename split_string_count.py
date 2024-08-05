# 주어진 문자열을 첫 문자를 기준으로 x와 다른 문자들의 출현 횟수를 세어 횟수가 같아지는 지점에서 문자열을 분리합니다. 
# 이 과정을 반복하여 최종적으로 분리된 문자열의 개수를 반환합니다.

def solution(s):
    count = 0
    while s:
        x = s[0]
        x_count = 0
        other_count = 0
        index = 0
        
        # 문자열을 순회하며 x와 다른 문자의 횟수를 센다
        for char in s:
            if char == x:
                x_count += 1
            else:
                other_count += 1
            
            index += 1
            if x_count == other_count:
                break
        
        # 현재까지 읽은 부분을 문자열에서 제거
        s = s[index:]
        count += 1
    
    return count
