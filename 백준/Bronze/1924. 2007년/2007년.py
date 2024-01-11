import sys
input = sys.stdin.readline
x, y = map(int, input().split())

month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

days = 0
for i in range(x-1):
    days += month[i]
days += y
print(day[days%7])