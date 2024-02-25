def solution(n, words):
    w = [words[0]]
    turn = 1
    for i in range(1, len(words)):
        if i % n == 0:
            turn += 1
        if w[-1][-1] != words[i][0]:
            return [(i % n)+1, turn]
        if words[i] not in w:
            w.append(words[i])
        else:
            return [(i % n)+1, turn]
    return [0,0]