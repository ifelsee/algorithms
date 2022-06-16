# kafayı kırarak yazdığım Radix Sort algoritması tarzı bir şey...
# amerikayı tekrardan kendi tarzımla keşvettim için ne kadar iyi ne kadar kötü bir yaklaşım bilemiyorum.
# verimli kullanımı için bir ton optimizasyon yapılması gerek. üşengeç herifin önde gideni olduğum için
# string olarak işledim veriyi................a.sdfasd............asdf.as..


import random

l1 = [i for i in list(range(9001))]
maxl = len(str(max(l1)))
l1 = [str(i) for i in l1]
random.shuffle(l1)


def sort(l1 = l1):  
    def d(l1=l1):
        temp = [[] for _ in range(maxl)]
        for i in l1: temp[len(i)-1].append(i)

        return temp 


    l1 = d()


    def f(x, dig ):
        pars = [[] for _ in range(10)]
        for m in range(dig):

            for i in x: pars[int(i[::-1][m])].append(i)
            x = pars[0]+ pars[1]+ pars[2]+ pars[3]+ pars[4]+ pars[5]+ pars[6]+ pars[7]+ pars[8]+ pars[9] 
            pars = [[] for _ in range(10)]

        return x


    for dig,i in enumerate(l1): l1[dig] = f(i,dig+1) 
    for i in l1: [print(j) for j in i]
    
    return l1

(sort())
