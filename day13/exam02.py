# #1 로또 당첨 번호를 임의로 100회차 만큼 생성하여 '로또.txt'파일에 저장
# file=open('로또.txt','w',encoding='UTF8')

# from random import randint

# dic={}

# for i in range(1,101):
#     l_n=set()
#     while len(l_n)<7:
#         l_n.add(randint(1,45))
#         dic[i]=l_n
#     file.write(f'{i}번째 로또 번호({l_n})\n')
# file.close()

# #2 '로또.txt'파일을 읽어 들여 각 번호의 빈도를 구하여 '빈도.txt' 파일에 저장
# w_file=open('빈도.txt','w',encoding='utf8')
# with open('로또.txt','r',encoding='utf8') as r_file:
#     r_file.read()
# dic_2={}
# for i in range(1,46):
#     Sum = 0
#     for j in range(1,101):
#         for k in range(7):
#             if list(dic[j])[k] == i :
#                 Sum+=1
#     dic_2[i]=Sum
#     w_file.write(f'{i}번: {Sum}회\n')
    
#     if i%5 ==0:
#         print()

# w_file.close()
# r_file.close()


# #3 '빈도.txt'파일을 읽어 들여 콘솔에 내림차순으로 출력한다.

# r_file_2=open('빈도.txt','r',encoding='utf8')
# r_file_2.read()

# sort_count=reversed(sorted(dic_2.items(),key=lambda x:x[1]))#키 값만 빼려 할 경우에는 그냥 dic만 써주기

# print(list(sort_count))


# #4 출력된 내용에서 빈도가 가장 낮은 수 6개를 오늘 구매한다.
# n=1
# while n<=6:
#     min_sort=min(dic_2,key=dic_2.get)
#     print(f'구매할 번호:{min_sort}')
#     dic_2.pop(min_sort)
#     n+=1

# r_file_2.close()


#===============================================================================================


# #Q1 로또 당첨 번호를 임의로 100회차 만큼 생성하여 txt 파일에 저장

# from random import randint

# lottoNum = []

# def lottoNumCreate() :
#     global lottoNum
#     while len(lottoNum) < 7 :
#         number = randint(1, 45)
#         if number not in lottoNum :
#             lottoNum.append(number)
    
#     return lottoNum

# file = open('로또.txt', 'w')

# lotto_dict = {}

# for i in range(100) :
#     lottoNumCreate()
#     lotto_dict[i+1] = lottoNum
#     lottoNum = []

# for k, v in lotto_dict.items() :
#     for val in v :
#         file.write(f'{val} ')
#     file.write('\n')

# file.close()
    
# #Q2 로또.txt파일을 읽어 각 번호의 빈도를 구해 txt파일에 저장

# file = open('로또.txt', 'r')

# numCnt = [0 for i in range(45)]
# while True :
#     readData = file.readline()
#     num = readData.split()

#     for cnt in num :
#         numCnt[int(cnt)-1] += 1

#     if not readData :
#         break
# file.close()

# # print(sorted(numCnt, reverse=True))

# file = open('빈도.txt', 'w')

# for i in range(len(numCnt)) :
#     file.write(f'{i+1}번 : {numCnt[i]} \n')
#     # print(f'{i+1}번 : {numCnt[i]}', end= '\n')

# file.close()

# #Q3 빈도.txt 파일을 읽어 콘솔에 내림차순으로 출력

# file = open('빈도.txt' , 'r')

# readData_dict = {}
# while True :
#     readData = file.readline()
#     dictData = readData.split()

#     for i in range(len(dictData)) :
#         readData_dict[dictData[0]] = dictData[2]

#     if not readData :
#         break

# file.close()

# sortData = sorted(readData_dict.items(), key = lambda x : int(x[1]), reverse=True)

# for i, j in sortData :
#     print(f'{i} : {j}')


from random import randint

# Q1. 로또 당첨 번호를 임의로 100회차 만큼 생성하여 "로또.txt" 파일에 저장
file_lotto = open("로또.txt", "w", encoding = "utf-8")
file_lotto.write("\t  < 1회 ~ 100회차 로또 당첨 번호 >\n\n")
lotto_numbers = []    
for i in range(1,101):
    number = []
    while len(number) < 7:
        su = randint(1,45)
        if su not in number:
            number.append(su)
    lotto_numbers += number
    file_lotto.write(f"{i}회차 로또번호: {number}\n")
file_lotto.close()
print()

# Q2. "로또.txt"파일을 읽어 들여 각 번호의 빈도를 구하여 "빈도.txt" 파일에 저장
file_lotto = open("로또.txt", "r", encoding= "utf-8")
fre = []
for i in range(1,46):
    fre.append([i, lotto_numbers.count(i)])

file_fre = open("빈도.txt", "w", encoding = "utf-8")
file_fre.write("각 번호의 빈도수\n\n")
for i in range(1,46):
    file_fre.write(f"{i}번 : {fre[i-1][1]}회\n")

file_lotto.close()
file_fre.close()
print()

# Q3. "빈도.txt" 파일을 읽어 들여 콘솔에 내림차순으로 출력한다.
file_fre = open("빈도.txt", "r")
most_fre = sorted(fre, key = lambda x:x[1], reverse = True)
print("================== 각 번호의 빈도수 (로또 번호, 나온 횟수) ==================")
print()
for i in range(1,46):
    if i < 10:
        i = str(i)
        i = "0" + i
    print(f"{i}등: {most_fre[int(i)-1]}", end = "\t")
    if int(i) % 5 == 0:
        print()
print()
print("="*77)

# Q4. 출력된 내용에서 빈도가 가장 낮은 수 6개를 오늘 구매한다.
print()
print("오늘 구매할 숫자 6개는 : ", end = " ")
su = 39
for i in range(6):
    print(most_fre[su][0], end = " ")
    su += 1
print("입니다. (Good Luck!)")
print()
file_fre.close()