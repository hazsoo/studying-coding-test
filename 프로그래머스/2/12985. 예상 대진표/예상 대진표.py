def solution(n,a,b):
    ans = 1
    match = n // 2
    game_a = (a+1) // 2
    game_b = (b+1) // 2
    
    while game_a != game_b:
        a = game_a
        b = game_b
        game_a = (a+1) // 2
        game_b = (b+1) // 2
        ans += 1
        match //= 2
        
    return ans