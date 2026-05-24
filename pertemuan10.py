def no1():
    list1 = [i + 1 for i in range(3)]
    print(list1)

def no2():
    array1 = [[2 * n for n in range(3)] for m in range(2)]
    print(array1)

def no3():
    kamar = [[[False for k in range(20)] for j in range(3)] for i in range(3)]
    kamar[1][2][19] = True
    print(kamar[1][2][19])

def no4():
    def fungsi(x):
        print("this is from function", str(x))
    a = False
    fungsi(12)
    print(a)

def no5():
    kuis1 = [i * 3 for i in range(1,11) if i % 2 == 0]
    print(kuis1)

def no6():
    array2d = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
    print(array2d)

def no7(): 
    data = [[2,4], [6,8], [10,12]]
    list1 = [i for baris in data for i in baris]
    print(list1)

def no8():
    def luasPersegi(p,l):
        return p * l
    panjang = 8
    lebar = 5
    print(f"hasil Luasnya adalah {luasPersegi(panjang,lebar)}")
no8()