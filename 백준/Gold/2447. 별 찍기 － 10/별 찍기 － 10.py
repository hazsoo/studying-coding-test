n = int(input())

def stars(len):
    if len == 1:
        return ['*']
    
    star = stars(len//3)
    l = []

    for s in star:
        l.append(s*3)
    for s in star:
        l.append(s + ' '*(len//3) + s)
    for s in star:
        l.append(s*3)
    
    return l

print('\n'.join(stars(n)))