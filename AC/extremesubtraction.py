t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0
    low = a[0]
    works = True
    for i in range(1, n):
        if a[i] < x:
            print("NO")
            works = False
            break

        next_low = low
        if a[i] - x < low:
            next_low = a[i] - x

        if a[i] - low > x:
            x = a[i] - low

        low = next_low

    if works:
        print("YES")
