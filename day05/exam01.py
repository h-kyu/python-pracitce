# cm = int(input("길이 입력(cm): "))
# print("┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐")
# print(" "*cm,"↑")

# cm = int(input("길이 입력(cm): "))
# print("┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐")

# for i in range(31):
#     print(" ",end='')
#     if i == cm:
#         print("↑")
#         break


# 음악 플레이어를 만들려고 한다. 현재 3분 50초 분량의 노래가 있다.
# 지금까지 진행된 노래 분량을 입력 받아 그림으로 표시하고 몇 % 진행했는지 수치로 나타내는 프로그램을 작성
# time = int(input("재생시간 입력(초): "))
# for i in range(231):
#     print("ㅁ",end='')
#     if i == time:
#         print("{:.1f}%".format((time/230)*100))
#         break

min = int(input('재생시간:'))
per =(min/230)*100
per = round(per)

for i in range(101):
    if i %3==0:
        print('■',end="")
    if per == i :
        print(' %d%%'%per)
        break