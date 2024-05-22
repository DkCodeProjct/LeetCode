"""
 oh shit ,, leetcode kind of sick y,know. in first few min ive got in my head
 user nested 4 loop., and it works,, then i aked gpt to give instuction, and its 
 told me to use ~ range(len(arry)) ~
 
 ;)

     // even thogh this is just simple one i can enjoy the joy of solving it,,,,,..
     also this could not be the expected behavior..
"""
def check(arys, targert):

    for i in range(len(arys)):
        for k in range(len(arys)):
            if arys[i] != arys[k] and arys[i] + arys[k] == targert:
                print(f'{arys[i]} + {arys[k]} == {targert}')
                return True
    return False

ary = [1,3,3,7,9,2,4,2]

targt = 6

print(check(ary,targt))