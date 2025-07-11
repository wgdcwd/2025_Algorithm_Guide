n, m = map(int, input().split())

arr = list(map(int, input().split()))

que = [i + 1 for i in range(n)]
head = 0
ans = 0

for i in range(m):
    target_ind = que.index(arr[i])
    diff = abs(target_ind - head)
    ans += min(diff, len(que) - diff)
    head = target_ind
    que.pop(head)

    if que:
        head = head % (len(que))
    else:
        head = 0

print(ans)
