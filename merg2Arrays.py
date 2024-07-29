"""
def merg(ary0, ary1):
    newList = []
    for i in ary0:
        for j in ary1:
            element = i, j
    newList.append(element)

    return newList
"""
"""
def merg(ar0, ar1):
    ls = []
    for i in ar0:
      
       for j in ar1:
           ls.append(j)
           ls.append(i)
    ls.extend(ar0)
    ls.extend(ar1)
    ls.sort()
    return ls
"""


#
#  None of These Codes didnt full fill the Requred approch for the Answer ..//
#   Must Be using [ linked List [] -> []  ]
# #
def mergArry(ary0, ary1):
    mergList = []
    mergList.extend(ary0)
    mergList.extend(ary1)
    mergList.sort()
    return mergList



l = [1,3,2,1]
ll = [2,4,1,2]
print(mergArry(l,ll))