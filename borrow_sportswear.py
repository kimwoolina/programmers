# 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 최대한 많은 학생이 체육수업을 들어야 합니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    # 여벌 체육복을 가진 학생 중에서 도난당한 학생
    # 다른 학생들에게 체육복을 빌려줄 수 없으므로 먼저 처리
    reserve_list = list(set(reserve) - set(lost))
    lost_list = list(set(lost) - set(reserve))
    
    # 체육복을 가진 학생 수 계산
    answer = n - len(lost_list)
    
    # 여벌 체육복을 가진 학생이 체육복을 빌려주는 과정
    for r in sorted(reserve_list):
        if r - 1 in lost_list:  # 앞번호 학생에게 체육복을 빌려줍니다
            lost_list.remove(r - 1)
            answer += 1
        elif r + 1 in lost_list:  # 뒷번호 학생에게 체육복을 빌려줍니다
            lost_list.remove(r + 1)
            answer += 1
    
    return answer
