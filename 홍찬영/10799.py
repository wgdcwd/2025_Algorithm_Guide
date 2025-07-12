arr = input() + "n"
l = len(arr)
stk = 0
ans = 0
i = 0
while i < l - 1:
    if arr[i] == "(":
        if arr[i + 1] == ")":
            ans += stk
            i += 2
        elif arr[i + 1] == "(":
            stk += 1
            ans += 1
            i += 1
    elif arr[i] == ")":
        stk -= 1
        i += 1

print(ans)
