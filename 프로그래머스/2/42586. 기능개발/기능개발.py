def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        cnt = 0
        while True:
            if progresses and progresses[0] >= 100:
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break

        if cnt != 0:
            answer.append(cnt)

    return answer