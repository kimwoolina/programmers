def kill_max_flies(N, M, grid):
    max_flies = 0
    
    # N=5이고 M=2인 경우, 파리채가 이동할 수 있는 범위는
	# i와 j는 0부터 3까지
    # N − M = 5 − 2 = 3
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            current_flies = 0
            for k in range(M):
                for l in range(M):
                    current_flies += grid[i + k][j + l]
            # k = 0, l = 0: grid[0 + 0][0 + 0] => grid[0][0] = 1
			# k = 0, l = 1: grid[0 + 0][0 + 1] => grid[0][1] = 3
			# k = 1, l = 0: grid[0 + 1][0 + 0] => grid[1][0] = 8
			# k = 1, l = 1: grid[0 + 1][0 + 1] => grid[1][1] = 13
            if current_flies > max_flies:
                max_flies = current_flies
    return max_flies

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    result = kill_max_flies(N, M, grid)
    print(f"#{test_case} {result}")