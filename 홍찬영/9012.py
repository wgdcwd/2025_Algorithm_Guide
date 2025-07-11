n = int(input())
for _ in range(n):
    s = input()
    cnt = 0
    ans = True
    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            ans = False
            break

    if ans:
        if cnt == 0:
                print("YES")
        else:
            print("NO")
    else:
        print("NO")
