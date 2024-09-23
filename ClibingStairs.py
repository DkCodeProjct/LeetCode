
#//  * You are climbing a staircase. It takes n steps to reach the top.
#//  Each time you can either climb 1 or 2 steps. 
#//  In how many distinct ways can you climb to the top?
#//  
#//   
#//  Example 1 ==>:
#//      Input: n = 2
#//      Output: 2
#//      Explanation: There are two ways to climb to the top.
#//      1. 1 step + 1 step
#//      2. 2 steps
#//  


class HowManyPath:
    def __init__(self, n):
        self.n = n
        
    def printPathWays(self, n, path):
        if n == 0:
            print(path)
        elif n > 0:
            self.printPathWays(n - 1, path + '1 step ')
            self.printPathWays(n - 2, path + '2 steps ')
    def steps(self):
        self.printPathWays(self.n, '')

input = 4
step = HowManyPath(input)
step.steps()