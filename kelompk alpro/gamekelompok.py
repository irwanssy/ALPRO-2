import random


inventory = {}

# ======================
# INVENTORY SYSTEM
# ======================
def tambah_item(nama_item, jumlah):
    if nama_item in inventory:
        inventory[nama_item] += jumlah
    else:
        inventory[nama_item] = jumlah
    print(f"{jumlah} {nama_item} didapatkan.")

def pakai_item(nama_item):
    if nama_item in inventory:
        if nama_item == "Potion":
            player["hp"] += 20
            print("HP bertambah 20!")

        inventory[nama_item] -= 1

        if inventory[nama_item] == 0:
            del inventory[nama_item]
    else:
        print("Item tidak ada!")

def tampilkan_inventori():
    print("\n=== INVENTORI ===")
    if not inventory:
        print("Kosong")
    else:
        for item, jumlah in inventory.items():
            print(f"{item}: {jumlah}")
    print("=================\n")

