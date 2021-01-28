class Matrix:
    def __init__(self,mtr):
        self.mtr = mtr
    def __str__(self):
        return str("\n ".join(map(str,self.mtr)))
    def __add__(self,other):
        sum = []
        for i in range(len(self.mtr)):
            sum.append([])
            for j in range(len(self.mtr[0])):
                sum[i].append(self.mtr[i][j]+other.mtr[i][j])
        return Matrix(sum)
mtr1 = Matrix([[1,2,3],[4,5,6]])
mtr2 = Matrix([[7,8,9],[10,11,12]])
print(mtr1)
print(mtr2)
mtr3 = mtr1+mtr2
print(mtr3)


