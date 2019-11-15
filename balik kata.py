def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.rstrip().split(' '))
    f.close()
    return data
def pal(kata):
    h = ''
    for i in range(len(kata)-1,-1,-1):
        h += kata[i]
    return h
data = buka('dbk.txt')
r = []
for i in range(len(data)):
    h = ''
    for j in range(len(data[i])):
        h += pal(data[i][j])
        h += ' '
    r.append(h)
for i in r:
    print(i)