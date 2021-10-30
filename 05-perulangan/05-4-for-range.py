for i in range(1,4):
  print(i)
print('Selesai')

print()
print('range(len)')
daftar_benda=['Meja', 'Kursi', 'Pintu', 'Lemari']
panjang_daftar = len(daftar_benda) # length of list
for i in range(panjang_daftar):
  print(i, end=" ")
  print(daftar_benda[i])
print('Selesai')

print()
print("range(1,len)")
daftar_benda=['Meja', 'Kursi', 'Pintu', 'Lemari']
panjang_daftar = len(daftar_benda)
for i in range(1,panjang_daftar):
  print(i, end=" ")
  print(daftar_benda[i])
print('Selesai')

print()
print("range(1,len, step)")
daftar_benda=['Meja', 'Kursi', 'Pintu', 'Lemari']
panjang_daftar = len(daftar_benda)
for i in range(1,panjang_daftar,2):
  print(i, end=" ")
  print(daftar_benda[i])
print('Selesai')
