def solution(n):
    words = n.split()
    
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                
                word[i].upper()
    
    
    return ' '.join(words)

print(solution("try hello world"))