class TowSum:
    def __init__(self, ary, targt):
        self.ary = ary
        self.targt = targt
        self.checkedHashTable = {}
    
    def towsum(self):
        for k in range(len(self.ary)):
            num = self.targt - self.ary[k]
            if num in self.checkedHashTable:
                return (self.checkedHashTable[num], k)
            self.checkedHashTable[self.ary[k]] = k
        return None

ary = [1,5,9,3,1,7,2,4]
target = 11
output = TowSum(ary, target)
print(output.towsum()) 