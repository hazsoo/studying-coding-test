def solution(elements):
    l = len(elements)
    sum_set = set()
    
    for i in range(l):
        e = elements[i]
        sum_set.add(e)
        for j in range(i+1, i+l):
            e += elements[j%l]
            sum_set.add(e)

    return len(sum_set)