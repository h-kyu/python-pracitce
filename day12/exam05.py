#"샘플문서.txt" 파일을 이용하여
#전체 글자 개수(공백 제외), 각 알파벳 개수(대소문자 구분x), 단어의 개수, 각 특수문자 개수(공백제외)를 파악하고
#"결과.txt" 파일을 출력후 가장 많이 사용된 알파벳, 단어, 특수문자를 구해라

import string

# 파일에서 텍스트 읽기
with open("샘플문서.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 전체 글자 개수 (공백 제외)
total_chars = len(text.replace(" ", ""))

# 각 알파벳 개수 (대소문자 구분 없이)
alphabet_counts = {}
for char in text:
    if char.isalpha():
        char = char.lower()  # 대소문자 구분 없이 카운트하기 위해 소문자로 변환
        if char in alphabet_counts:
            alphabet_counts[char] += 1
        else:
            alphabet_counts[char] = 1

# 단어 개수
words = text.split()
word_count = len(words)

# 각 특수문자 개수 (공백 제외)
special_char_counts = {}
for char in text:
    if char in string.punctuation and char != " ":
        if char in special_char_counts:
            special_char_counts[char] += 1
        else:
            special_char_counts[char] = 1

# 결과 파일에 출력
with open("결과.txt", "w", encoding="utf-8") as file:
    file.write(f"전체 글자 개수(공백 제외): {total_chars}\n")
    file.write(f"각 알파벳 개수(대소문자 구분x):\n")
    for char, count in alphabet_counts.items():
        file.write(f"{char}: {count}\n")
    file.write(f"단어 개수: {word_count}\n")
    file.write(f"각 특수문자 개수(공백 제외):\n")
    for char, count in special_char_counts.items():
        file.write(f"{char}: {count}\n")

# 가장 많이 사용된 알파벳, 단어, 특수문자 구하기
most_common_alphabet = max(alphabet_counts, key=alphabet_counts.get)
most_common_word = max(words, key=words.count)
most_common_special_char = max(special_char_counts, key=special_char_counts.get)

print("가장 많이 사용된 알파벳:", most_common_alphabet)
print("가장 많이 사용된 단어:", most_common_word)
print("가장 많이 사용된 특수문자:", most_common_special_char)

# # Q2. "샘플문서.txt" 파일을 이용하여 다음 정보를 파악하시오.

# # 1) 전체 글자 개수(공백 제외)
# f = open("샘플문서.txt", "r")
# st = f.read()

# total_str = len(st.replace(" ",""))
# print(f"전체 글자 개수(공백 제외): {total_str}")
# f.close()
# print()


# # 2) 각 알파벳 개수(대소문자 구분X)
# f = open("샘플문서.txt", "r")
# st = f.read()

# count_alpa = []
# su = 65
# su2 = 97
# print("각 알파벳 개수")
# for i in range(26):
#     print(f"{chr(su2)} : {st.count(chr(su)) + st.count(chr(su2))}개")
#     count_alpa.append([chr(su2), st.count(chr(su)) + st.count(chr(su2))])
#     su += 1
#     su2 += 1

# most_alpa = sorted(count_alpa, key = lambda x: x[1], reverse = True)  
# f.close()
# print()


# # 3) 단어의 개수
# f = open("샘플문서.txt", "r")
# st = f.read()

# words = st.split()
# cnt_word = len(words)
# print(f"단어의 개수: {cnt_word}")

# li2 = []
# for i in set(words):
#     li2.append([i, words.count(i)])

# most_words = sorted(li2, key = lambda x: x[1], reverse = True)
# f.close()
# print()


# # 4) 각 특수문자 개수(공백 제외)
# f = open("샘플문서.txt", "r")
# st = f.read()

# li = []
# for i in st.replace(" ",""):
#     if 65 <= ord(i) <= 90:
#         continue
#     elif 97 <= ord(i) <= 122:
#         continue
#     elif i.isnumeric():
#         continue
#     else:
#         li.append(i)

# use = []
# for i in set(li):
#     use.append([i, li.count(i)])

# print(f"각 특수문자 개수: {use}")
# most_special = sorted(use, key = lambda x: x[1], reverse = True)
# f.close()
# print()

# # 다음 내용을 "결과.txt" 파일에 출력
# f= open("결과.txt", "w", encoding= "utf-8")

# f.write(f"가장 많이 사용된 알파벳은? {most_alpa[0][0]}\n")
# f.write(f"가장 많이 사용된 단어는? {most_words[0][0]}\n")
# f.write(f"가장 많이 사용된 특수문자는? {most_special[0][0]}\n")
# f.close()