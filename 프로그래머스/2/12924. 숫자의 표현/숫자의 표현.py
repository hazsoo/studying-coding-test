def solution(n):
    answer = 1
    for i in range(1, (n//2)+1):
        sum = 0
        k = i
        while sum < n:
            sum += k
            k += 1
        if sum == n:
            answer += 1
    return answer