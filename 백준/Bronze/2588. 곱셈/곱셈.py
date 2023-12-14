import sys
input = sys.stdin.readline
n1 = int(input())
n2 = int(input())
n3 = n1 * (n2%10)
n4 = n1 * ((n2%100)//10)
n5 = n1 * (n2//100)
n6 = n3 + int(str(n4)+'0') + int(str(n5) + '00')
print(n3)
print(n4)
print(n5)
print(n6)