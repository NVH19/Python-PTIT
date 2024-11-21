d = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
sum = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                x, y = i + d[k][0], j + d[k][1]
                if x >= 0 and x < n and y >= 0 and y < m and not visited[x][y]:
                    sum += a[x][y]
                    visited[x][y]=1
print(sum)
            