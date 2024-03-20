hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        print("Anda mendapatkan diskon sebesar Rp.", diskon)
    else:
        print("Total belanjaan Anda adalah Rp.", total_belanja)
        print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000")

total_belanja = float(input("Masukkan total belanjaan Anda: Rp. "))
hitung_diskon(total_belanja)