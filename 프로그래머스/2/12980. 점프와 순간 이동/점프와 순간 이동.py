def solution(n):
    ans = 1
    while n >= 2:
        if n % 2 == 0:
            n /= 2
        else:
            n //= 2
            ans += 1
    return ans