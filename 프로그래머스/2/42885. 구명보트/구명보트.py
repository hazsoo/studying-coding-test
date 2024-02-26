def solution(people, limit):
    ans = 0
    people.sort()
    left, right = 0, len(people)-1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        ans += 1
    
    return ans