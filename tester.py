


def ausgabe(a):
    print(a)
    help=a
    help.reverse()
    res = int("".join(str(x) for x in help), 2)
    print(str(res))
    help.reverse()
    return int(res)
def step(t):
    if t[3]^t[2]:

        p=1
    else:
        p=0
    t[3] = t[2]
    t[2]=t[1]
    t[1] = t[0]
    t[0]=p

    return t

def logic():
    a = [0, 1, 0, 0]
    f=[]
    x=0
    while(x<=14):
        f.append(ausgabe(a))
        a=step(a)
        x+=1
    print(f)









logic()