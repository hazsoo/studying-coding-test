from itertools import product

def solution(word):
    l = []
    g = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1,6):
        for j in product(g, repeat=i):
            l.append(list(j))
        
    l.sort()

    answer = 0
    for i in l:
        answer += 1
        st = ''.join(s for s in i)
        if st == word:
            break

    return answer