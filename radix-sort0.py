# kafayı kırarak yazdığım Radix Sort algoritması tarzı bir şey...
# amerikayı tekrardan kendi tarzımla keşvettim için ne kadar iyi ne kadar kötü bir yaklaşım bilemiyorum.
# verimli kullanımı için bir ton optimizasyon yapılması gerek. üşengeç herifin önde gideni olduğum için
# string olarak işledim veriyi...

import random
from typing import List

l1: List[int] = [i for i in list(range(10000))]
random.shuffle(l1)

def sort(l1: List[int] = l1 )-> List[int]:

    if type(l1[0]) == int : 
        maxl: int = len(str(max(l1)))
        l1: List[str] = [str(i) for i in l1]
    else: return  

    def d(l1: List[str] = l1) -> List[List[str]]:
        temp: List[List] = [[] for _ in range(maxl)]
        for i in l1: temp[len(i)-1].append(i)

        return temp 


    l1 = d()


    def f(x: List[str], dig: int):
        pars: List[List] = [[] for _ in range(10)]
        for m in range(dig):

            for i in x: pars[int(i[::-1][m])].append(i)
            x: List[int] = pars[0]+ pars[1]+ pars[2]+ pars[3]+ pars[4]+ pars[5]+ pars[6]+ pars[7]+ pars[8]+ pars[9] 
            pars: List[List] = [[] for _ in range(10)]

        return x


    for dig,i in enumerate(l1): l1[dig] = f(i,dig+1) 
     
    return [int(j) for i in l1 for j in i]



print(sort())

