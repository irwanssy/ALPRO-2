def no1():    
    iniTuple = (1,2,3,4,5)
    print(iniTuple)

def no2():
    a = ("james", 12, 13, 14)
    print(a[0])
    print(len(a))
    a2 = a + (15, 16)
    print(a2)

def no3():
    a = (1,2,3,4,5)
    print("ini tuple lama:", a)
    b = list(a)
    b[0] = 0
    a = tuple(b)
    print("ini tuple baru:", b)

def no4():
    t = ("apel", "mangga", "sirsak", "jeruk")
    print("1. banyaknya tuple:", len(t))
    t2 = t + ("pisang", "nanas")
    print("2. setelah ditambah:",t2)
    t3 = t2 * 2
    print("3. setelah dikalikan:", t3)
    if "apel" in t3:
        print(f"4.{True}")
    if ("susu", "kedelai") not in t3:
        print(f"5.{True}") 

def no5():
    t1 = (1,2,3)
    a, b, c = t1
    print(a,b,c)

def no6():
    dict = {
        1:"irwansyah",
        2:"mutiara"
            }
    print(dict)

def no7():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara"
            }
    print(dict["nama"],"and", dict["myBini"])

def no8():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara" 
    }
    print(dict.keys())

def no9():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara" 
    }
    print(dict.values())

def no10():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara" 
    }
    print(dict.items())
def no11():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara" 
    }
    dict.update({"myHp":"Techno"}) #update
    for a,b in dict.items():
        print(f"{a} -> {b}")
def no12():
    dict = {
        "nama":"irwansyah",
        "myBini":"mutiara" 
    }
    print(dict.popitem())

def no13():
    dict = {
        1:"Mie ayam",
        2:"Nasi Goreng",
        3:"Nasi Jamblang"
    }
    for k, v in dict.items():
        print(f"{k}. {v}")
    print("=" * 10)
    #nilai baru
    dict[3] = "Mie Goreng"
    for k, v in dict.items():
        print(f"{k}. {v}")
    print("=" * 10)
    #mngurutkan
    for k in sorted(dict.values()):
        print(f"urutan abjad {k}")
    print("=" * 10)
    #menambahkan data baru
    dict[4] = "Es Teh"
    for k, v in dict.items():
        print(f"{k}. {v}")
    print("=" * 10)
    #delete
    del dict[4]
    for k, v in dict.items():
        print(f"{k}. {v}")
def no14():
    while True:
        try:
            print("wajib angka!")
            x = int(input("harus angka: "))
            break
        except:
            print("Salah!, harus angka")

def no15():
    try:
        x = int("abc")
    except ValueError or TypeError as e:
        print("error", e)
no15()