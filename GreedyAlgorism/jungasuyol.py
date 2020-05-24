n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0
result = ""
temp = []

while lt <= rt:
    if a[lt] > last:
        temp.append((a[lt], 'L'))
    if a [rt] > last:
        temp.append((a[rt], 'R'))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        result = result + temp[0][1]
        last = temp[0][0]
        if temp[0][1] == 'L':
            lt +=1
        else : 
            rt -=1
    temp.clear()
print(len(result))
print(result)