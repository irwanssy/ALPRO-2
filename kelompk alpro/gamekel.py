import random

print("\nHallo Traveler, Selmat datang di Game RPG sederhana ini!")
namaPlayernya = input("Masukkan nama player: ").title()
print("_" * 50)
player = {
    "nama": namaPlayernya,
    "level": 1,
    "xp": 0,
    "xp_next_level": 100, 
    "max_hp": 1000,
    "darah": 100,
    "coin": 100,
    "inventory": []
}

def player_status():
    print("\n" + "=" * 8, f"Status {player['nama']}", "=" * 8)
    print(f"Nama        : {player['nama']}")
    print(f"Level       : {player['level']}")
    print(f"Darah       : {player['darah']}")
    print(f"Coin        : {player['coin']}")
    print(f"Inventory   : {player['inventory']}")

def generate_enemy():
    enemies = ["Goblin", "Orc", "Slime"]
    enemy = random.choice(enemies)
    hp = random.randint(50, 100)
    attack = random.randint(5, 15)
    return {"name": enemy, "hp": hp, "attack": attack}

#aksi
def bertarung():
    enemy = generate_enemy()
    print("\n"+"!" * 20 + " ATTACK " + "!" * 20)
    print(f"  Kamu menghadapi {enemy['name']}! HP musuh: {enemy['hp']}, Serangan: {enemy['attack']}")

    while enemy['hp'] > 0 and player['darah'] > 0:
        print(f"\nDarahmu: {player['darah']}, XP-mu: {player['xp']}")
        action = input("Pilih aksi: (1) Serang (2) Lari (3) Gunakan Item: ")

        if action == "1":
            damage = random.randint(10, 25)
            enemy['hp'] -= damage
            print(f"Kamu menyerang {enemy['name']} dan memberikan {damage} damage!")
            
            if enemy['hp'] <= 0:
                perolehan_xp = random.randint(30, 60)
                tambah_xp(perolehan_xp)
                perolehan_koin = random.randint(10, 30)
                player['coin'] += perolehan_koin
                print(f"Kamu mendapatkan {perolehan_koin} koin!")
                print(f"Kamu mengalahkan {enemy['name']}!")
                loot = random.choice(["Potion", "Pedang", "Perisai"])
                player['inventory'].append(loot)
                print(f"Kamu mendapatkan item: {loot}")
                
                break
            
            player['darah'] -= enemy['attack']
            print(f"{enemy['name']} menyerang balik! Kamu kehilangan {enemy['attack']} darah.")
        
        elif action == "2":
            chance = random.random()
            if chance < 0.5:
                print("Kamu berhasil melarikan diri!")
                break
            else:
                print(f"Gagal kabur! {enemy['name']} menyerang kamu.")
                player['darah'] -= enemy['attack']
        
        elif action == "3":
            if not player['inventory']:
                print("Inventori kosong!")
                continue
            
            print("Inventori:")
            for idx, item in enumerate(player['inventory'], 1):
                print(f"{idx}. {item}")
            
            try:
                itemChoice = int(input("Pilih item yang ingin digunakan: "))
                if 1 <= itemChoice <= len(player['inventory']):
                    selected_item = player['inventory'][itemChoice - 1]
                    if selected_item == "Potion":
                        player['darah'] += 20
                        if player['darah'] > player['max_hp']:
                            player['darah'] = player['max_hp']
                        print("Kamu menggunakan Potion! Darah bertambah 20.")
                    elif selected_item == "Pedang":
                        print("Kamu menggunakan Pedang! Seranganmu meningkat untuk serangan berikutnya.")
                    elif selected_item == "Perisai":
                        print("Kamu menggunakan Perisai! Pertahananmu meningkat untuk serangan berikutnya.")
                    player['inventory'].remove(selected_item)
                else:
                    print("Pilihan item tidak valid.")
            except ValueError:
                print("Input tidak valid. Masukkan nomor.")
        else:
            print("Aksi tidak valid.")
    
    if player['darah'] <= 0:
        print("Darahmu habis. Game Over!")
        exit()

def beli_item():
    print("\n" + "=" * 5,"Selamat Datang di Toko Item:", "=" * 5)
    items = {"Potion": 20, "Pedang": 50, "Perisai": 40}
    for item, price in items.items():
        print(f"{item}: {price} coin")
    
    
    choice = input("Pilih item yang ingin dibeli: ").title()
    if choice in items:
        if player['coin'] >= items[choice]:
            player['coin'] -= items[choice]
            player['inventory'].append(choice)
            print(f"Kamu membeli {choice}!")
        else:
            print("Coin tidak cukup!")
    else:
        print("item tidak tersedia!")
    
def check_level_up():
    if player['xp'] >= player['xp_next_level']:
        player['level'] += 1
        player['xp'] -= player['xp_next_level'] 
        
        player['max_hp'] += 20 
        player['darah'] = player['max_hp'] 
        player['energy'] += 10
        
        player['xp_next_level'] = int(player['xp_next_level'] * 1.5)
        
        print(f"\n✨ TINGKATKAN LEVEL! ✨")
        print(f"Selamat {player['nama']}, kamu sekarang Level {player['level']}!")
        print(f"Darah Maksimal bertambah menjadi {player['max_hp']} dan HP pulih sepenuhnya!")

def tambah_xp(jumlah):
    print(f"✨ Kamu mendapatkan {jumlah} XP!")
    player['xp'] += jumlah
    check_level_up()

def tampilkan_xp_detail():
    print("\n" + "="*30)
    print(f"Status Player : {player['nama'].upper()} ")
    print("="*30)
    print(f"Level      : {player['level']}")
    
    lebar_bar = 20
    progres = int((player['xp'] / player['xp_next_level']) * lebar_bar)
    bar = "█" * progres + "-" * (lebar_bar - progres)
    
    print(f"XP         : [{bar}] {player['xp']}/{player['xp_next_level']}")
    print(f"Max Darah  : {player['darah']}/{player['max_hp']}")
    print(f"Koin       : {player['coin']}")
    print(f"Inventory  : {', '.join(player['inventory']) if player['inventory'] else 'Kosong'}")
    print("="*30)
    
    input("\nTekan Enter untuk kembali ke menu utama...")

while True:
    player_status()
    print("-" * 50)
    print("Pilih aksi:")
    print("1. Lawan enemy | 2. Beli Item | 3. Cek XP & Status | 0. Keluar")
    try:
        pilihan = int(input("Masukkan nomor aksi (1-3): 0 untuk keluar: "))
        if pilihan == 1:
            bertarung()
        if pilihan == 2:
            beli_item()
        if pilihan == 3:
            tampilkan_xp_detail()
        if pilihan == 0:
            print("Anda Keluar !!!")
            break
    except ValueError:
        print("Input tidak valid. Masukkan nomor.")
        continue

