import random
namaPlayernya = input("Masukkan nama player: ")
player = {
    "nama": namaPlayernya,
    "darah": 100,
    "energy": 50,
    "coin": 100,
    "inventory": []
}

def player_status():
    print(f"Nama        : {player['nama']}")
    print(f"Darah       : {player['darah']}")
    print(f"Energy      : {player['energy']}")
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
    print(f"\n⚔️  Kamu menghadapi {enemy['name']}! HP musuh: {enemy['hp']}, Serangan: {enemy['attack']}")

    while enemy['hp'] > 0 and player['darah'] > 0:
        print(f"\nDarahmu: {player['darah']}, Energy: {player['energy']}")
        action = input("Pilih aksi: (1) Serang (2) Lari: ")

        if action == "1":
            damage = random.randint(10, 25)
            enemy['hp'] -= damage
            print(f"Kamu menyerang {enemy['name']} dan memberikan {damage} damage!")
            
            if enemy['hp'] <= 0:
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
        
        else:
            print("Aksi tidak valid.")
    
    if player['darah'] <= 0:
        print("Darahmu habis. Game Over!")
        exit()
def beli_item():
    print("\nToko Item:")
    items = {"Potion": 20, "Pedang": 50, "Perisai": 40}
    for item, price in items.items():
        print(f"{item}: {price} coin")
    
    choice = input("Pilih item yang ingin dibeli: ")
    if choice in items:
        if player['coin'] >= items[choice]:
            player['coin'] -= items[choice]
            player['inventory'].append(choice)
            print(f"Kamu membeli {choice}!")
        else:
            print("Coin tidak cukup!")
    else:
        print("item tidak tersedia!")
    
while True:
    player_status()
    print("Pilih aksi:")
    print("1. Lawan enemy | 2. Beli Item | ")
    try:
        pilihan = int(input("Masukkan nomor aksi (1-4): 0 untuk keluar: "))
        if pilihan == 1:
            bertarung()
        if pilihan == 0:
            print("Keluar!")
            break
    except ValueError:
        print("Input tidak valid. Masukkan nomor.")
        continue

