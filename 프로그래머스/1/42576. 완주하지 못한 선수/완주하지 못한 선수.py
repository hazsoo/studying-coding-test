from collections import defaultdict

def solution(participant, completion):
    answer = ''
    pd = defaultdict(lambda: 0)
    for p in participant:
        pd[p] += 1
    pd = dict(pd)
    
    for c in completion:
        pd[c] -= 1
        if pd[c] == 0:
            pd.pop(c)
        
    for key in pd.keys():
        answer += key
    return answer