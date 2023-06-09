a = [13, 24,15,26,55]
a.sort(reverse=True)
print(a)

list1=[2,4,6,8]
list2=[1,3,5,7]
print(id(list1))
list1.extend(list2)
print(list1)
print(id(list1))
list1 = list1 + list2
print(list1)
print(id(list1))

# 리스트 복제
original_list = [1,2,3]
copied_list = original_list.copy()
print(copied_list)
print(id(copied_list))
print(id(original_list))

# 리스트 요소 삭제
numbers=[1,2,3,4,5]
numbers.clear()
print(numbers)