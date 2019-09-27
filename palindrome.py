def baca_file(a):
    f = open(a)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.rstrip().split(' '))
    return data
def kata(kt):
    h = 0
    for i in range(len(kt)):
        if kt[i] == ['']:
            continue
        for j in kt[i]:
            a = j
            b = ''
            for k in range(len(j)-1,-1,-1):
                b += j[k]
                if a == b:
                    h += 1
    return h
data = 'data.txt'
Kata = baca_file(data)
hasil = kata(Kata)
print('jumlah kata yang bacaannya sama dari kiri ke kanan dan sebalikny dalam file adalah',hasil)
