def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        l = []
        for x in range(len(arr2[0])):
            sum = 0
            for y in range(len(arr1[0])):
                sum += a1[y] * arr2[y][x]
            l.append(sum)
        answer.append(l)
        
    return answer