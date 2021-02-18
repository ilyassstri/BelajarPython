# Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi Kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi bagi /
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi Eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi Modulus % -> sisa pembagian
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi floor division // -> kebalikan dari modulus
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen ** 
    3. perkalian dan teman-temannya * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)
# kurung akan mengambil langkah paling pertama

hasil = (x + y) * z
print('(', x, '+', y, ') *', z, '=', hasil)
