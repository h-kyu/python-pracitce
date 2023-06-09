name_lst = []
age_lst = []

# 1.
# for i in range(5):
#     print("{}번째 정보 입력".format(i+1))
#     name = input("이름: ")
#     age = int(input("나이: "))
#     name_lst.append(name)
#     age_lst.append(age)
# print(name_lst, age_lst)

# for i in range(5):
#     print("{}정보".format(i+1))
#     print("이름:",name_lst[i], ", 나이:",age_lst[i])

# 2.
for i in range(5):
    print("{}번째 정보 입력".format(i+1))
    name = input("이름: ")
    age = int(input("나이: "))
    name_lst.append(name)
    age_lst.append(age)
print(name_lst, age_lst)

idx = sorted(range(len(age_lst)), key=lambda k: age_lst[k])

name_lst = [name_lst[i] for i in idx] 
# sorted_list = list(zip(sorted(age_lst), name_lst))
for i in range(5):
    print("{}정보".format(i+1))
    print("이름:",name_lst[i], ", 나이:",sorted(age_lst)[i])

    
# for i in range(5):
#     print("{}정보".format(i+1))
#     print("이름:",name_lst[i], ", 나이:",age_lst[i])


# people = []
# for i in range(5):
#     print("{}번째 정보 입력".format(i+1))
#     name = input("이름: ")
#     age = int(input("나이: "))
#     people.append((name, age))
# print(people)
# # 나이순 정렬
# people.sort(key = lambda x: x[1])
# for i in people:
#     print(i[0], i[1])

