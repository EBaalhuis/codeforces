t = int(input())

for case in range(t):
    n = int(input())

    arr = [2*n + 2*i for i in range(n)]
    print(str(arr)[1:-1].replace(',',''))
