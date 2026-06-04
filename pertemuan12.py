def no1():
    a = 5
    def perkalian(x):
        x = 3
        return x * 2
    print(perkalian(a))
    print(a)

def no2():
    a = 1
    def perkalian(x):
        a = 5
        return x * a
    print(perkalian(a))
    print(a)

def no3():
    def perkalian(x):
        a = 5
        return x * a
    print(perkalian(7))

def no4():
    a = 5
    def ubah(x):
        global a
        a = x + a
        return a
    print(ubah(5))
    print(a)    

def no5():
    def hitungIMT(b,t):
        imt = b / t ** 2
        return imt
    berat = float(input("masukan berat (kg): "))
    tinggi = float(input("masukan tinggi (m): "))
    index_massa_tubuh = hitungIMT(berat,tinggi)
    kategori = ["Normal", "Gemuk", "Obesitas"]
    if index_massa_tubuh < 18.0 or index_massa_tubuh <= 25.0:
        print("Index massa tubuh anda",index_massa_tubuh,"masuk kategori", kategori[0])
    elif index_massa_tubuh > 25.0 or index_massa_tubuh <= 27.0:
        print("Index massa tubuh anda",index_massa_tubuh,"masuk kategori", kategori[1])
    else:
        print("Index massa tubuh anda",index_massa_tubuh,"masuk kategori", kategori[2])

def no6():
    def cekSegitiga(a,b,c):
        if a + b <= c:
            return False
        if b + c <= a:
            return False
        if c + a <= b:
            return False
        return True
    print(cekSegitiga(1,1,1))
    print(cekSegitiga(1,1,2))

def no7():
    def cekSegitiga(a,b,c):
        if a + b <= c or b + c <= a or c + a <= b:
            return False
        return True
    print(cekSegitiga(1,1,1))
    print(cekSegitiga(1,1,2))

def no8():
    def cekSegitiga(a,b,c):
        return a + b > c and b + c > a and c + a > b
    print(cekSegitiga(1,1,1))
    print(cekSegitiga(1,3,1))

def no9():
    def faktorial(n):
        if n < 0:
            return None
        if n < 2:
            return 1
        hasil = 1
        for i in range(n):
            hasil = hasil * (i + 1)
        return(hasil)
    n = int(input("masukan angka: "))
    print(n,"! =", faktorial(n))
    
def no10():
    def fibonacci(n):
        if n < 1:
            return None
        if n < 3:
            return 1

        elem_1 = elem_2 = 1
        hasil_jumlah = 0
        for i in range(3, n + 1):
            hasil_jumlah = elem_1 + elem_2  
            elem_1 = elem_2                 
            elem_2 = hasil_jumlah
        return hasil_jumlah

    for n in range(1, 10):
        print(n, "-->", fibonacci(n))

def no11():
    def faktorial(n):
        if n == 0:
            return 1
        return n * faktorial(n-1)
    print(faktorial(4))

def no12():
    def fibonacci(n):
        if n < 1:
            return None
        if n < 3:
            return 1
        return fibonacci(n-1) + fibonacci(n-2)
    print(fibonacci(6))
no12()
