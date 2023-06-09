from random import randint

def lotto(n):
    lottonum = []
    for i in range(1,n+1):
        num = []
        while len(num) < 7:
            n = randint(1,45)
            if n not in num:
                num.append(n)
        lottonum.append(num)
    return lottonum

n = int(input("로또 몇회차 목록이 필요한가요: "))

with open("로또.csv",'w') as f:
    title = ["No", "Number1", "Number2", "Number3","Number4", "Number5", "Number6", "Bonus"]
    for i in range(len(title)):
        f.write(title[i]+',')
    f.write("\n")
    a = lotto(n)
    for i in range(len(a)):
        f.write("{},".format(i+1))
        for j in range(7):
            f.write(str(a[i][j])+',')
        f.write("\n")

with open("로또.csv","r") as f:
    data = f.read().split(',')
    count = [0]*45
    for i in data:
        for j in range(1,46):
            if i == str(j):
                count[int(j)-1]+=1
    with open("빈도.csv",'w') as f:
        f.write("Number,Frequency\n")
        for i in range(45):
            f.write("{},".format(i+1))
            f.write("{}".format(count[i]))
            f.write("\n")