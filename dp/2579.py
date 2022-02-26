# 계단 오르기

import sys

n = int(sys.stdin.readline())
stairs = [0] * (n+1)
for i in range(1, n+1):
    stairs[i] = int(sys.stdin.readline())
dp = [0] * (n+1)

if n == 1:
    print(stairs[1])
    exit()
elif n == 2:
    print(stairs[1] + stairs[2])
    exit()
dp[1] = stairs[1]
dp[2] = stairs[2]+stairs[1]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])