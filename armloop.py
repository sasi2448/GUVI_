n,m= raw_input().split()
n=int(n)
m=int(m)

for i in range(n,m):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum =sum+digit ** 3
        temp=temp//10
    if i==sum:
        print i
