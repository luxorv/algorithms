
while True:

    queries = int(input())

    if queries == 0:
        break

    m, n = map(int, input().split())

    for i in range(queries):
        x, y = map(int, input().split())

        if x == m or y == n:
            print('divisa')

        elif x > m and y > n:
            print('NE')
        elif x > m and y < n:
            print('SE')
        elif x < m and y > n:
            print('NO')
        elif x < m and y < n:
            print('SO')
