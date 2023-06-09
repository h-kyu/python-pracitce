def d(a):
    sum=0
    for i in range(len(str(a))):
        sum += int(str(a)[i])
    sum+=a
    return sum

num = list(range(1,5001))
for i in range(1,5001):
    if d(i) in num:
        num.remove(d(i))

sum = 0
for i in num:
    sum+=i
print(sum)

