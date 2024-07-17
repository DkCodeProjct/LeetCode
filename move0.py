"""
..// first attempt

def move0(ary):
    #move = []
     
    move = []
    for i in range(len(ary)):
        move.append(i)
        if i == 0:
            move.pop(i)
            move.append(i)
        else:
            continue
    return move
"""

#
# 
#  Time Complexity would be O(n^2).  
#  Not Efficent
# #




def move0(ary):
    move = []
    
    for i in range(len(ary)):
        if ary[i] != 0:
            move.append(ary[i])
    
    for j in range(len(ary)):
        if ary[j] == 0:
            move.append(ary[j])
    
           
    return move

nums = [0,1,0,3,12]
# Expected output = [1,3,12,0,0]
print(move0(nums))
    