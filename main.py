from VaM import *
if __name__=="__main__":
    f = open('inp.txt', "rt")
    lines = f.readlines()
    f.close()
    n=int(lines[0])
    pm=[]
    for i in range(1, n+1):
        l=MyWord.cut(lines[i])
        l=list(map(float, l))
        v=Vector(l)
        pm.append(v)
    M = Matrix(pm)
    mn = M[0][0]
    mx = M[0][0]
    s = 0
    av = 0
    for i in M:
        mn = min(mn, i)
        mx = max(mx, i)
        s += i

    av = s / (len(M) * len(M[0]))
    print(mn, mx)
    print(s, av)