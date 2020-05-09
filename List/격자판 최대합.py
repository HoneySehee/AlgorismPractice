n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

result=0

for x in range(n):
    sum1 = sum2 = 0
    for y in range(n):
        sum1 = sum1 + a[x][y]
        sum2 = sum2 + a[y][x]
    if sum1 > result:
        result = sum1
    if sum2 > result:
        result = sum2
sum1 = sum2 = 0

for i in range(n):
    sum1 = sum1 + a[i][i]
    sum2 = sum2 + a[i][n - i - 1]
if sum1 > result:
    result = sum1
if sum2 > result:
    result = sum2

print(result) 
