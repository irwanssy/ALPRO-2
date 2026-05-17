menu = { 
    "Es Kopi Susu":12000,
    "Es Kopi Coklat":13000,
    "Es Kopi Espresso":15000,
    "Es Kopi Latte":17000,
    "Es Kopi Mocha":20000
}

print("=" * 7, "UIN Coffe", "=" * 7)
def menuTampil():
    for i in menu:
        print(f"Menu :", i, "Harga :", menu[i])
    print("Pembelian lebih dari 3 menu akan mendapatkan diskon 10%")
    print("=" * 30)

def pembelian():
    total = 0
    jumlah_menu = int(input("Masukan jumlah menu yang ingin dibeli: "))
    for i in range(jumlah_menu):
        menu_pilihan = input("Masukan menu yang ingin dibeli: ")
        menu_pilihan = menu_pilihan.title()
        if menu_pilihan in menu:
            total += menu[menu_pilihan]
        else:
            print("Menu tidak tersedia")    
    if jumlah_menu > 3:
        diskon = total * 0.1
        total = total - diskon
    print(f"Total harga: {total}")
menuTampil()
pembelian()


    