import random

nombor = int(input("masukkan umur anda: "))

if nombor >=13:
    print("Anda layak bermain")
    nama = str(input("Masukkan nama anda: "))
    print("hi", nama)
    
elif nombor <=13:
    print("Maaf anda tidak layak bermain")
    
print("mari bermain!")
print("kuprum - 29,",
      "ferum - 26,",
      "helium - 2,",
      "litium - 3,",
      "gallium - 31")

jadual = ["kuprum", "ferum", "helium", "litium", "gallium"]
rahsia = random.choice(jadual)

if rahsia == "helium":
    print ("Ia merupakan gas monoatom tidak berwarna, tidak berbau, tidak berasa dan tidak beracun ")
    
elif rahsia == "kumprum":
    print("Ia merupakan logam mulur yang mempunyai kekonduksian elektrik yang sangat baik")

elif rahsia == "ferum":
    print("merupakan salah satu daripada tiga oksida utama besi") 
    
elif rahsia == "litium":
    print("sejenis logam lembut, berwarna putih keperakan dan sangat aktif terhadap air dan udara")
    
elif rahsia == "gallium":
    print("digunakan untuk membuat aloi dalam termometer suhu tinggi dan digunakan sebagai semikonduktor komputer.")
    
teka = True

while teka:
    teka = str(input("Masukkan jadual berkala tekaan anda :"))
    if rahsia == teka:
        print ("Tahniah! Tekaan anda betul")
        print ("jadual berkala itu ialah", rahsia)
        teka = False
    elif rahsia != teka:
        print ("Maaf tekaan anda salah")
        
print("selamat tinggal!")
    