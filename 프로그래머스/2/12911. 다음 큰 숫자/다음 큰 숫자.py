def solution(n):
    nbin = format(n, 'b')
    one = nbin.count('1')
    answer = 0
    while True:
        n += 1
        if format(n, 'b').count('1') == one:
            return n