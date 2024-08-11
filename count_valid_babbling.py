# "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 
# 연속해서 같은 발음을 하는 것을 어려워합니다.
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수

def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count


print(solution(["aya", "yee", "u", "maa"]))	# 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))	 #2