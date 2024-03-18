def solution(n):
    answer = 1
    while n >= 2:
        if n % 2 == 0:
            n /= 2
        else:
            n //= 2
            answer += 1
            
    return answer