import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    word = input().split()
    print("Case #{}:".format(i+1), *word[::-1])