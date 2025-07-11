import sys
input = sys.stdin.readline

deq = []


for _ in range(int(input())):
    a = input().rstrip()
    x = 0
    if " " in a:
        a, x = a.split()

    if a == "push_front":
        deq.insert(0, x)
    elif a == "push_back":
        deq.append(x)
    elif a == "pop_front":
        print(deq.pop(0) if deq else -1)
    elif a == "pop_back":
        print(deq.pop(-1) if deq else -1)
    elif a == "size":
        print(len(deq))
    elif a == "empty":
        print(0 if deq else 1)
    elif a == "front":
        print(deq[0] if deq else -1)
    elif a == "back":
        print(deq[-1] if deq else -1)
