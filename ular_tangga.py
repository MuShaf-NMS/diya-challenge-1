f = open('f_u_t.txt')
l = f.readlines()
data = []
for i in range(1,len(l)):
    data.append(int(l[i]))
db = []
for i in data:
    x = []
    for j in range(1,i*i+1,i):
        y = []
        for k in range(j,j+i):
            y.append(k)
        x.append(y)
    db.append(x)
h = []
for i in range(len(db)):
    t = len(db[i])//2
    a = t-1
    b = t+2
    c = 0
    for j in range(a,b):
        for k in range(a,b):
            if j == t and k == t:
                continue
            c += db[i][j][k]
    h.append(c)
print(h)