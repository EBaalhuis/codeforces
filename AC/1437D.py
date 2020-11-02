t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    last = 1
    prev_children = 1
    children = 0
    h = 1

    for i in range(1, n):
        cur = a[i]

        if cur > last:
            children += 1
        else:
            prev_children -= 1
            if prev_children == 0:
                h += 1
                prev_children = children
                children = 0
            children += 1

        last = cur

    print(h)
