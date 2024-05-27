# // remove duplicant from the ary

"""
    // this is just a psudocode for the problem.
    i think i didnt properly implement the hash Table #
"""

def rm(ary):
    h1 = {}
    for j in range(len(ary)):
        if ary[j] in h1:
            continue
        h1[ary[j]] = True
    return list(h1.keys())

k = [2,0,4,9,5,9,5]
print(rm(k))

class Rm:
    def __init__(self):
        self.h1 = {}
    def remove(self,ary):
        for j in range(len(ary)):
            if ary[j] in self.h1:
                continue
            self.h1[ary[j]] = True
        return list(self.h1.keys())