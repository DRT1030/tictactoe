def ketupat(x):
    d = int(x/2); y = 0; g = x-1
    while (y <= g): print(" "*g + "*@"*y + "*"*1);y += 1;g-=1; 
    while (d >= 0): print(" "*g + "*@"*d + "*"*1); d -= 1; g +=1
ketupat(20)


def kotak(x):
    y = 2*x-1; g = 2*x-2; d = 0
    if (x >= 3):
        d += 2*(x-2)-1
    for i in range(y):
        if (i % 2 == 1):
            if(i > 1 and i < (g-1)): print("*@*" + "@" + "*@*")
            else: print("*"+"@"*(y-2)+"*");
        elif(i%2 == 0):
            if (i > 0 and i < g ): print("*@" + "*" + "@*"); pass
            else: print("*"*y);
        
    print("-----------")
          

def kotak2(x):
    y = 2*x-1
    l = 0
    p = 0
    if x > 1: g = x-1;
    if x > 2: l += 2*(x-2); p += x-2
    for i in range(y):
        if i % 2 == 0:
            if i > 0 and i < l+1: print("*@"+"*"*p+"@*")
            
            else:print("*"*y)
        elif i % 2 == 1:
            if i > 1 and i < y-2: print('*@'*g + '*')
            else: print('*@' + '@'*l + '*')
        
    print("-------")


"""
def kotak3(niter):
    val = "@"
    c1 = '*'
    c2 = '@'
    for i in range(niter):
        c = c1 if i % 2 == 0 else c2
        val = f"{(i+2)*c}\n{c}{val}{c}\n{(i+2)*c}"
    print(val)
"""

kotakx = kotak2
kotakx(1)
kotakx(2)
kotakx(3)
kotakx(4)
kotakx(5)
kotakx(6)
kotakx(7)
kotakx(8)
kotakx(9)


