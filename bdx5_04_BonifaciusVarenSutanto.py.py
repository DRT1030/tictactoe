pi = 3.14159265; print('X5/04/Bonifacius Varen Sutanto')
print('1. Persegi'); s = float(input('Ketik panjang sisi: ')); L = s * s; K = 4 * s; print('Luas persegi adalah', L); print('Keliling persegi adalah', K);print('-------------------------')

print('2. Persegi panjang'); p = float(input('Ketik panjang: ')); l = float(input('Ketik lebar: ')); L = p * l; K = 2*(p+l); print('Luas persegi panjang adalah', L);
print('Keliling persegi panjang adalah', K); print('------------------------------')

print('3. Jajar genjang'); a = float(input('Ketik panjang alas(a): ')); b = float(input('Ketik panjang atap(b): ')); c = float(input('Ketik panjang sisi samping kiri(c): '));
d = float(input('Ketik panjang sisi samping kanan(d): ')); t = float(input('Ketik tinggi jajar genjang(t): ')); L = a * t; K = a+b+c+d
print('Luas jajar genjang adalah', L); print('Keliling jajar genjang adalah', K); print('------------------------------')

print('4. Jajar genjang sama sisi')
a = float(input('Ketik panjang alas(a): ')); b = float(input('Ketik panjang sisi samping(b): ')); t = float(input('Ketik tinggi(t): ')); L  = a*t; K = 2*(a+b)
print('Luas jajar genjang sama sisi adalah: ', L); print('Keliling jajar genjang sama sisi adalah: ', K); print('------------------------------')

print('5. Segitiga')
a = float(input('Ketik panjang alas(a): ')); b = float(input('Ketik panjang sisi kiri(b): ')); c = float(input('Ketik panjang sisi kanan(c): ')); t = float(input('Ketik tinggi(t):'))
L = 0.5 * a * t; K = a + b + c; print('Luas segitiga adalah: ', L); print('Keliling segitiga adalah: ', K); print('------------------------------')

print('6. Belah ketupat')
a = float(input('Ketik panjang sisi a: ')); b = float(input('Ketik panjang sisi b: ')); c = float(input('Ketik panjang sisi c: ')); d = float(input('Ketik panjang sisi d: '))
d1 = float(input('Ketik panjang sisi diagonal 1 (d1): ')); d2 = float(input('Ketik panjang sisi diagonal 2 (d2): ')); L = 0.5 * d1 * d2; K = a + b + c + d
print('Luas belah ketupat adalah: ', L); print('Keliling belah ketupat adalah: ', K); print('------------------------------')

print('7. Layang-layang')
a = float(input('Ketik panjang sisi a: ')); b = float(input('Ketik panjang sisi b: ')); c = float(input('Ketik panjang sisi c: ')); d = float(input('Ketik panjang sisi d: '))
d1 = float(input('Ketik sisi diagonal 1 layang-layang: ')); d2 = float(input('Ketik sisi diagonal 2 layang-layang: ')); L = 0.5 * d1 * d2; K = a + b + c + d
print('Luas layang-layang adalah: ', L); print('Keliling layang-layang adalah: ', K); print('------------------------------')

print('8. Trapesium ')
a = float(input('Ketik panjang sisi a: ')); b = float(input('Ketik panjang sisi b: ')); c = float(input('Ketik panjang sisi c: ')); d = float(input('Ketik panjang sisi d: '))
t = float(input('Ketik tinggi trapesium: ')); L = (a+b)/2 * t; K = a + b + c + d; print('Luas trapesium adalah: ', L); print('Keliling trapesium adalah: ', K); print('--------------------')

print('9. Lingkaran')
r = float(input('Ketik jari-jari lingkaran: ')); L = pi * r ** 2; K = 2 * pi * r; print('Luas lingkaran adalah: ', L); print('Keliling lingkaran adalah: ', K);print('---------------------')

#output yang penting
