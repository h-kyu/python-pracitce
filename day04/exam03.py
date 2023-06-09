# 5개의 실수를 입력 받아 최소값과 최대값을 제외한 나머지 점수들의 합계와 평균을 구하시오
a = int(input("점수를 입력하세요: "))
b = int(input("점수를 입력하세요: "))
c = int(input("점수를 입력하세요: "))
d = int(input("점수를 입력하세요: "))
e = int(input("점수를 입력하세요: "))

if a<b and a<c and a<d and a<e:
    min = a
elif b<a and b<c and b<d and b<e:
    min = b
elif c<a and c<b and c<d and c<e:
    min = c
elif d<a and d<b and d<c and d<e:
    min = d
else:
    min = e

if a>b and a>c and a>d and a>e:
    max = a
elif b>a and b>c and b>d and b>e:
    max = b
elif c>a and c>b and c>d and c>e:
    max = c
elif d>a and d>b and d>c and d>e:
    max = d
else:
    max = e
sum = a + b + c + d + e - min - max
avg = sum/3
print("최소값과 최대값을 제외한 점수들의 합:{} 평균:{}".format(sum,avg))
