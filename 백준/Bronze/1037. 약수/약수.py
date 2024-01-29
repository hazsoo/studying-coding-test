c = int(input())
n = list(map(int, input().split()))

print(min(sorted(n)) * max(sorted(n)))