#
# 
#  .// Time Compexity O(n^2) ,
#   
#   Which is not Good and Expect this is just my first attempt 
#
# # # #

class TreeSum:
    def __init__(self, ary, targt):
        self.ary = ary
        self.targt = targt
    
    def treesum(self):
        for i in range(len(self.ary)):
            for j in range(len(self.ary)):
                for k in range(len(self.ary)):
                    if self.ary[i] != self.ary[j] and self.ary[j] != self.ary[k] and self.ary[i] != self.ary[j] and self.ary[i] + self.ary[j] + self.ary[k] == self.targt:
                        return (i, j, k)
        return None


a = [2,3,6,-1,-2,3,1,5]
t = 8
ts = TreeSum(a, t)
print(ts.treesum())