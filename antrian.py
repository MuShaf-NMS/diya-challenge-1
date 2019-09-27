antri = [1,2,3,4,5,6,7,8,9,10]
waktu = [2,3,3,7,1,2,2,1,5,2]
akumulasi = []
kasir = [[1,4],[2,5,7,9],[3,6,8,10]]
for j in range(len(kasir)):
  a = 0
  for k in kasir[j]:
    if k in antri:
      t = antri.index(k)
      a += waktu[t]
  akumulasi.append(a)
print(akumulasi)
print('waktu yang dibutuhkan untuk melayani seluruh antrian adalah ',max(akumulasi), ' menit')
