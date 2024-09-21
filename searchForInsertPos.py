

#// Given a sorted array of distinct integers and a target value, 
#// return the index if the target is found. If not, 
#// return the index where it would be if it were inserted in order.

#// Input: nums = [1,3,5,6], target = 5
#// Output: 2



class SearchForInsert:
    def __init__(self, ary):
        self.ary = ary

    def searchInsert(self, targt):
        left = 0
        right = len(self.ary) - 1
       

        while left <= right:
            mid = (left + right) // 2 # Mid should be inside while loop 
            if self.ary[mid] == targt: # cos it has to be update evry time
                return mid
            
            elif self.ary[mid] < targt:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return left
    

arry = [1, 2, 3, 4, 5, 7, 8] 
search = SearchForInsert(arry)
targt = search.searchInsert(6)
print(targt)

# Enjoy Coding this
# cs50.ai.ddb Helped me