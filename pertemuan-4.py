def no1():
    a = input()
    print(a)

def no2():
    kataKata = input("kata kata hari ini: ")
    print(kataKata)

def no3():
    pengertianInput = input()
    print(pengertianInput)

def no4():
    jariJari = float(input("Masukan jari jari lingkaran: "))
    print(jariJari)

def no5():
    a = float(input("Masukkan sisi alas: "))
    t = float(input("Masukkan sisi tinggi: "))
    hypo = (a**2 + t**2)**0.5
    print("Sisi miring segitiga adalah:", hypo) 

def no6():
    a = float(input("Masukkan sisi alas: "))
    t = float(input("Masukkan sisi tinggi: "))
    print("Sisi miring segitiga adalah:", (a**2 + t**2)**0.5)

def no7():
    Nama = str(input("Masukkan nama : "))
    umur = int(input("Masukan Kota asal : "))
    print("Hai, saya " + Nama + " umur saya " + umur + " tahun")

def no8():
    garis = "="
    print("+" + "garis" * 20 + "+")

def no9():
    umur = int(input("Masukkan umur Anda: "))
    print("Wow umurmu sudah " + str(umur) + " tahun!")

def no10():
    a = int(input("masukan angka: "))
    print(type(a))

def no11():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    print("Hasil penjumlahan:", a + b)
    print("Hasil pengurangan:", a - b)
    print("Hasil pembagian:", a / b)
    print("Hasil perkalian:", a * b)
    print("Selamat kamu sudah pintar Matematika.")

def no12():
    x = float(input("Masukan nilai x : "))
    y = 1.0 / (x+1.0 / (x+1.0 / (x+1.0 /x)))
    print("Hasil dari y adalah : ", y)

def no13():
    jam = int(input("waktu mulai (jam) : "))
    menit = int(input("waktu mulai (menit) : "))
    durasi = int(input("Durasi Acara (menit) : "))
    #Tambah durasi ke menit
    menit += durasi
    #Hitung tambahan jam 
    jam += menit // 60
    menit %= 60
    #Supaya jam tak lebih dari 24
    jam %= 24
    print("Acara berakhir pukul", jam, ":", menit)