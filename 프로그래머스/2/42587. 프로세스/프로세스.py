def solution(priorities, location):
    answer = 0
    temp = list(enumerate(priorities))
    
    while temp:
        l, priority = temp.pop(0)
        if any(priority < p for _, p in temp):
            temp.append((l,priority))
        else:
            answer += 1
            if l == location:
                break

    return answer