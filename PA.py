def setir(l):
    for i in range(len(l)-1,1,-1):
        for j in range(i):
            if len(l[j]) < len(l+1):
                l[j],l[j+1] = l[j+1],l[j]
def mkstr(l):
    a = l[0]
    for i in range(1,len(l)):
        if l[i] > a:
            a = l[i]
    return a

def com(l):
    r = ''
    p = len(l)
    for i in range(p):
        a = mkstr(l)
        r += a
        l.remove(a)
    return r

l = ['123','234','34','21','2','1','3456','43']
setir(l)
print(l)