n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())
ans = 0
i, j = 0, n - 1

while i < j:
    if arr[i] + arr[j] == x:
        ans += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] > x:
        j -= 1
    elif arr[i] + arr[j] < x:
        i += 1

print(ans)
