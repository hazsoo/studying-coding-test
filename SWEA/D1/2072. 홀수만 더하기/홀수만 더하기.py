T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    sum = 0
    for i in range(len(num)):
        if num[i] % 2 == 1:
            sum += num[i]
    print("#{} {}".format(test_case, sum))
