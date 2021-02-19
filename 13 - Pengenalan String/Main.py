data = "ini adalah string"  # kumpulan dari karakter
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single qoute '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single qoute'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' ,enjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline -> macam2 konfensi dimanakah akhir dari barisnya
print("baris pertama.\nbaris kedua.")  # LF -> Line feed -> unix, macos, linux
# CR -> Carriage return -> comodore, acorn, lisp
print("baris pertama.\rbaris kedua.")
# CRLF -> line feed carriage return -> dipakai oleh windows
print("baris pertama.\r\nbaris kedua.")

# 3. String literal atau raw

# hati-hati
print('C:\new folder')  # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder\dec\d')  # akan diprint semuanya

# multiline literal string
print(""" 
Nama : Ucup
kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")
