from collections import defaultdict

def solution(clothes):
    answer = 1
    temp = []
    for cloth in clothes:
        temp.append(cloth[1])
        
    dic_temp = defaultdict(lambda: 0)
    for t in temp:
        dic_temp[t] += 1
        
    values = list(dict(dic_temp).values())
    for v in values:
        answer *= v+1
    
    return answer - 1