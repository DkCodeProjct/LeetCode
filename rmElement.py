"""
# First Try
def rmVal(ary, val):
    rm = []
    for i in range(len(ary)):
        if i in rm and i == val:
            rm.pop(i)
            
        else:
            rm.append(i)
    return rm
"""

"""
# Second Try
def rmVal(ary, val):
    rm = []
    for j in range(len(ary)):
        if ary[j] != val: # if it's == val dont appent it ignore it ...//
            rm.append(ary[j])
            rm.append('_')
    return rm

l = [1,2,3,2]
v = 2
print(rmVal(l,v))
"""

"""
# Third Try
class RemoveElement:
    def __init__(self, val):
        self.ary = []
        self.val = val
    
    def rmElement(self):
        inputArry = len(self.ary)
        outputAry = []
        for j in range(len(self.ary)):
            if j != self.val:
                outputAry.append(j)
        
        while len(outputAry) < inputArry:
            outputAry.append('_')

        return self.ary
"""



""" ////////////////////// """
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# #
""" ////////////////////// """
# last attempt

class RemoveElement:
    def __init__(self, ary, val) -> list:
        self.ary = ary
        self.val = val

    def rmElement(self):
        inputAry = len(self.ary)
        outputAry = []

        for element in self.ary:
            if element != self.val:
                outputAry.append(element)
        
        while len(outputAry) < inputAry:
            outputAry.append('_')

        return outputAry


if __name__ == "__main__":
    ary = [3, 2, 2, 3]
    val = 3
    rmv = RemoveElement(ary, val)
    modified_ary = rmv.rmElement()
    print(modified_ary)
