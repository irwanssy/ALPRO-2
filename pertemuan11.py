def no1():
    def selamatUlangTahun(harapan=True):
        print("3")
        print("2")
        print("1")
        if not harapan:
            return 
        print("selamat Ulang tahun")
    selamatUlangTahun()

def no2():
    def selamatUlangTahun(harapan=True):
        print("3")
        print("2")
        print("1")
        if not harapan:
            return 
        print("selamat Ulang tahun")
    selamatUlangTahun(False)

def no3():
    def angkaSpesial():
        return 1
    x = angkaSpesial()
    print("Angka spesial:", x)

def no4():
    def angkaSpesial():
        return 1
    angkaSpesial()
    print("angka spesialnya tidak muncul")

def no5():
    def keywordNono(n):
        if n % 2 == 0:
            return True
    print(keywordNono(13))

def no6():
    def penjumlahanList(data):
        s = 0
        for d in data:
            s += d
        return s
    print(penjumlahanList([10,10]))

def no7():
    def penjumlahanList(data):
        s = 0
        for d in data:
            s += d
        return s
    print(penjumlahanList(7))

def no8():
    def fungsianeh(n):
        list1 = []
        for i in range(n):
            list1.insert(0,i)
        return list1
    print(fungsianeh(5))

def no9():
    def tahunKabisat(tahun):
        if tahun % 400 == 0 or tahun % 4 == 0 and tahun % 100 != 0:
            return True
        else:
            return False
        
    data_uji = [1900,2000, 2016, 1987]
    data_hasil = [False,True,True,False]
    for i in range(len(data_uji)):
        th = data_uji[i]
        print(th, "->", end=" ")
        hasil = tahunKabisat(th)

        if hasil == data_hasil[i]:
            print("oke")
        else:
            print("gagal")

def no10():
    def tahunKabisat(tahun):
        if tahun % 400 == 0 or tahun % 4 == 0 and tahun % 100 != 0:
            return True
        else:
            return 
    def hari_bulanKabisat(tahun,bulan):
        if bulan == 2:
            if tahunKabisat(tahun):
                return 29
            else:
                return 28
        elif bulan == 1:
            return 31
        elif bulan == 11:
            return 30
        
    data_uji = [1900,2000, 2016, 1987]
    data_bulan = [2,2,1,11]
    data_hasil = [28,29,31,30]
    for i in range(len(data_uji)):
        th = data_uji[i]
        bln = data_bulan[i]
        print(th,bln, "->", end=" ")
        hasil = hari_bulanKabisat(th,bln)

        if hasil == data_hasil[i]:
            print("oke")
        else:
            print("gagal")

def no11():

    def tahunKabisat(tahun):
        if tahun % 400 == 0 or tahun % 4 == 0 and tahun % 100 != 0:
            return True
        else:
            return False

    def hari_bulanKabisat(tahun, bulan):
        if bulan == 2:
            if tahunKabisat(tahun):
                return 29
            else:
                return 28
        elif bulan in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def hari_padaTahun(tahun, bulan, hari):
        batas_hari = hari_bulanKabisat(tahun, bulan)
        if bulan < 1 or bulan > 12:
            return None
        if hari < 1 or hari > batas_hari:
            return None
        total_hari = 0
        for m in range(1, bulan):
            total_hari += hari_bulanKabisat(tahun, m)
        total_hari += hari
        return total_hari

    print(hari_padaTahun(2000, 12, 31))

def no12():
    def cekPrima(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(1,20):
        if cekPrima(i+1):
            print(i+1, end=" ")
    print()

def no13():
    def cekPrima(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(1,20):
        if cekPrima(i+1):
            print(i+1, end=" ")
    print()

def no14():
    def liter100km_ke_mpg(liter):
        mil = 100000 / 1609.344
        galon = liter / 3.785411784
        return mil / galon
    def mpg_ke_liter100km(mil_per_galon):
        liter = 3.785411784
        km100 = (mil_per_galon * 1.609344) / 100
        return liter / km100
    print(liter100km_ke_mpg(3.9))
    print(liter100km_ke_mpg(7.5))
    print(liter100km_ke_mpg(10.0))
    print(liter100km_ke_mpg(60.3))
    print(liter100km_ke_mpg(31.4))
    print(liter100km_ke_mpg(23.5))
no14()