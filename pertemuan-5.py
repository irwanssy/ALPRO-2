def no1():
    x = 1
    y = 2
    print(x == y) #false
    print(x != y) #true
    print(x > y) #false
    print(x < y) #true
    print(x >= y) #false
    print(x <= y) #true

def no2():
    def perbandingan():
        x = int(input("masukkan angka kmu: "))
        if x < 100:
            print("False")
        else:
            print("True")
    perbandingan()

def no3():
    a = 10
    if a > 0:
        print("-" * 5 + "bilangan bulat positif" + "-" * 5)

def no4():
    a = -1
    if a >= 1:
        print("-" * 5 + "bilangan bulat positif" + "-" * 5)
    if a < 0:
        print("-" * 5 + "bilangan bulat negatif" + "-" * 5)
    if a == 0:
        print("-" * 5 + "bilangan bulat nol" + "-" * 5)

def no5():
    #if-else statement
    n = int(input("masukkan sebuah angka: "))
    if n % 2 == 0:
        print("genap")
    else:
        print("ganjil")

def no6():
    n = 88
    if n >= 90:
        print(n)
        print("lulus")
    elif n >= 80 and n < 90:
        print(n)
        print("remedial")
    else:
        print(n)
        print("tidak lulus")

def no7():
    angka1 = int(input("masukan angka 1: "))
    angka2 = int(input("masukan angka 2: "))
    if angka1 > angka2:
        angkaBesar = angka1
    else:
        angkaBesar = angka2
    print("angka terbesar adalah", angkaBesar)

def no8():
    angka1 = int(input("masukan angka 1: "))
    angka2 = int(input("masukan angka 2: "))
    angka3 = int(input("masukan angka 3: "))    
    if angka1 > angka2 and angka1 > angka3:
        angkaBesar = angka1
    elif angka2 > angka1 and angka2 > angka3:
        angkaBesar = angka2
    elif angka3 > angka1 and angka3 > angka2:
        angkaBesar = angka3
    print("angka terbesar adalah", angkaBesar)

def no9():
    angka1 = int(input("masukan angka 1: "))
    angka2 = int(input("masukan angka 2: "))
    angka3 = int(input("masukan angka 3: "))    
    angkaBesar = max(angka1, angka2, angka3)
    print("angka terbesar adalah", angkaBesar, sep="-")

def no10():
    penghasilan = float(input("penghasilan: "))
    pajak = 0
    if penghasilan <= 60_000_000:
        print(penghasilan, " tarif 5%")
        tpajak = 0.05
    elif penghasilan > 60_000_000:
        print(penghasilan, " tarif 10%")
        tpajak = 0.15
    elif penghasilan > 250_000_000:
        print(penghasilan, "tarif 15%")
        tpajak = 0.25
    elif penghasilan > 500_000_000:
        print(penghasilan, "tarif 25%")
        tpajak = 0.30
    else:
        print("penghasilan tidak termasuk dalam kategori pajak yang diketahui.")
    pajak = penghasilan * tpajak
    print("pajak yang harus anda bayar: ", pajak)
