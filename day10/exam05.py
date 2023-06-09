# 실행 후 과목수를 입력 받고 그 수만큼 과목명을 리스트로 생성한다
num = int(input("과목수: "))
subject = []
for i in range(num):
    subject_n = input("과목명 {}: ".format(i+1))
    subject.append(subject_n)

classes =int(input("총 몇반: "))
student = []
for i in range(classes):
    a = int(input("{}반의 학생수: ".format(i+1)))
    student.append(a)

result=[]
for i in range(classes):
    info = []
    for j in range(student[i]):
        info1=[]
        name = input("{}번째 반의 {}번째 사람 이름: ".format(i+1,j+1))
        info1.append(name)
        sum = 0
        for k in range(len(subject)):
            score = int(input("{} = ".format(subject[k])))
            info1.append(score)
            sum+=score
        avg=round(sum/num,2)
        info1.append(sum)
        info1.append(avg)
        info.append(info1)
    result.append(info)
for i in range(classes):
    result[i].sort(key=lambda x: x[4],reverse=True)
for i in range(classes):
    for j in range(student[i]):
        result[i][j].append(j+1)

all = []
for i in range (classes):
    all+=result[i]
all.sort(key=lambda x: x[5],reverse=True)
for i in range (len(all)):
    all[i].append(i+1)
    
print("이름\t", end='')
for j in subject:
    print(j,end='\t')
print("총점\t평군\t반석차\t전교석차")

for i in range(len(all)):
    for j in range(5+num):
        print(all[i][j], end='\t')
    print()
