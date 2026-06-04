def no1():
    data = [32,16,8,4,2,1]
    print(f"data awal: {data}")
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            print(f"iterasi {i+1}, langkah {j+1}: {data}")
        print("-"*8)
    print("hasil:", data)

def no2():
    #interative
    data = []
    daftarAngka = input("Masukan angka: ke dalam data: (pisahkan dengan koma): ")
    for angka in daftarAngka.split(","):
        data.append(int(angka))
    print("data yg ada: ", data)

    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(f"iterasi {i+1}: {data}")
    print("hasil after diurutkan:", data)


def no8():
    listA = [2,3,4,5,6,7]
    print(";ist Awal:", listA)
    listA = listA[-2:1]
    print(listA)

def no13():
    listA = [2,3,4,5,6,7]
    print(";ist Awal:", listA)
    del listA[:]
    print(listA)

def no19():
    myList = [1,2,3,4,5,6,7,8,9,10]
    toFind = 5
    found = False

    for i in range(len(myList)):
        found = myList[i] == toFind
        if found:
            print("ketemu")
            break
    if found:
        print("elemen ditemukan pada indeks ke-",i)
    else:
        print("not found")

def no20():
    tebakanKu = [3,7,11,42,34,49]
    undian = [5,9,11,42,3,49]
    tebakanBenar = 0
    for angka in tebakanKu:
            if angka in undian:
                tebakanBenar += 1
    print(f"tebakan yg benar dari Undian ada {tebakanBenar}!")

def no21():
    data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    print(f"data lama:{data}")
    dataBaru = []
    for angka in data:
        if angka not in dataBaru:
            dataBaru.append(angka)
    print(f"data baru setelah menghapus duplikast:{dataBaru}")

no21()