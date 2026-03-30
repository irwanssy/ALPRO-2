def nomor1():
    angka = [1,2,3,4,5]
    print("list lamanya: ", angka)
    angka[0] = 10
    print("list baru: ", angka)

def nomor2():
    angka = [1,2,3,4,5]
    print(angka[0])
    print(angka)

def nomor3():
    isiList = [1,2,3,4,5]
    print(f"ada {len(isiList)} elemen dalam list")

def nomor4():
    lis1 = [1,2,3]
    print(f"list lama: {lis1}")
    del lis1[0]
    print(f"list after deletion: {lis1}")

def nomor5():
    list1 = [1,2,3]
    return list1[-1]

topi_list = [1,2,3,4,5]
def nomor6():
    replace = int(input("masukkan angka: "))
    topi_list[2] = replace
    del topi_list[-1]
    print(len(topi_list))
    print(topi_list)

def nomor7():
    angka = [111,2,3,45]
    angka.append(60)
    print(angka)
    print(len(angka))
    angka.insert(0,99)
    print(angka)
    print(len(angka))

def nomor8():
    list1 = []
    for i in range(5):
        list1.append(i + 1)
    print("list1: ", list1)

def nomor9():
    list2 = []
    for i in range(5):
        list2.insert(0, i + 1)
    print("list2: ", list2)

def nomor10():
    var1 = 1
    var2 = 2
    var2 = var1
    var1 = var2
    print("var1: ", var1)
    print("var2: ", var2)

def nomor11():
    var1 = 1
    var2 = 2
    auxi = var1
    var1 = var2
    var2 = auxi
    print("var1: ", var1)
    print("var2: ", var2)

def nomor12():
    my_list = [10,1,8,3,5]
    my_list2 = my_list.copy()
    my_list[0], my_list[4] = my_list[4], my_list[0]
    my_list[1], my_list[3] = my_list[3], my_list[1]
    print(my_list)
    for i in range(len(my_list2) // 2):
        my_list2[i], my_list2[len(my_list2) - i - 1] = my_list2[len(my_list2) - i - 1], my_list2[i]
    print(my_list2)

exo = []
def nomor13():
    exo.append("Suho")
    exo.append("Kai")
    exo.append("Chanyeol")
    exo.append("Sehun")
    for anggota in ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]:
        exo.append(anggota)
    print(exo)
    #hapus anggota yang tidak aktif -----
    del exo[6] , exo[7], exo[7]
    print(f"setelah dihapus: {exo}")
    exo.insert(-2, "Xiumin")
    print(f"setelah ditambahkan: {exo}")
nomor13()
print(exo)