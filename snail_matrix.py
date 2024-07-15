# [제약사항] 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

T = int(input())

# 달팽이 배열을 생성하는 함수
def create_snail(N):
    snail = [[0]*N for _ in range(N)]
    num = 1
    x, y = 0, 0
    dx, dy = 0, 1

    while num <= N*N:
        snail[x][y] = num
        num += 1
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy

    return snail

for test_case in range(1, T + 1):
    N = int(input())
    snail = create_snail(N)

    print(f"#{test_case}")
    for row in snail:
        print(' '.join(map(str, row)))
