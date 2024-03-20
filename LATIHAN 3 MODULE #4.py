database_mahasiswa = {
    "mirsyad": "123456",
    "07352311150": "123456",
}

daftar_dosen_pengampu = {
    "Bahasa Inggris": "Mam yeti",
    "Dasar Pemograman": "Pak Yasir",
}

while True:
    print("\n=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    print("=#=#=#=# PROGRAM LOGIN #=#=#=#=")
    print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

    username = input("Masukkan username atau NPM: ")
    password = input("Masukkan password: ")

    if username in database_mahasiswa and database_mahasiswa[username] == password:
        print("Autentikasi berhasil!")
        break
    else:
        print("Autentikasi gagal. Silakan coba lagi.")

print("Daftar mata kuliah yang tersedia:")
daftar_mata_kuliah = list(daftar_dosen_pengampu.keys())
for i in range(len(daftar_mata_kuliah)):
    print(f"{i + 1}. {daftar_mata_kuliah[i]}")

while True:
    try:
        pilihan_mata_kuliah = int(input("Masukkan nomor mata kuliah: "))
        if 1 <= pilihan_mata_kuliah <= len(daftar_dosen_pengampu):
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor yang sesuai.")
    except ValueError:
        print("Masukkan nomor mata kuliah yang sesuai.")

mata_kuliah_terpilih = daftar_mata_kuliah[pilihan_mata_kuliah - 1]

print("Daftar dosen pengampu untuk mata kuliah", mata_kuliah_terpilih, ":")
print(daftar_dosen_pengampu[mata_kuliah_terpilih])

print("Username / NPM :", username)
print("Nama mata kuliah :", mata_kuliah_terpilih)
daftar_dosen = daftar_dosen_pengampu[mata_kuliah_terpilih]
print("Dosen pengampu :",daftar_dosen)

print("\nTerima Kasih telah menggunakan program saya\n")
print("          NAMA : M.IRSYAD S.Y              ")
print("          NPM  : 07352311150                \n")
