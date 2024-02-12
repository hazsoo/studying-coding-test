def solution(nums):
    l = len(nums)
    nums = set(nums)
    if len(nums) <= l//2:
        return len(nums)
    else:
        return l//2