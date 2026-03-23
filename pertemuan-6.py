while True:
    perintah = input("masukan command: ")
    if perintah == "keluar".lower():
        print("keluar")
        break
    else:
        print("jalankan", perintah)

hp = 10
while hp > 0:
    print("HP: ", hp)
    hp -= 1

ganjil = 0
genap = 0
angka = int(input("masukkan angka (0 untuk berhenti): "))
while angka != 0:
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    angka = int(input("masukkan a4ngka (0 untuk berhenti): "))
print("Jumlah angka ganjil:", ganjil)
print("Jumlah angka genap:", genap)

secretNumber = 11
angkaTebakan = int(input("Tebak angka: "))
while angkaTebakan != secretNumber:
    print("hahaha ! kamu nyangkut deh di Loop saya")
    angkaTebakan = int(input("Tebak lagi: "))
print("selamat, Muggle! kamu bebas sekarang!")

for a in range(10):
    print("nilai a saat ini adala a:",a)
for b in range(2,8):
    print("nilai b saat ini adala b:",b)
for c in range(2,8,3):
    print("nilai c saat ini adalah c:",c)
for d in range(1,1):
    print("nilai d saat ini adala d:",d)
for e in range(2,1):
    print("nilai e saat ini adala e:",e)
#----------------------------------------
power = 1
for expo in range(11):
    print(f"2 pangkat {expo} adalah {power}")
    power *= 2
print("\n")
#-----------------------------------------
for i in range(10):
    if i == 3:
        continue
    print("continue:", i)
for i in range(8):
    
    print(i)
    if i == 6:
        print("break selese:", i)
        break
#----------------------------------------
secretNumber = 77
while True:
    tebakAngka = int(input("tebak angka: "))
    if tebakAngka == secretNumber:
        print("selamat anda benar! anda mendapatkan Porsche Macan Electric!")
        break 
    else:
        print("coba lagi!")
#-------------------------------------------
kata = input("kata: ").upper()

for i in range(len(kata)):
    huruf = kata[i]
    if huruf == "A":
        continue
    elif huruf == "I":
        continue
    elif huruf == "U":
        continue
    elif huruf == "E":
        continue
    elif huruf == "O":
        continue
    else:
        print(huruf)
#----------------------------------------
n = 1
while n <= 5:
    print(n)
    n += 1
else:
    print("else: ", n)
#----------------------------------------
for i in range(0,10,2):
    print(i)
else:
    print("genap: ", i)
print()
a = 1
b = 0
hitung =(a and b) or (not False)
print("hasil persamaan logika: ", hitung)
print()
#----------------------------------------
a = 5
b = 3
print("logika:", a and b)
print("bitwise:", a & b)

a = 5
print(a << 3) #40
print(16 >> a) #

x = 4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a,b,c,d,e,f)