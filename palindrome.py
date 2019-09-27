f = open('data.txt')
l = f.readlines()
data = []
h = 0
for i in l:
  data.append(i.rstrip().split(' '))
for i in range(len(data)):
  if data[i] == ['']:
    continue
  for j in data[i]:
    a = j
    b = ''
    for k in range(len(j)-1,-1,-1):
      b += j[k]
    if a == b:
      h += 1
print('jumlah kata yang bacaannya sama dari kiri ke kanan dan sebalikny dalam file adalah',h)

