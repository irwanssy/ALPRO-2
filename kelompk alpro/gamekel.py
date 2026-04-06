# ================= IMPORT =================
import random


# ================= INTRO =================
print("\nHallo Traveler, Selamat datang di Game RPG sederhana ini!")
namaPlayernya = input("Masukkan nama player: ").title()
print("_" * 50)


# ================= DATA PLAYER =================
player = {
    "nama": namaPlayernya,
    "level": 1,
    "xp": 0,
    "xp_next_level": 100, 
    "max_hp": 1000,
    "darah": 100,
    "coin": 100,
    "inventory": [],
    "energy": 50,
    "max_energy": 50
}


# ================= STATUS PLAYER =================
def player_status():
    print("\n" + "=" * 8, f"Status {player['nama']}", "=" * 8)
    print(f"Nama        : {player['nama']}")
    print(f"Level       : {player['level']}")
    print(f"Darah       : {player['darah']}")
    print(f"Energy      : {player['energy']}")
    print(f"Coin        : {player['coin']}")
    print(f"Inventory   : {player['inventory']}")


# ================= GENERATE ENEMY =================
def generate_enemy():
    enemies = ["Goblin", "Orc", "Slime"]
    enemy = random.choice(enemies)
    hp = random.randint(50, 100)
    attack = random.randint(5, 15)
    return {"name": enemy, "hp": hp, "attack": attack}


# ================= LEVEL SYSTEM =================
def check_level_up():
    if player['xp'] >= player['xp_next_level']:
        player['level'] += 1
        player['xp'] -= player['xp_next_level']
        
        player['max_hp'] += 20 
        player['darah'] = player['max_hp']
        player['energy'] = player['max_energy']
        
        player['xp_next_level'] = int(player['xp_next_level'] * 1.5)
        
        print(f"\n✨ LEVEL UP! Sekarang Level {player['level']}!")

def tambah_xp(jumlah):
    print(f"✨ Kamu mendapatkan {jumlah} XP!")
    player['xp'] += jumlah
    check_level_up()


# ================= TAMPILKAN XP =================
def tampilkan_xp_detail():
    print("\n" + "="*30)
    print(f"Status Player : {player['nama'].upper()} ")
    print("="*30)
    print(f"Level      : {player['level']}")
    
    lebar_bar = 20
    progres = int((player['xp'] / player['xp_next_level']) * lebar_bar)
    bar = "█" * progres + "-" * (lebar_bar - progres)
    
    print(f"XP         : [{bar}] {player['xp']}/{player['xp_next_level']}")
    print(f"HP         : {player['darah']}/{player['max_hp']}")
    print(f"Energy     : {player['energy']}/{player['max_energy']}")
    print(f"Koin       : {player['coin']}")
    print(f"Inventory  : {', '.join(player['inventory']) if player['inventory'] else 'Kosong'}")
    print("="*30)
    
    input("\nTekan Enter untuk kembali...")


# ================= SHOP SYSTEM =================
def beli_item():
    print("\n" + "=" * 5,"Selamat Datang di Toko Item:", "=" * 5)
    items = {"Potion": 20, "Pedang": 50, "Perisai": 40}

    for item, price in items.items():
        print(f"{item}: {price} coin")
    
    choice = input("Pilih item: ").title()

    if choice in items:
        if player['coin'] >= items[choice]:
            player['coin'] -= items[choice]
            player['inventory'].append(choice)
            print(f"Kamu membeli {choice}!")
        else:
            print("Coin tidak cukup!")
    else:
        print("Item tidak tersedia!")


# ================= BATTLE SYSTEM =================
def bertarung():
    enemy = generate_enemy()
    print("\n"+"!" * 20 + " BATTLE " + "!" * 20)
    print(f"Kamu menghadapi {enemy['name']}! HP: {enemy['hp']} | ATK: {enemy['attack']}")

    while enemy['hp'] > 0 and player['darah'] > 0:
        print(f"\nHP: {player['darah']}/{player['max_hp']} | ⚡ Energy: {player['energy']}")
        print(f"HP Musuh: {enemy['hp']}")

        action = input("Aksi: (1) Attack (2) Item (3) Defend (4) Lari: ")

        # ===== ATTACK =====
        if action == "1":
            if player["energy"] < 10:
                print("⚡ Energy tidak cukup!")
                continue

            player["energy"] -= 10

            if random.randint(1, 100) <= 20:
                print("💨 Seranganmu meleset!")
            else:
                damage = random.randint(10, 25)
                enemy['hp'] -= damage
                print(f"⚔️ Kamu memberikan {damage} damage!")

        # ===== ITEM =====
        elif action == "2":
            if not player['inventory']:
                print("Inventori kosong!")
                continue

            for idx, item in enumerate(player['inventory'], 1):
                print(f"{idx}. {item}")

            try:
                pilih = int(input("Pilih item: "))
                item = player['inventory'][pilih - 1]

                if item == "Potion":
                    player['darah'] = min(player['darah'] + 20, player['max_hp'])
                    print("🧪 HP bertambah!")
                elif item == "Pedang":
                    print("⚔️ Attack boost sementara!")
                elif item == "Perisai":
                    print("🛡️ Defense boost sementara!")

                player['inventory'].remove(item)

            except:
                print("Input salah!")
                continue

        # ===== DEFEND =====
        elif action == "3":
            regen = random.randint(5, 15)
            player["energy"] = min(player["energy"] + regen, player["max_energy"])

            if random.randint(1, 100) <= 20:
                print("❌ Gagal defend!")
                damage = enemy["attack"]
            else:
                print(f"🛡️ Berhasil defend +{regen} energy!")
                damage = enemy["attack"] // 2

            player['darah'] -= damage
            print(f"Kamu kena {damage} damage!")
            continue

        # ===== LARI =====
        elif action == "4":
            if random.random() < 0.5:
                print("🏃 Berhasil kabur!")
                break
            else:
                print("Gagal kabur!")

        else:
            print("Pilihan salah!")
            continue

        # ===== MUSUH MENYERANG =====
        if enemy['hp'] > 0:
            enemy_damage = random.randint(5, enemy['attack'])
            player['darah'] -= enemy_damage
            print(f"👹 Musuh menyerang {enemy_damage} damage!")

        # ===== MENANG =====
        if enemy['hp'] <= 0:
            print(f"\n🎉 Kamu mengalahkan {enemy['name']}!")

            xp = random.randint(30, 60)
            coin = random.randint(10, 30)

            tambah_xp(xp)
            player['coin'] += coin

            loot = random.choice(["Potion", "Pedang", "Perisai"])
            player['inventory'].append(loot)

            print(f"Dapat {coin} coin & item {loot}")
            break

    if player['darah'] <= 0:
        print("💀 Kamu mati! Game Over.")
        exit()


# ================= MAIN MENU =================
while True:
    player_status()
    print("-" * 50)
    print("1. Lawan Enemy")
    print("2. Beli Item")
    print("3. Cek Status & XP")
    print("0. Keluar")

    try:
        pilihan = int(input("Pilih: "))

        if pilihan == 1:
            bertarung()
        elif pilihan == 2:
            beli_item()
        elif pilihan == 3:
            tampilkan_xp_detail()
        elif pilihan == 0:
            print("Keluar game...")
            break
        else:
            print("Pilihan tidak tersedia!")

    except ValueError:
        print("Input harus angka!")