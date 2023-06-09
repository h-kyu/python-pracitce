# word = "Hello"
# word_dict = {char: word.count(char) for char in word} 
# print(word_dict) # Output: {'H': 1, 'e': 1, 'l': 2, 'o': 1} 


# r = tuple(range(1,6))
# print(type(r))
# print(r)

# t = tuple(x for x in range(1, 6))
# print(type(t))
# print(t)

# # 제너레이터 컴프리헨션 예시
# squares_gen = (num ** 2 for num in range(1, 6))
# print(squares_gen)  # 출력: <generator object <genexpr> at 0x7f37f8b32e40>
# print(list(squares_gen))  # 출력: [1, 4, 9, 16, 25]

# 리스트 컴프리헨션을 사용하여 람다 함수 리스트 생성
list = [lambda x: x*2 for x in range(1, 5)]
print(list[0])
print(list[1](4))
print(list[2](6))
print(list[3](8))
