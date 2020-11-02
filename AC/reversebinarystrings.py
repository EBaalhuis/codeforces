t = int(input())

for case in range(t):
    n = int(input())
    s = input()

    zeros = 0
    ones = 0

    for i in range(1, len(s)):
        if s[i] == '0' and s[i-1] == '0':
            zeros += 1
        if s[i] == '1' and s[i-1] == '1':
            ones += 1

    print(max(zeros, ones))
