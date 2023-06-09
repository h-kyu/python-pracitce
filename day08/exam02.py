# my_list = [('1banana',5),('4apple',1),('2orange',2)]

# sorted_list1 = sorted(my_list, key=lambda x:x[0])
# print(sorted_list1)

# sorted_list2 = sorted(my_list, key=lambda x:x[1])
# print(sorted_list2)

# # 1. 
# calculate_velocity = lambda distance, time: distance/time
# print(calculate_velocity(400,4))
# print(calculate_velocity(500,5))

# # 2.
# is_even = lambda number: number%2==0
# is_even(4)
# is_even(15)

# # 3.
# find_max = lambda num1,num2: max(num1,num2)
# find_max(17, 20)
# find_max(25, 14)

# # 4.
# compare_strings = lambda str1,str2: str1 == str2
# compare_strings("apple","apple")
# compare_strings("apple","banana")

# # 5.
# calculate_sum = lambda numbers:sum(numbers)
# print(calculate_sum([1,2,3,4,5]))

#물체의 위치와 시간을 받아서, 등속 운동하는 물체의 속도를 계산하는 함수를 구현

calculate_velocity=lambda distance,time:round(distance/time,2)

dis=float(input('속도 입력:'))
t=float(input('시간 입력:'))

result=calculate_velocity(dis,t)
print(result)
    
#정수를 받아서 해당 정수가 짝수인지 홀수인지 판별하는 함수를 구현
is_even=lambda number:number%2

num=int(input('정수 입력:'))
if is_even(num)==0:
     print(True)
else:
     print(False)


#두 개의 정수를 받아서, 두 정수 중에서 큰 값을 반환하는 함수를 구현

def universal_func(a,b,func=None):
     if not func:
          return -1
     else:
          return func(a,b)
     
larger=lambda x,y:max(x,y)

a=int(input('정수를 입력:'))
b=int(input('또 다른 정수를 입력:'))

result=universal_func(a,b,func=larger)

#두 개의 문자열 받아서 같은지 비교

same=lambda str1,str2:str1==str2

str_1=str(input('문자열 입력:'))
str_2=str(input('비교문자열 입력'))

if same(str_1,str_2) is True:
    print(True)
else:
    print(False)

#리스트 받아서 모든 숫자의 합을 계산하는 함수 구현

from typing import List

calculate_list=lambda numbers:sum(List[float])

a=[]
n=int(input('리스트 개수 입력:'))
for i in range(n):
    num=input('정수 입력:')
    a.append(num)

print(calculate_list(a))

