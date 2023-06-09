# maintest.py

from mymodule import mysum as ms
import mymodule as mm

result = ms(1,2)
print(result)

result = mm.mymin(10,20)
print(result)