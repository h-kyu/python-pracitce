alphabet ='abcdefghijklmnopqrstuvwxyz'
special =',.;:\'"()-_+=|~`!@#$%^&*<>?'

def fileopen(data):
    alpha_freq=[0]*26
    special_freq=[0]*len(special)
    with open(data,'r', encoding="utf-8") as file:
        text = file.read().lower()
        splitdata = text.split()
    word_count=[]
    for i in set(splitdata):
        word_count.append([i,splitdata.count(i)])
    word_count.sort(key = lambda x:x[1], reverse = True)

    spe_text = set()
    for i in text:       
        if i in alphabet:
            alph = alphabet.find(i)
            alpha_freq[alph] += 1
        if i in special:
            spe_text.add(i)
            spe = special.find(i)
            special_freq[spe] += 1
    
    return word_count, special_freq, alpha_freq, splitdata, len(splitdata)

def count_character(data): 
    count = 0    
    for i in data :    
        count += len(i) 
    return  count

words, spe_n, alpha_n, data, count_word = fileopen("샘플문서.txt") 

print("공백을 제외한 문자수 : ",count_character(data)) 

print("각 알파벳 개수")
for i in range(len(alphabet)):
    print("{}: {}개".format(alphabet[i],alpha_n[i]))


print("단어의 개수 : ",count_word)

print("각 특수문자 개수")
a = len(special)
while a>0:
    for i in special:
        if spe_n[special.index(i)]==0:
            a-=1
            continue
        else:
            print("{} : {}개".format(i,spe_n[special.index(i)]))
            a-=1

a = alpha_n.index(max(alpha_n))
b = spe_n.index(max(spe_n))

with open("결과.txt",'w') as file:
    data1 = "가장 많이 사용된 알파벳: {}\n".format(alphabet[a])
    data2 = "가장 많이 사용된 특수문자: {}\n".format(special[b])
    data3 = "가장 많이 사용된 특수문자: {}\n".format(words[0][0])
    file.write(data1)
    file.write(data2)
    file.write(data3)