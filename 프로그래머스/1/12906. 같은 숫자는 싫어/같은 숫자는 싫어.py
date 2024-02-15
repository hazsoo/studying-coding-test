def solution(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            res.append(arr[i])
    return res