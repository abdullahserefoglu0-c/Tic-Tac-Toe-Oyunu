# Tic-Tac-Toe (XOX) Oyunu - BOZ213 Ara Sınav Projesi

Bu proje, **BOZ213** dersi ara sınav ödevi kapsamında Python programlama dili kullanılarak geliştirilmiş, bilgisayara karşı oynanan bir Tic-Tac-Toe (XOX) oyunudur.

## 📝 Proje Hakkında

**Geliştirici:** Abdullah Şerefoğlu
**Öğrenci No:** 24040127
**Ders:** BOZ213
**Tarih:** Kasım 2025

Bu yazılımda kullanıcı, **'O'** sembolünü kullanarak bilgisayarın yönettiği **'X'** sembolüne karşı yarışır. Oyun mantığı, bilgisayarın stratejik olarak her zaman ortadaki kareden başlaması ve sonraki hamleleri rastgele yapması üzerine kuruludur.

## 🚀 Özellikler

* **İnsan vs Bilgisayar:** Oyun, kullanıcı ve bilgisayar arasında oynanır.
* **Otomatik Başlangıç:** Senaryo gereği bilgisayar ('X') oyuna her zaman tahtanın tam ortasındaki kareyi (5 numara) alarak başlar.
* **Rastgele Yapay Zeka:** Bilgisayar, ilk hamleden sonraki hamlelerini boş kareler arasından rastgele seçerek yapar (`random` modülü kullanılmıştır).
* **Hata Kontrolü:** Kullanıcının dolu kareye hamle yapması veya 1-9 aralığı dışında sayı girmesi engellenir.
* **Durum Analizi:** Oyunun kazananı (yatay, dikey, çapraz kontrolü) veya beraberlik durumu her hamlede otomatik hesaplanır.

## 🛠️ Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için:

1.  **Python Yüklü Olduğundan Emin Olun:** Bilgisayarınızda Python 3.x sürümü kurulu olmalıdır.
2.  **Projeyi İndirin:**
    ```bash
    git clone [https://github.com/abdullahserefoglu0-c/Tic-Tac-Toe-Oyunu.git](https://github.com/abdullahserefoglu0-c/Tic-Tac-Toe-Oyunu.git)
    ```
3.  **Dizine Girin ve Çalıştırın:**
    ```bash
    cd Tic-Tac-Toe-Oyunu
    python "BOZ213v01a01_Arasınav Projesi.py"
    ```

## 🎮 Oynanış

1.  Oyun başladığında bilgisayar otomatik olarak ortadaki kareyi alır.
2.  Siz, 1-9 arasındaki numaraları kullanarak boş bir kare seçersiniz.
3.  3 sembolü yan yana getiren kazanır.

---
