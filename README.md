# PythonSQL

Python içinde SQL kullanımına dair örnek proje. Bu projede SQLite kullanılarak Python ile veritabanı işlemlerinin nasıl yapılacağı gösterilmektedir.

---

## İçindekiler

- `main.py` — Python kodu; SQLite veritabanına bağlanma, tablo oluşturma, veriler ekleme, sorgu yapma gibi işlemleri içerir.  
- `students.db` — SQLite formatındaki veritabanı dosyası; `main.py` tarafından kullanılan örnek öğrenci verileri içeriyor.  
- `README.md` — (bu dosya) projenin amacı, kurulumu ve nasıl çalıştırılacağı hakkında bilgi verir.

---

## Amaç

Bu projenin amacı:

- Python içinde SQL’in nasıl kullanılacağını göstermek;  
- Özellikle **SQLite** kütüphanesi ile; tablo oluşturma, CRUD (Create, Read, Update, Delete) işlemleri, sorgulama gibi temel veritabanı işlemlerini örneklemek;  
- SQL verilerini daha detaylı okuma ve tekrar kullanılabilir şekilde nasıl organize edilebileceğini göstermek.

---

## Gereksinimler

- Python 3.x  
- `sqlite3` kütüphanesi (Python standard kütüphanesi içinde geliyor)  
- İstersen `venv` gibi bir sanal ortam

---

## Kurulum ve Çalıştırma

1. Bu depoyu klonla:

   ```bash
   git clone https://github.com/dnzhnycl/PythonSQL.git
   ```

2. Proje dizinine gir:

   ```bash
   cd PythonSQL
   ```

3. (İsteğe bağlı) sanal ortam oluştur:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

4. Gerekli kütüphaneler varsa yükle (bu projede özel bir bağımlılık yok):

   ```bash
   pip install -r requirements.txt
   ```

   > Not: `requirements.txt` yoksa bu adımı atla.

5. `main.py` dosyasını çalıştır:

   ```bash
   python main.py
   ```

   Bu işlem `students.db` veritabanını kullanarak tablo oluşturacak, örnek öğrencileri ekleyecek ve bazı sorgular yapacaktır.

---

## Ne Öğrenebilirsiniz?

- Python’da `sqlite3` modülü ile çalışmayı  
- Veritabanı oluşturma (CREATE TABLE), veri ekleme (INSERT), veri güncelleme (UPDATE), veri silme (DELETE) gibi işlemleri  
- SQL sorgularını Python içinden nasıl çalıştıracağınızı  
- Veritabanı bağlantısını güvenli şekilde açma/kapatma mantığı  
- Veritabanı dosyası ile kodun birlikte nasıl kullanılabileceği

---

## Yapı

```
PythonSQL/
├── main.py
├── students.db
└── README.md
```

- `main.py` — Python ile SQL işlemlerini gösteren asıl betik.  
- `students.db` — örnek veritabanı.  
- `README.md` — proje ile ilgili açıklamalar.

---

## Katkıda Bulunma

Eğer bu projeyi geliştirmek istersen:

- Yeni SQL örnekleri ekleyebilirsin (join’ler, transaction’lar, performans optimizasyonları vs.)  
- Farklı veritabanlarına destek ekleyebilirsin (örneğin PostgreSQL, MySQL)  
- Kodun yorumlarını (docstring) ve hata yakalamaları (exception handling) geliştirebilirsin  

---

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Dilediğin gibi kullanabilir, değiştirebilir ve dağıtabilirsin.
