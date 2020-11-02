t = int(input())

for case in range(t):
    l, r = list(map(int, input().split()))

    if l >= (r+1) / 2:
        print("YES")
    else:
        print("NO")
