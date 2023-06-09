# 1
base_list=[10,17,3,9,27,10,8,9,13,21]

# 2
invert_list =list(reversed(base_list))
print(invert_list)

# 3
even=0
odd=0
print(base_list)
for i in range(len(base_list)):
    if (i+1) % 2 == 0:
        even += base_list[i]
    else:
        odd += base_list[i]
print("짝수번째 합: {}, 홀수번째 합: {}".format(even,odd))

#4
base_list.sort(reverse=True)
sort_list = base_list
print(sort_list)

# 5
base_list=[10,17,3,9,27,10,8,9,13,21]
sort_list = sorted(base_list, reverse=True)
rank_list = []

for i in base_list:
    rank = sort_list.index(i) + 1
    rank_list.append(rank)
print(sort_list)
print(rank_list)


