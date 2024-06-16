"""
TIME COMPLEXITY

//  O(n^2)

"""


def ts(ary, target):
    
    for i in range(len(ary)):
        for k in range(len(ary)):
            if ary[i] != ary[k] and ary[i] + ary[k] == target:
                return ary[i] ,ary[k]
    return None
ary = [1,3,4,5,2]
target = 7
print(ts(ary,target))


class TowSum:
    def __init__(self):
        self.ary = [1,4,2,5,8,3]
        self.target = 12
    
    def towsum(self):
        for i in range(len(self.ary)):
            for k in range(len(self.ary)):
                if self.ary[i] != self.ary[k] and self.ary[i] + self.ary[k] == self.target:
                    return f'{self.ary[i]} + {self.ary[k]}\nbecause {i} + {k} == {target}'
        return None
    

output = TowSum()
print(output.towsum())