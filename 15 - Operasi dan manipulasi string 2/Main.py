# Operasi dan manupulasi string 2

# merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("normal = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeeZZzzzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  # hasilnya akan boolean
print(salam + ' is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilnya akan boolean
print(salam + ' is upper = ' + str(apakah_upper))

# isalpha() <- untuk mengecek semuanya huruf
# isalnum() <- huruf dan angka
# isdecimal() <- untuk angka saya
# isspace() <- spasi, tab, newline \n
# istitle() <- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # hasilnya akan boolean
print(judul + ' is title = ' + str(cek_judul))

# ngecek komponen startwith() endwith() <-- kerennlah
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

# penggabungan komponen join() split
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, '-')
print("'" + tengah + "'")


# kebalikannya -> strip()
tengah = tengah.strip("-")  # menghilangkan tanda -
print("'"+tengah+"'")
