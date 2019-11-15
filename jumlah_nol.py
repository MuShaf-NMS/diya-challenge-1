def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.rstrip().split(' '))
    f.close()
    return data
def pro(a):
    angka = []
    for i in a:
        angka.append(int(i))
    m = max(angka)
    angka.remove(m)
    jmlh = 0
    for i in range(len(angka)):
        jmlh += int(angka[i])
    if m - jmlh == 0:
        return 'YA'
    else:
        return 'Tidak'
data = buka('djn.txt')
for i in range(len(data)):
    print(pro(data[i]))