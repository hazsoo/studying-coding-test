def solution(keymap, targets):
    answer = []
    for tg in targets:
        cnt = 0
        for i in range(len(tg)):
            min = 10000
            for km in keymap:
                index = km.find(tg[i])
                if index != -1 and min > index:
                    min = index
            cnt += min+1
        if cnt > 10000:
            cnt = -1
        answer.append(cnt)
    return answer