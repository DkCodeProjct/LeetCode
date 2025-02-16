import random

def getOp():
    while True:
        get = input("enter op [ex:- +]: ")
        if get in ["+", "-", "*", "/"]:
            return get
        else:
            print("invalid op to choose")

def func():
    q = 5
    op = getOp()
    
    while q != 0:
        x = random.randint(1, 10)
        y = random.randint(1, 10)     

        while True:  
            ans = input(f"{x} {op} {y} = ")
            if ans.strip() == "" or not ans.lstrip("-").isdigit():
                print("Invalid input! Please enter a number.")
            else:
                ans = int(ans)
                break  
        
        attempt = 0
        if ans != eval(f"{x} {op} {y}"):
            while attempt != 2:  # 3 attempts
                while True:
                    ans = input(f"{x} {op} {y} = ")
                    if ans.strip() == "" or not ans.lstrip("-").isdigit():
                        print("Invalid input! Please enter a number.")
                    else:
                        ans = int(ans)
                        break

                if ans != eval(f"{x} {op} {y}"):
                    print("EEE")
                    attempt += 1
                else:
                    break
        
        if ans == eval(f"{x} {op} {y}"):
            q -= 1  

    return ans  

func()