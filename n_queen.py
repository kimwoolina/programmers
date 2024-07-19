def nqueen(n):
    """
    visited 의 인덱스는 행, 값은 열을 나타낸다.
    퀸을 (1, 3)에 놓은 경우, visited[1] = 3 으로 표현하겠다는 것.
    (어차피 퀸들을 같은 행, 열에 둘 수 없으므로 이렇게 1차원 배열로도 표현할 수 있다.)

    예시) n=4 이고 visited = [1, 3, 0, 2] 인 경우,
    체스판을 그려보면 아래와 같다. (1이 퀸)
    0 1 0 0
    0 0 0 1
    1 0 0 0
    0 0 1 0
    
    
    """
    visited = [-1] * n
    cnt = 0 # 퀸 배치 경우의 수 # 출력 시 사용
    answers = []

	# 이 row가 퀸을 둘 수 있는 장소인지 확인
    # 백트래킹의 핵심 부분인 코드
    def is_ok_on(nth_row):
        """
        n번째(nth) 행에 퀸을 놓았을 때, 올바른 수인지 검사한다.
        nth 행의 퀸 위치와, 0번째 행부터 n-1번째 행까지 놓여진 퀸의 위치를 비교한다.
        nth 행에 놓여진 퀸이 규칙을 깼다면 False 를 반환한다.
        """
        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.
        # 영상에서 n-1이라고 말하는데 오류입니다. nth_row-1까지 살펴봅니다.
        for row in range(nth_row):
            # 방금 놓여진 nth 퀸은 (nth_row, visited[nth_row]) 에 놓여져있다.
            # 각 행에 차례대로 단 한 번만 두기 때문에 행이 겹치는 것은 검사하지 않아도 된다.
            # 1) 열 번호가 겹치지는 않는지? visited[nth_row] == visited[row]:
            # 2) 또는 대각선으로 존재하지는 않는지? nth_row - row == abs(visited[nth_row] - visited[row]) 살펴본다.
            # nth_row - row == abs(visited[nth_row] - visited[row]) ➡️ x좌표의 차이 == y값의 좌표의 차이
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    # 퀸을 배치하는 함수
    def dfs(row):
        """
        row 는 퀸을 놓을 행번호를 의미한다.
        dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
        dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
        ...
        dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
        따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.
        """

        #
        # 0 ~ n-1 행에 퀸을 모두 하나씩 두었을 때 경우의 수를 1 증가시키고 재귀탐색을 종료한다.
        if row >= n:
            # nonlocal 은 지역변수가 아님을 의미한다.
            nonlocal cnt
            cnt += 1
            print("*" * 80)
            print(f"{cnt}번째 답 - visited: {visited}")
            # 모든 요소가 '.' 인 n길이의 리스트 만듦
            grid = [['.'] * n for _ in range(n)]
            # 퀸이 있는 자리에 Q넣어줌
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                # 마지막에 한꺼번에 출력하기 위한 과정  
                # ['.', 'Q', '.', '.'] => '.Q..'
                result.append(''.join(row))
            # answer: 가장 마지막 출력이 될 부분
            answers.append(result)
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n): 
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            visited[row] = col
            # 백트래킹!
            if is_ok_on(row):
                dfs(row + 1)

    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers

print(nqueen(4))