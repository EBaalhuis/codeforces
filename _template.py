import io, os
from math import *
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))
