nama = (input("masukkan namamu:"))
kelas = (input("masukkan kelasmu:"))
nilai = int(input("masukkan nilai:"))

print("----BIODATA SISWA----")
print("nama siswa: ",nama)
print("kelas : ", kelas)

if nilai<=75:
   print("selamat, kamu LULUS")
else: 
   print("maaf, kamu BELUM LULUS")