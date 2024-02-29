from collections import Counter

def solution(k, tangerine):
    answer = 1
    counter = Counter(tangerine)
    values = sorted(list(counter.values()), reverse=True)
    
    sum = 0
    for i in range(len(values)-1):
        sum += values[i]
        if sum >= k:
            return answer
        answer += 1
        
    return answer