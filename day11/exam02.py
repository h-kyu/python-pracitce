# 튜플 생성
base_tup = (32, 12, 54, 22, 76, 77, 45, 44, 77, 54, 32)

# 생성한 튜플의 중복을 제거하여 unique_list이름의 리스트에 저장
base_set = set(base_tup) # set로 중복 제거
unique_list = list(base_set) # 리스트로 변환
print(unique_list)

# 알파벳을 키로 하여 unique_list의 값들을 unique_dict 이름의 딕셔너리로 저장
base_keys = ['A','B','C','D','E','F','G','H']
unique_dict = {}
for i in range(len(unique_list)):
    unique_dict[base_keys[i]]=unique_list[i]
print(unique_dict)

# unique_dict= {}
# n = 65
# for i in range(len(unique_list)):
#     unique_dict[chr(n)] = unique_list[i]
#     n += 1
# print(unique_dict)  

# 딕셔너리에서 값을 기준으로 오름차순으로 정렬하여 sort_tup이름의 튜플에 저장하고 출력
sort_tup = sorted(unique_dict.items(), key=lambda x:x[1])
print(sort_tup)