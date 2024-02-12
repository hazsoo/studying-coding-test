def solution(nums):
    l = len(nums)
    nums = set(nums)
    return min(l//2, len(nums))