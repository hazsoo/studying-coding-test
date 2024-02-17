def solution(n, m, section):
    answer = 0
    wall = [0]*(n+1)
    for s in section:
        wall[s] = 1
    for i in range(len(section)):
        if wall[section[i]] == 1:
            for j in range(section[i], min(section[i]+m, len(wall))):
                wall[j] = 0
            answer += 1
    return answer