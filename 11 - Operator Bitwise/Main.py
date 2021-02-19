# Operator bitwise, operasi biner, Binary
# Operasi masing-masing bit

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('/n========OR========')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('nilai : ', b, ', binary :', format(b, '08b'))
print('------------------------------(|)')
print('nilai : ', c, ', binary :', format(c, '08b'))


# bitwise AND (&)
c = a & b
print('/n========AND=======')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('nilai : ', b, ', binary :', format(b, '08b'))
print('------------------------------(&)')
print('nilai : ', c, ', binary :', format(c, '08b'))


# bitwise XOR (^)
c = a ^ b
print('/n========XOR=======')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('nilai : ', b, ', binary :', format(b, '08b'))
print('------------------------------(^)')
print('nilai : ', c, ', binary :', format(c, '08b'))


# bitwise NOT (~) -> akan negmirror dengan nilainya
c = ~a
print('/n========NOT=======')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('------------------------------(~)')
print('nilai : ', c, ', binary :', format(c, '08b'))
print('------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai : ', e ^ d, ' , binary :', format(e ^ d, '08b'))

# shifting

# shift right (>>) -> untuk menggeser nilai ke kanan
c = a >> 1
print('/n========>>=======')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('------------------------------(>>)')
print('nilai : ', c, ', binary :', format(c, '08b'))

# shift left (<<) -> untuk menggeser nilai ke kiri
c = a << 2
print('/n========<<=======')
print('nilai : ', a, ', binary :', format(a, '08b'))
print('------------------------------(<<)')
print('nilai : ', c, ', binary :', format(c, '08b'))
