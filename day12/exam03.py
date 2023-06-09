# file_n = input("저장할 파일명: ")
# name = input("이름: ")
# age = int(input("나이: "))
# print("저장되었습니다")


# file = open("{}".format(file_n),"w")
# data = "이름: {}\n나이: {}".format(name,age)
# file.write(data)
# file.close()

# file_c = input("불러올 파일명: ")

# file = open("{}".format(file_c), 'r')
# while True:
#     readData = file.readline()
#     if not readData:
#         break
#     print(readData, end="")
# print()
# print("모두 읽었습니다.")
# file.close

load = input("불러올 파일명:")
file = open(load,"r")
print(file.read())
print("모두읽었습니다")
file.close()