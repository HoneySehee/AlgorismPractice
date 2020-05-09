n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

result = 0

row=col=n//2

for x in range(n):
    for y in range(row, col+1):
        result += a[x][y]
    
    if x < n // 2:
        row -= 1
        col += 1
    else:
        row += 1
        col -= 1

print(result)