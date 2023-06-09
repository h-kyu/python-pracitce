from random import randint
def lottonum(a):
    lotto={}
    for i in range(a):
        lo_v=set()
        while len(lo_v) < 7:
            num=randint(1,45)
            lo_v.add(num)
            lotto[i+1]=lo_v
    for i in range(a):
        print("■{}회차■".format(i+1),end=' ')
        for j in range(7):           
            if j == 6:
                print('bonus:[{}]'.format(list(lotto[i+1])[j]))
            else:
                print(list(lotto[i+1])[j],end=' ')
lottonum(10)
