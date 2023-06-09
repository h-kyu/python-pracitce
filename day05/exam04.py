# num = int(input("수를 입력하세요: "))
# for i in range(3):
#     print("■"*5)
#     if i == 2:
#             break
#     for j in range(num-1):
#         print("□"*5)
    
# dan = int(input("단을 입력하세요: "))
# print("=== {}단 ===".format(dan))
# for i in range(1,10):
#     print("{} x {} = {}".format(dan,i,dan*i))

# dan = int(input("단을 입력하세요: "))
# print("=== {}단 ===".format(dan))
# for i in range(1,10):
#     print("{} x {} = {}".format(dan,i,dan*i), end =' ')

dan = int(input("단을 입력하세요: "))
print("=== {}단 ===".format(dan))
for i in range(1,10):
    print("{} x {} = {}".format(dan,i,dan*i), end =' ')
    if i == 5:
        print()

print()

for i in range(1,10):
    for j in range(2,10):
        print("{} x {} = {:2d}".format(j,i,i*j),end=" ")
    print()