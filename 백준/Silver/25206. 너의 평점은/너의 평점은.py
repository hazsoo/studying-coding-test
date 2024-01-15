import sys
input = sys.stdin.readline

grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

sum_score = 0
sum_point = 0
for _ in range(20):
    s, p, g = input().split()
    p = float(p)
    if g != 'P':
        sum_point += p
        sum_score += p * score[grade.index(g)]

print('{:.6f}'.format(sum_score/sum_point))