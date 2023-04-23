a = [int(x) for x in input().split()]

result = list()

for i in range(len(a)-1):
    result.append(a[i-1]+a[i]+a[i+1])
result.append(a[-1]+a[-2]+a[0])
print(max(result))
