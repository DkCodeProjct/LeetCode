"""
def towSum(ary,target):
    for i in range(len(ary)):
        for k in range(len(ary)):
            if i != k and ary[i] + ary[k] == target:
                print(f'{ary[i]} + {ary[k]} == {target}')
                return True
    return False
a = [1,2,4,5,6]
t = 8
print(towSum(a,t))


"""
class SolutionTowSum:
    def __init__(self, ary, trgt):
        self.ary = ary
        self.trgt = trgt
    
    def towsum(self):
        for j in range(len(self.ary)):
            for k in range(len(self.ary)):
                if j != k and  self.ary[j] + self.ary[k] == self.trgt:
                    return True
        return False

array = [1,2,3,6,3,5]
target =  8

classSol = SolutionTowSum(array, target)
outPut = classSol.towsum()
print(outPut)