import random
#game multiplayer
x = 0 #game starter
pencacah = []
pencacah_utama = []
print("Tebak Bilangan")

def GameMultiP(pemain):
    global pencacah
    pencacah = 0
    n = random.randint(1,999999999999)
    print(f"\n{pemain} giliranmu")
    while True:
        usr = int(input("Masukkan bilangan tebakanmu: "))
        pencacah += 1
        if n == usr:
            print(f"Selamat {pemain}, tebakanmu benar")
            print(f"skor: {pencacah}")
            break
        elif n > usr:
            print(f"Lebih keatas")
        elif n < usr:
            print(f"Lebih kebawah")
        else:
            print("Terjadi kesalahan")
        pencacah_utama.append(pencacah)

if x == 0:
    pemain1 = input("Type in player 1 name: ")
    x += 1
GameMultiP(pemain1)
