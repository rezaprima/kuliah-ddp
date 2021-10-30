daftar_benda=['Meja', 'Kursi', 'Pintu', 'Lemari']
dicari='Almari'
panjang_daftar = len(daftar_benda) # length of list
for i in range(panjang_daftar):
  if daftar_benda[i]==dicari:
    print('%s ditemukan di posisi %d'%(dicari,i))
    break
else:
  print('%s tidak ditemukan'%(dicari))
