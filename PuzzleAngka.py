def baca(file):
    f = open(file)
    l = f.readlines()
    data = []
    Data = []
    for i in l:
        data.append(i.strip().split(' '))
    for i in range(len(data)):
        a = []
        for j in range(len(data[i])):
            a.append(data[i][j])
        Data.append(a)
    return Data
def permute(l,head=[],t=[]):
    sz = len(l)
    if sz == 1:
        result = head+l
        t.append(result)
    else:
        for i in range(sz):
            new_head = head.copy()
            new_head.append(l[i])
            new_l = l.copy()
            new_l.pop(i)
            permute(new_l,new_head)
    return t
def com(a,d, t=[],):
    b = len(a)
    if b == d:
        if a not in t:
            t.append(a)
    elif b > d:
        for i in range(b):
            ab = a.copy()
            ab.pop(i)
            com(ab,d)
    return t
def hasil(Data):
    h = []
    for i in range(len(Data)):
        if i % 2 != 0:
            if int(Data[i][0]) == 0:
                h.append(int(Data[i-1][0]))
            else:
                l = int(Data[i - 1][0])
                c = []
                e = []
                f = []
                a = com(Data[i], l)
                for j in a:
                    d = permute(j)
                    for k in d:
                        if k not in c:
                            c.append(k)
                for j in range(len(c)):
                    b = ''
                    for k in range(len(c[j])):
                        b += c[j][k]
                    f.append(b)
                for j in range(len(f)):
                    e.append(int(f[j]))
                h.append(max(e))
    return h
s = ['56','1111','9462']
f = 'file.txt'
b = baca(f)
print(b)
h = hasil(b)
for i in h:
    print(i)
