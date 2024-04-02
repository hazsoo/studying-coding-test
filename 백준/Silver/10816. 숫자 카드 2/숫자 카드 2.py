from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

counter = Counter(cards)

for n in nums:
    print(counter[n], end=' ')