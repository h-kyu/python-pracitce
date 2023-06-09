from random import randint

lotto=[]
for i in range(100):
    lottonum = set()
    while len(lottonum) < 7:
        num = randint(1,45)
        lottonum.add(num)
    lotto.append(list(lottonum))

with open("로또.txt",'w') as file:
    for i in range(len(lotto)):
        for j in range(7):
            data = lotto[i][j]
            file.write("{} ".format(data))
        file.write("\n")

with open("로또.txt", 'r') as file:
    num = file.read().split()
    num_lst = [x for x in range(1,46)]
    num_dict = {}
    count = [0]*45
    for i in range(len(num)):
        for j in num_lst:
            if int(num[i]) == j:
                count[j-1]+=1
    for i in num_lst:
        num_dict[i]=count[i-1]
    with open("빈도.txt",'w') as file:
        for round, num in num_dict.items():
            file.write(f"{round}번 : {num} 회 \n") 

with open("빈도.txt",'r') as file:
    a = file.read().split()
    i = 0
    round_dict = {}
    while i < len(a):
        round_dict[a[i]] = int(a[i+2])
        i += 4
    round_dict1= dict(sorted(round_dict.items(), key=lambda x: x[1], reverse=True))
    for round, num in round_dict1.items():
        print(f"{round} : {num}회 ") 
    round_k = list(round_dict1.keys())
    print("빈도가 가장 낮은 수 6개: ",end='')
    for i in range(6):
        print(round_k[44-i],end=' ')
