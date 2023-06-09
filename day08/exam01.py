# # 인자로 N을 전달하면 N에 대한 팩토리얼을 반환하는 함수(재귀)

fact = 1
def factorial(N):
    global fact
    if N == 0:
        return fact
    fact *= N
    N -= 1
    factorial(N)
n = int(input("수 입력: "))
print(factorial(n))

# # 인자로 N을 전달하면 거꾸로 만든 수를 반환하는 함수(재귀) 

# num = ''
# def back(N):
#     global num
#     if N == 0:
#         return
#     num += str(N%10)
#     N //= 10
#     back(N)
#     return num

# a= int(input("팩토리얼 변환:"))
# result = 1
# def fac(a):
#     global result
#     result = result*a
#     a = a-1

#     if a == 1:
#         print(result) 
#         return
#     fac(a)
# fac(a)

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fac(n-1)
# n = int(input("수입력: "))
# print(fac(n))