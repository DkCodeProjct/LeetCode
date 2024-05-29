def towsum(ary, targt):
    checkedHash = {}
    
    for j in range(len(ary)):
        num = targt - ary[j]
        
        if num in checkedHash:
            return (checkedHash[num],j)
        
        checkedHash[ary[j]] = j
    return None

ary = [2,2,1,4,9,3]
target = 7
print(towsum(ary,target))
