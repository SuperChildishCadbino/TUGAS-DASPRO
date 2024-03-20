#buatlah program untuk menghitung nilai akhir mahasiswa dimana anda memiliki:
# 1. Nilai kehadiran sebayak 16x. hitung total nilai kehadiran
# 2. 8 Tugas, hitung total nilai tugas
# 3. Nilai UTS
# 4. Nilai UAS

# jumlahkan keempat nilai tersebut dan tentukan hasil nilai kelulusan. dengan
# ketentuan

# A => 90
# B => 80
# C => 70
# D => 60
# E =< 60

print("\n=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("=#=#=#=# PROGRAM MENGHITUNG NILAI MAHASISWA #=#=#=#=")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

nama = (input("Masukkan Nama : "))
kehadiran = int(input("Masukkan total kehadiran : "))
tugas = int(input("Masukkan total tugas : "))
nilai_uts = int(input("Masukkan  Nilai UTS : "))
nilai_uas = int(input("Masukkan  Nilai UAS : "))

total_kehadiran = kehadiran * 16
total_nilai = total_kehadiran + tugas + nilai_uts + nilai_uas
nilai_akhir = total_nilai / 4

if nilai_akhir >= 90:
    hasil_nilai = 'A'

elif nilai_akhir >= 80:
    hasil_nilai = 'B'

elif nilai_akhir >= 70:
    hasil_nilai = 'C'

elif nilai_akhir >= 60:
    hasil_nilai = 'D'

else:
    hasil_nilai = 'E'

print("NAMA : ",nama)
print("Nilai akhir : ",nilai_akhir)
print("Hasil nilai kelulusan",hasil_nilai)