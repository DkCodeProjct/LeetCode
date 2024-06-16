class TowSum:
    def __init__(self, ary, target):
        self.h1 = {}
        self.ary = ary
        self.target = target


    def towsum(self):
        for i in range(len(self.ary)):
            value = self.target - self.ary[i]

            if value in self.h1:
                return self.h1[value], i
            self.h1[self.ary[i]] = i
        
        return None