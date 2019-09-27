f = open('data_arsitek.txt')
List = f.readlines()
def baca_file(l):
  datamentah = []
  data = []
  for i in l:
    datamentah.append(int(i))
  a = []
  for i in range(len(datamentah)):
    if i == 0:
      data.append(datamentah[i])
    elif i >= 1:
      a.append(datamentah[i])
  data.append(a)
  return data
f.close()
def proses(a,b):
  l_baru = []
  lis = []
  i = 0
  for x in range(a):
    if len(b) == i:
      break
    for y in range(b[i]):
      i += 1
      lis.append(b[i])
    i += 1
    l_baru.append(sorted(lis, key=abs))
    lis = []
  return l_baru
def hasil_akhir(a):
  warna = ''
  hasil = []
  for i in range(len(a)):
    w = 0
    warna = ''
    for j in a[i]:
      if j > 0:
        if warna != 'H':
          warna = 'H'
          w += 1
      else:
        if warna != 'B':
          warna = 'B'
          w += 1
    hasil.append(w)
  return hasil
dari_file = baca_file(List)
a = dari_file[0]
b = dari_file[1]
Data = proses(a,b)
hasil = hasil_akhir(Data)
for i in hasil:
  print(i)
