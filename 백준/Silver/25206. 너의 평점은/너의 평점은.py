import sys
input = sys.stdin.readline

sum_score = 0
sum_grade = 0
for _ in range(20):
    grade = input().split()
    grade[1] = float(grade[1])
    if grade[2] != 'P':
        sum_grade += grade[1]
    if grade[2] == 'A+':
        sum_score += grade[1] * 4.5
    elif grade[2] == 'A0':
        sum_score += grade[1] * 4.0
    elif grade[2] == 'B+':
        sum_score += grade[1] * 3.5
    elif grade[2] == 'B0':
        sum_score += grade[1] * 3.0
    elif grade[2] == 'C+':
        sum_score += grade[1] * 2.5
    elif grade[2] == 'C0':
        sum_score += grade[1] * 2.0
    elif grade[2] == 'D+':
        sum_score += grade[1] * 1.5
    elif grade[2] == 'D0':
        sum_score += grade[1] * 1.0
    elif grade[2] == 'F':
        sum_score += grade[1] * 0.0
    else:
        continue
print('{:.6f}'.format(sum_score/sum_grade))