def tampilkan(nama_siswa, nama_matakuliah, nilai_akhir):
  status=""

  if nilai_akhir > 70:
    status="LULUS"
  else:
    status="MENGULANG"
  
  print(f"siswa bernama {nama_siswa} di {nama_matakuliah} memiliki nilai {nilai_akhir}, {status}")

tampilkan("Reza", "DDP", 75)
tampilkan("Dian", "Bahasa", 65)