# latihan satuan temperature

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR \n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah", celcius, " Celcius")

# reamut
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")
