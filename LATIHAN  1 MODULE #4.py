print("\n=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("=#=#=#=# PROGRAM DISCOUNT #=#=#=#=")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

print("###### Anda akan mendapatkan diskon jika total belanja anda mencapai Rp. 250.000 ######\n")
total_belanja = float(input("Masukkan total belanjaan Anda: Rp. "))

if total_belanja >= 250000:
    diskon = total_belanja * 50 / 100
    print("Anda mendapatkan diskon sebesar : Rp.", diskon)
else:
    print("Total belanjaan Anda adalah : Rp.", total_belanja)
    print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000")

print("\nTerima Kasih telah menggunakan program saya\n")
print("          NAMA : M.IRSYAD S.Y              ")
print("          NPM  : 07352311150                \n")
