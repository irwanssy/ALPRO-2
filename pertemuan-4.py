def nomor1():
    a = input()
    print(a)

def nomor2():
    kataKata = input("kata kata hari ini: ")
    print(kataKata)

def nomor3():
    pengertianInput=input("Masukan Pengertia: ")
    print(pengertianInput)

def nomor4():
    jariJari = float(input('Masukan jari jari lingkaran: '))
    print(jariJari)

a = float(input("alas: "))
t = float(input("tinggi: "))
hypo = (a**2 + t**2)** .0
print("sisi miring segitigas: ", hypo)

a = float(input("alas: "))
t = float(input("tinggi: "))
print("sisi miring segitigas: ",(a**2 + t**2)** .0)

nama = input("masukan nama anda: ")
umur = int(input("umur:"))
print("halo " + nama + " umur saya adala" + str(umur)+ "tahun")

garis = '='
print("+" + garis * 20 + "+")

a = int(input("masukan angka pertama: "))
print(str(a))

a = int(input("masukan angka pertama: "))
print(type(a))

a = int(input("angka pertama: "))
b = int(input("angka kedua: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

x = int(input("masukan nilai x "))
y = 1.0/(x+1.0(x+1.0/(x+1.0/x)))
print(y)

jam = int(input("masukan jam: "))
menit = int(input("masukan menit: "))
durasi = int(input("durasi: "))

jamBaru = jam+ (menit+durasi)// 60
menitBaru = (menit+durasi) % 60
print((str(jamBaru)+ ':' +str(menitBaru)))
