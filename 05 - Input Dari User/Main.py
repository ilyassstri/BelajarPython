# Input dari user

# data yang dimasukkan pasti string
data = input("Masukkan nama: ")

print("data =", data, ",type =", type(data))

# jika mau mengambil integer, maka
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))
print("data = ", angka, ",type =", type(angka))


# bagaimana jika boolean?
biner = bool(int(input("masukkan nilai boolean: ")))

print("data = ", biner, ",type =", type(biner))
