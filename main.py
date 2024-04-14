from VaM import *
if __name__=="__main__":
    f = open('inp.txt', "rt")
    lines = f.readlines()
    f.close()

    M = Matrix(int(lines[0]))
    lines = lines[1:]
    for i in range(len(M)):
        l=MyWord.cut(lines[i])
        l=list(map(float, l))
        M[i] = Vector(l)

    mn=M[0][0]
    mx=M[0][0]
    s=0
    av=0
    for i in M:
        mn=min(mn, i)
        mx=max(mx, i)
        s+=i

    av=s/(len(M)*len(M[0]))
    print(mn, mx)
    print(s, av)