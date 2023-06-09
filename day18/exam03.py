# try:
#     ret = 4 /0
# except ZeroDivisionError as msg:
#     print('예외: ', msg)


# ret = 0
# try:
#     n = int(input('나눌 숫자 입력: '))
#     ret = 100/n
# except ZeroDivisionError as msg:
#     print('예외:', msg)
# else:
#     print('예외없음')
# print(ret)


# class MyError(Exception):
#     pass

# def valuecheck(n):
#     if n < 0 or n > 100:
#         raise MyError('범위 에러')

# valuecheck(50)
# valuecheck(12)
# try:
#     valuecheck(-1)
# except MyError as msg:
#     print('예외:',msg)
# valuecheck(77)
# valuecheck(101)

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
def valuecheck(n):
    if n < 0 or n > 100:
        raise MyError('범위 에러')

valuecheck(50)
valuecheck(12)
try:
    valuecheck(-1)
except MyError as msg:
    print('예외:',msg)
valuecheck(77)
valuecheck(101)