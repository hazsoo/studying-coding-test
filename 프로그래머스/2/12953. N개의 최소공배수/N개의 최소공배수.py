def solution(arr):
    ans = 1
    for a in arr:
        ans = lcm(ans,a)
    return ans
    
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    return x * y // gcd(x,y)