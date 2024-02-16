def solution(sequence, k):
    start, end, total = 0, 0, sequence[0]
    sequence += [0]
    first, second = 1000000, 2000000

    while end < len(sequence)-1:
        if total <= k:
            if total == k and end-start < second-first:
                first, second = start, end
            end += 1
            total += sequence[end]
        else:
            start += 1
            total -= sequence[start-1]
    return [first, second]