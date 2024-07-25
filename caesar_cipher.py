# "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수

import string

def solution(s, n):
    result = []
    
    for char in s:
        # 공백은 아무리 밀어도 공백
        if char == ' ':
            result.append(' ')
        elif char in string.ascii_uppercase:
            # 'A'~'Z' 범위에서 암호화
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            result.append(new_char)
        elif char in string.ascii_lowercase:
            # 'a'~'z' 범위에서 암호화
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(chr((ord(i)+n)))

    return ''.join(result)



# 테스트
print(solution("AB", 1)) # "BC"
print(solution("z", 1)) # "a"
print(solution("a B z", 1)) # "e F d"
