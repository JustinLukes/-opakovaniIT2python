
import os,platform,random,sys







def clear(zadaní="None"):
    input("Press any key to Continue...")
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#definici clear() neřeste. Chci aby Clear Fungoval na Windowsu a na Linuxu :)



jméno = "Justin Jindřich"
příjmení = "Lukes"
print(f"{jméno} {příjmení}")
clear()
while True:
    try:
        věk = int(input("Zadejte svůj věk:"))
        break
    except ValueError:
        print("Tohle není číslo")

clear()
print(f"Délka {jméno} {příjmení} je {len(jméno) + len(příjmení)}")
clear()

a = 6
for x in range(0,5):
    a += 6
    print(a)
print(f"výsledek proměné (A) je {a}") 

clear()
while True:
    while True:
        try:
            věk = int(input("Zadejte svůj věk:"))
            print("děkuji")
            break
        except ValueError:
            print("Zadej jen celočíselnou hodnotu.")

    clear()
    hodnota = random.randint(0,10)
    print(f"{hodnota}")
    clear()
    hodnotau = input("Zadej svou hodnotu :")
    if hodnotau == hodnota:
        break

