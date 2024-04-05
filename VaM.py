import copy
import MyWord
class Vector:
    SEP = ','
    def __init__(self, n):
        if isinstance(n, Vector):
            self._data = copy.deepcopy(n._data)
        elif isinstance(n, list):
            self._data = copy.deepcopy(n)
        else:
            assert type(n) is int
            assert n>0
            self._data = [0.0]*n
    def __str__(self):
        comp_list = map(str, self._data)
        s = self.SEP.join(comp_list)
        return '{' + s + '}'
    def __add__(self, other):
        res = copy.deepcopy(self)
        if isinstance(other, Vector):
            assert len(self) == len(other)
            for i in range(len(self)):
                res[i] += other[i]
            # альтернативна реалізація:
            #res = Vector(self)
            #for i in range(len(self._data)):
            #   res._data[i] += other._data[i]
            return res
        else:
            for i in range(len(self)):
                res[i] += other
            return res
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        self._data[j] = val
    def __delitem__(self, j):
        del self._data[j]
    def __len__(self):
        return len(self._data)
    def __radd__(self, other):
        #return self.__add__(other)
        return self + other
    def __mul__(self, other):
        res = copy.deepcopy(self)
        assert (type(other) is int or type(other) is float)
        for i in range(len(self)):
            res[i] *= other
        return res
    def __rmul__(self, other):
        return self * other
class Matrix(Vector):
    SEP = '\n'
    def __init__(self, n):
        super().__init__(n)
    def __call__(self, a = None):
        if a is None:
            if len(self)==1:
                return self[0][0]
            # розкриття по стовпцю або рядку
            det = 0
            for i in range(len(self)):
                #det += (-1)**(0+1 + i+1) * self[0][i] * self( (0,i) )
                det += (-1) ** i * self[0][i] * self((0, i))
            return det
        else:
            i,j = a
            # наприклад, якщо a = (1,2), то стане i==1, j==2
            tmp = Matrix(self) # або через copy.deepcopy(self)
            for k in range(len(self)):
                row = tmp[k]
                del row[j]
            del tmp[i]

            minor = tmp()
            return minor
    def GauseAlg(self):
        Newmatr=copy.deepcopy(self._data)
        n=len(Newmatr)
        Newmatr=Newmatr[0]*(1/Newmatr[0][0])
        for i in range(1, n):
            c=-1.0*Newmatr[i][0]
            hv=c * Newmatr[i-1]
            Newmatr[i]=Newmatr[i]+hv
        return Newmatr

if __name__=="__main__":
    print("Hello, world!")