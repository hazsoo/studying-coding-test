import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print('SK')
elif n == 2:
    print('CY')
elif n == 3:
    print('SK')
elif n == 4:
    print('SK')
else:
    dp = [-1]*(n+1)
    dp[1] = 'SK'
    dp[2] = 'CY'
    dp[3] = 'SK'
    dp[4] = 'SK'
    for i in range(5, n+1):
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
    print(dp[n])