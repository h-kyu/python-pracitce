# 컴프리헨션(리스트, 집합, 딕셔너리)을 사용하여 
# 각각 홀수 숫자, 제곱수, 숫자와 제곱수 쌍을 생성하는 프로그램

# 리스트 컴프리헨션을 사용하여 1 ~ 100사이의 홀수 숫자 리스트 생성
odd_numbers = [odd for odd in range(1,100) if odd%2==1]
print("Odd numbers:", odd_numbers)
"""
결과:
Odd numbers: [1, 3, 5, 7, 9, 11, 13, 
15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 
35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 
55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 
75, 77, 79, 81, 83, 85, 87, 
89, 91, 93, 95, 97, 99]
"""

# 집합(Set) 컴프리헨션을 사용하여 1 ~ 10까지의 제곱수 집합(Set) 생성
squares = {square**2 for square in range(1,11)}
print("Squares:", squares)
"""
결과:
Squares: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
"""
# 딕셔너리 컴프리헨션을 사용하여 15 ~ 25사이의 숫자와 제곱수 쌍의 딕셔너리 생성
number_square_pairs = {square : square**2 for square in range(15,26)}
print("Number-Square pairs:", number_square_pairs)
"""
결과:
Number-Square pairs: {15: 225, 16: 256, 17: 289, 
18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 
23: 529, 24: 576, 25: 625}
"""

# [1, 2, 3, 2, 4, 2, 5] 리스트에서 index()함수를 활용하여 
# 값 2의 모든 인덱스를 리스트로 생성
my_list = [1, 2, 3, 2, 4, 2, 5]
search_value = 2
indices = [i for i in range(len(my_list)) if my_list[i] == search_value]
print("indices: ", indices) 
"""
결과:
indices: [1, 3, 5]
"""

