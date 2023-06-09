# Q6.
# for i in range(5):
#     for j in range(5):
#         print(i+j+1,end='')
#     print()

# Q7. 
# for i in range(5):
#     for j in range(5):
#         print(5-i+j,end='')
#     print()

# Q8.
# for i in range(1,6):
#     print(i*'*')

# Q9.
# for i in range(5):
#     print((5-i)*'*')

# Q10.
# for i in range(5):
#     print(' '*i, '*'*(5-i))

# Q11.
# for i in range(1,6):
#     print(' '*(5-i), '*'*i)

# Q12.
# for i in range(10):
#     if i > 5:
#         print((10-i)*'*')
#         continue
#     print(i*'*')

# Q13.
# for i in range(1,10):
#     if i > 5:
#         print('*'*(i-4))
#         continue
#     print('*'*(6-i))

# Q14.
# for i in range(1,10):
#     if i > 5:
#         print(' '*(9-i)+'*'*(i-4))
#         continue
#     print(' '*(i-1)+'*'*(6-i))

# Q15.
# for i in range(9):
#     if i > 4:
#         print(' '*(i-4)+'*'*(9-i))
#         continue
#     print(' '*(4-i)+'*'*(i+1))

# Q16.
# for i in range(5):
#     print(' '*(4-i)+'*'*(2*i+1))

# Q17.
# for i in range(5):
#     print(' '*i+'*'*(9-2*i))

# Q18.
# for i in range(9):
#     if i > 4:
#         print(' '*(i-4), '*'*(17-2*i))
#         continue
#     print(' '*(4-i),'*'*(2*i+1))

# Q19.
# for i in range(9):
#     if i > 4:
#         print('*'*(i-3)+' '*(17-2*i)+'*'*(i-3))
#         continue
#     print('*'*(5-i)+' '*(2*i+1)+'*'*(5-i))

# Q20.
# for i in range(9):
#     if i > 4:
#         print('*'*(9-i)+' '*(2*i-7)+'*'*(9-i))
#         continue
#     print('*'*(i+1)+' '*(9-2*i)+'*'*(i+1))

# Q21.
for i in range(9):
    if i > 4:
        print(' '*(8-i)+'*'*(2*i-6))
        continue
    print(' '*(i)+'*'*(9-2*i))