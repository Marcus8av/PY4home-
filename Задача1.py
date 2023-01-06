#Вычислить число c заданной точностью d при $d = 0.001, π = 3.141.$
import math
def element(d):
    p = 0
    for i in range(d):
        s = 8*i+1
        p += 1/(16**i)*(4/(s)-2/(s+3)-1/(s+4)-1/(s+5))   
    return p
d = (input().replace(',', '.')).split('.')
d = len(d[1])
print(round(math.pi,d))
print(round(element(d),d))