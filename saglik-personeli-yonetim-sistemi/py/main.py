import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        # Personel nesneleri
        personel1 = Personel(1, "Ahmet", "Yılmaz", "Muhasebe", 6000)
        personel2 = Personel(2, "Ayşe", "Kara", "İK", 7000)
        print(personel1)
        print(personel2)

        # Doktor nesneleri
        doktor1 = Doktor(3, "Mehmet", "Demir", "Cerrahi", 12000, "Genel Cerrahi", 10, "Hastane A")
        doktor2 = Doktor(4, "Selin", "Aydın", "Kardiyoloji", 11000, "Kardiyolog", 5, "Hastane B")
        doktor3 = Doktor(5, "Ali", "Vural", "Pediatri", 10000, "Çocuk Doktoru", 3, "Hastane C")
        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire nesneleri
        hemsire1 = Hemsire(6, "Fatma", "Çelik", "Acil", 5000, 40, "Sertifika A", "Hastane A")
        hemsire2 = Hemsire(7, "Murat", "Güneş", "Yoğun Bakım", 5500, 45, "Sertifika B", "Hastane B")
        hemsire3 = Hemsire(8, "Zeynep", "Büyük", "Pediatri", 5200, 42, "Sertifika C", "Hastane C")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta nesneleri
        hasta1 = Hasta(9, "Cem", "Yıldız", "1990-05-12", "Gribal Enfeksiyon", "İlaç Tedavisi")
        hasta2 = Hasta(10, "Ece", "Arslan", "1985-07-23", "Kırık", "Alçı")
        hasta3 = Hasta(11, "Kemal", "Durmaz", "1992-08-14", "Ameliyat", "Cerrahi Müdahale")
        print(hasta1)
        print(hasta2)
        print(hasta3)

        # Pandas DataFrame
        data = {
            "Personel No": [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no()],
            "Ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad()],
            "Soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad()],
            "Departman": [personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman()],
            "Maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas()],
            "Uzmanlik": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None],
            "Deneyim Yılı": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None],
            "Hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane()],
            "Çalışma Saati": [None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati()],
            "Sertifika": [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika()],
            "Hasta No": [None, None, None, None, None, None, None, None],
            "Doğum Tarihi": [None, None, None, None, None, None, None, None],
            "Hastalık": [None, None, None, None, None, None, None, None],
            "Tedavi": [None, None, None, None, None, None, None, None]
        }

        df = pd.DataFrame(data)

        # Boş olan değişken değerleri için 0 atayınız.
        df.fillna(0, inplace=True)
        print(df)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplayınız ve yazdırınız.
        doktor_uzmanlik_grup = df[df["Uzmanlik"] != 0].groupby("Uzmanlik").size()
        print("Doktor Uzmanlık Grupları ve Sayıları:")
        print(doktor_uzmanlik_grup)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulunuz.
        deneyimli_doktorlar = df[(df["Deneyim Yılı"] != 0) & (df["Deneyim Yılı"] > 5)].shape[0]
        print(f"5 yıldan fazla deneyime sahip doktor sayısı: {deneyimli_doktorlar}")

        # Hasta adına göre DataFrame'i alfabetik olarak sıralayınız ve yazdırınız.
        hasta_df = pd.DataFrame({
            "Hasta No": [hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "Ad": [hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
            "Soyad": [hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
            "Doğum Tarihi": [hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
            "Hastalık": [hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
            "Tedavi": [hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
        })
        hasta_df_sorted = hasta_df.sort_values(by="Ad")
        print("Alfabetik sıraya göre hastalar:")
        print(hasta_df_sorted)

        # Maaşı 7000 TL üzerinde olan personelleri bulunuz ve yazdırınız.
        yuksek_maas_personeller = df[df["Maas"] > 7000]
        print("Maaşı 7000 TL üzerinde olan personeller:")
        print(yuksek_maas_personeller)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösteriniz ve yazdırınız.
        hasta_df["Doğum Tarihi"] = pd.to_datetime(hasta_df["Doğum Tarihi"])
        yeni_dogumlu_hastalar = hasta_df[hasta_df["Doğum Tarihi"].dt.year >= 1990]
        print("1990 ve sonrası doğumlu hastalar:")
        print(yeni_dogumlu_hastalar)

        # Var olan DataFrame'den ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini içeren yeni bir DataFrame elde ediniz ve yazdırınız.
        yeni_df = df[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yılı", "Hastalık", "Tedavi"]]
        print("Yeni DataFrame:")
        print(yeni_df)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()