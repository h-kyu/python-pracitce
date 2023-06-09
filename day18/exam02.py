class MyStr:
    def __init__(self,str_str):
        self.str_str=str_str
    def size(self):
        return len(self.str_str)
    
class MyStr2(MyStr):
    def upper_count(self):
        counts=0
        for i in self.str_str:
            if i.isupper():
                counts+=1
        return counts

class MyStr3(MyStr2):   
    def lower_count(self):
        counts = 0
        for i in self.str_str:
            if i.islower():
                counts+=1
        return counts

ms1 = MyStr('hello WelcomE!')
print(ms1.size())

ms2 = MyStr2('hello WelcomE!')
print(ms2.size())
print(ms2.upper_count())


ms3 = MyStr3('hello WelcomE!')
print(ms3.size())
print(ms3.upper_count())
print(ms3.lower_count())

# class Mystr:
#     def __init__(self,s):
#         self.s = s
        
#     def size(self):
#         return len(self.s)
        

# class Mystr2(Mystr):
#     def __init__(self, s):
#         super().__init__(s)
        
#     def upper_count(self):
#         count = 0
#         for i in range(len(self.s)):
#             for j in range(65,91):
#                 if self.s[i] == chr(j):
#                     count+=1
#         return count
                
                
# class Mystr3(Mystr2):
#     def __init__(self, s):
#         super().__init__(s)
        
#     def lower_count(self):
#         count = 0
#         for i in range(len(self.s)):
#             for j in range(97,123):
#                 if self.s[i] == chr(j):
#                     count+=1
#         return count
    
# st = "hello WelcomE!"
# ms1 = Mystr(st)
# ms2 = Mystr2(st)
# ms3 = Mystr3(st)

# print(ms1.size())
# print()
# print(ms2.size())
# print(ms2.upper_count())
# print()
# print(ms3.size())
# print(ms3.upper_count())
# print(ms3.lower_count())
