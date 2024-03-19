print("\n=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("=#=#=#=# PROGRAM CONVERT #=#=#=#=")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

bilangan = int(input("Massukan bilangan : "))

konversi1 = bin(bilangan)[2:]

konversi2 = hex(bilangan)

konversi3 = oct(bilangan)

print()

print("Convert Bilangan Biner ", konversi1.zfill(8))

print("Bilsngsn HexaDecimal ", konversi2)

print("Bilsngsn HexaDecimal ", konversi3)

print("\nTerima Kasih telah menggunakan program saya\n")
print("          NAMA : M.IRSYAD S.Y              ")
print("          NPM  : 07352311150                \n")
