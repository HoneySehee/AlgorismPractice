n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    row, direction, k = map(int, input().split())
    if direction == 0:
        for _ in range(k):
            a[row-1].append(a[row-1].pop(0))
    else:
        for _ in range(k):
            a[row-1].insert(0, a[row-1].pop())
result = 0
row1 = 0
column = n - 1
for i in range(n):
    for j in range(row1, column + 1):
        result+=a[i][j]
    if i < n//2:
        row1 += 1
        column -= 1
    else:
        row1 -= 1
        column += 1
print(result)