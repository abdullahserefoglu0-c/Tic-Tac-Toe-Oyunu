from random import randrange

def TahtayiGoster(tahta):
    """
    Bu fonksiyon, Tic-Tac-Toe tahtasının mevcut durumunu
    senaryoda belirtilen formatta ekrana basar.
    'tahta' parametresi, 3x3 bir liste olmalıdır.
    """
    print("+-------+-------+-------+")
    print("|       |       |       |")
    # tahta[satır][sütun] kullanarak hücrelere erişiyoruz
    print(f"|   {tahta[0][0]}   |   {tahta[0][1]}   |   {tahta[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {tahta[1][0]}   |   {tahta[1][1]}   |   {tahta[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {tahta[2][0]}   |   {tahta[2][1]}   |   {tahta[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def KullaniciHamlesi(tahta):
    """
    Kullanıcıdan ('O') hamlesini alır.
    Girişin geçerli (1-9 arası) ve boş bir kare olup olmadığını doğrular.
    Geçerliyse 'tahta' listesini günceller.
    """
    while True:
        try:
            # 1. Kullanıcıdan giriş al
            hamle_numarasi = int(input("Hamleni yap (1-9): "))
            
            # 2. Geçerli aralıkta mı kontrol et (1-9)
            if hamle_numarasi < 1 or hamle_numarasi > 9:
                print("Geçersiz hamle. Lütfen 1-9 arasında bir sayı girin.")
                continue
                
            # 3. Sayıyı (satır, sütun) koordinatlarına çevir
            # (hamle_numarasi - 1) çünkü listeler 0'dan başlar
            satir = (hamle_numarasi - 1) // 3 
            sutun = (hamle_numarasi - 1) % 3
            
            # 4. Karenin dolu olup olmadığını kontrol et
            # Eğer kare 'O' veya 'X' ise doludur
            if tahta[satir][sutun] in ['O', 'X']:
                print("Bu kare zaten dolu. Başka bir kare seçin.")
                continue
            
            # 5. Hamle geçerli, tahtayı güncelle ve döngüden çık
            tahta[satir][sutun] = 'O'
            break
            
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def BosKareleriBul(tahta):
    """
    Tahtadaki tüm boş kareleri tarar.
    Boş karelerin (satır, sütun) koordinatlarını bir liste olarak döndürür.
    Bu liste, bilgisayarın hamle seçimi ve beraberlik kontrolü için kullanılır.
    """
    bos_kareler = []
    # 0, 1, 2 değerleri için satırları döngüye al
    for satir in range(3):
        # 0, 1, 2 değerleri için sütunları döngüye al
        for sutun in range(3):
            # Eğer kare 'O' veya 'X' değilse, boştur (yani içinde sayı vardır)
            if tahta[satir][sutun] not in ['O', 'X']:
                bos_kareler.append((satir, sutun))
    return bos_kareler

def ZaferKontrolu(tahta, sembol):
    """
    Verilen 'sembol' ('X' veya 'O') için kazanma durumunu kontrol eder.
    Yatay, dikey ve çapraz tüm olasılıklara bakar.
    """
    # Yatay (satır) kontrolü
    for satir in range(3):
        if tahta[satir][0] == sembol and tahta[satir][1] == sembol and tahta[satir][2] == sembol:
            return True
            
    # Dikey (sütun) kontrolü
    for sutun in range(3):
        if tahta[0][sutun] == sembol and tahta[1][sutun] == sembol and tahta[2][sutun] == sembol:
            return True
            
    # Çapraz kontrol (sol üstten sağ alta)
    if tahta[0][0] == sembol and tahta[1][1] == sembol and tahta[2][2] == sembol:
        return True
        
    # Çapraz kontrol (sağ üstten sol alta)
    if tahta[0][2] == sembol and tahta[1][1] == sembol and tahta[2][0] == sembol:
        return True
        
    # Kazanma durumu yok
    return False

def BilgisayarHamlesi(tahta):
    """
    Bilgisayarın ('X') hamlesini yapar.
    Önce boş karelerin listesini alır (BosKareleriBul fonksiyonu ile),
    sonra bu listeden 'randrange' kullanarak rastgele bir kare seçer
    ve tahtayı 'X' ile günceller.
    """
    # 1. Boş kareleri bul
    bos_kareler = BosKareleriBul(tahta)
    
    # 2. Boş kare varsa...
    if bos_kareler:
        # 3. Rastgele bir index seç (0 ile 'boş kare sayısı - 1' arasında)
        rastgele_index = randrange(len(bos_kareler))
        
        # 4. O index'teki (satır, sütun) koordinatını al
        secilen_hamle = bos_kareler[rastgele_index] # Örn: (1, 2)
        satir = secilen_hamle[0]
        sutun = secilen_hamle[1]
        
        # 5. Tahtayı güncelle
        tahta[satir][sutun] = 'X'

# --- OYUNUN BAŞLANGICI (ANA PROGRAM) ---

# 1. Tahtayı (3x3 liste) ilk değerleriyle (sayılarla) oluştur
tahta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Göreve göre bilgisayar ('X') başlar ve her zaman ortayı (kare 5) alır.
# Kare 5, tahta[1][1]'e karşılık gelir.
tahta[1][1] = 'X'

# Oyun döngüsü
while True:
    # 3. Bilgisayarın son hamlesini (veya başlangıç durumunu) göster
    TahtayiGoster(tahta)
    
    # 4. Kullanıcıdan ('O') hamle al (ve tahtayı güncelle)
    KullaniciHamlesi(tahta)
    
    # 5. Kullanıcı kazandı mı diye kontrol et
    if ZaferKontrolu(tahta, 'O'):
        TahtayiGoster(tahta) # Kullanıcının kazanan son hamlesini göster
        print("Kazandın!")
        break
        
    # 6. Boş kare kalmadıysa (beraberlik kontrolü)
    # BosKareleriBul() boş bir liste döndürürse (if not ... True olur)
    if not BosKareleriBul(tahta):
        TahtayiGoster(tahta)
        print("Berabere!")
        break
        
    # 7. Bilgisayar ('X') hamlesini yapsın
    print("--- Bilgisayar Hamlesi ---")
    BilgisayarHamlesi(tahta)
    
    # 8. Bilgisayar kazandı mı diye kontrol et
    if ZaferKontrolu(tahta, 'X'):
        TahtayiGoster(tahta) # Bilgisayarın kazanan hamlesini göster
        print("Bilgisayar kazandı!")
        break
        
    # 9. Bilgisayarın hamlesinden sonra boş yer kalmadıysa berabere
    if not BosKareleriBul(tahta):
        TahtayiGoster(tahta) # Dolu tahtayı göster
        print("Berabere!")
        break

# Döngü bittiğinde oyun sona erer.