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

    print(M.det())
    f=open('res.txt', "wt")
    N=M.inverse()
    print(len(N), file=f)
    for i in range(len(N)):
        v=N[i]
        print(*v._data, file=f)
    f.close()