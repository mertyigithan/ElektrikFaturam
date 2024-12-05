# Fonksiyon:
def elektrikFaturasi():
    tuketim_miktari = float(input("Eğer biliyorsanız, hesaplamak istediğiniz aydaki elektrik tüketiminizi kWh cinsinden giriniz. Elektrik tüketiminizi bilmiyorsanız lütfen 0 giriniz: "))
    if tuketim_miktari != 0:
        enerji_birim_fiyat = 1.859 # TL (Kasım 2024)
        enerji_bedeli = tuketim_miktari * enerji_birim_fiyat
        ETV = enerji_bedeli * 0.015 # Elektrik ve Havagazı Tüketim Vergisi
        KDV = enerji_bedeli * 0.1 # Katma Değer Vergisi
        fatura_tutari = enerji_bedeli + ETV + KDV
        print(f"Elektrik fatura tutarınız: {round(fatura_tutari, 2)} TL")
    else:
        yeni_alet = ""
        while yeni_alet != "sonuç":
            yeni_alet = input("Lütfen eklemek istediğiniz elektrikli ev aletinin adını giriniz. Aynı cihazdan birden fazla ekleyebilirsiniz. Ekleme işlemini sonlandırmak için 'sonuç' yazabilirsiniz: ")
            if yeni_alet == "sonuç":
                print(f"Yaklaşık elektrik tüketiminiz: {tuketim_miktari / 1000} kWh")
                enerji_birim_fiyat = 1.859 # TL (Kasım 2024)
                enerji_bedeli = (tuketim_miktari / 1000) * enerji_birim_fiyat
                ETV = enerji_bedeli * 0.015 # Elektrik ve Havagazı Tüketim Vergisi
                KDV = enerji_bedeli * 0.1 # Katma Değer Vergisi
                fatura_tutari = enerji_bedeli + ETV + KDV
                print(f"Tahmini elektrik fatura tutarınız: {round(fatura_tutari, 2)} TL")
            else:
                haftalik_kullanim = int(input("Bu elektrikli aleti haftada kaç gün çalıştırdığınızı giriniz: "))
                gunluk_sure = float(input("Bu elektrikli aleti günde kaç saat çalıştırdığınızı giriniz: "))
                # Elektrikli Ev Aletleri:
                if yeni_alet == "televizyon" or yeni_alet == "tv":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 50)
                elif yeni_alet == "buzdolabı":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 21)
                elif yeni_alet == "çamaşır makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 750)
                elif yeni_alet == "elektrikli süpürge" or yeni_alet == "elektrik süpürgesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 750)
                elif yeni_alet == "bulaşık makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 840)
                elif yeni_alet == "ütü":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 2400)
                elif yeni_alet == "saç kurutma makinesi" or yeni_alet == "fön makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1750)
                elif yeni_alet == "klima":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1080)
                elif yeni_alet == "fırın":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 2150)
                elif yeni_alet == "mikrodalga" or yeni_alet == "mikrodalga fırın":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 800)
                elif yeni_alet == "dizüstü bilgisayar" or yeni_alet == "laptop":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 75)
                elif yeni_alet == "masaüstü bilgisayar" or yeni_alet == "bilgisayar":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 150)
                elif yeni_alet == "aspiratör":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 20)
                elif yeni_alet == "elektrikli radyatör" or yeni_alet == "elektrikli kalorifer":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 2500)
                elif yeni_alet == "telefon şarjı" or yeni_alet == "telefon şarj aleti":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 5)
                elif yeni_alet == "kettle":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1500)
                elif yeni_alet == "tost makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1500)
                elif yeni_alet == "çamaşır kurutma makinesi" or yeni_alet == "kurutma makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1000)
                elif yeni_alet == "led ampul" or yeni_alet == "ampul":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 7)
                elif yeni_alet == "floresan ampul":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 36)
                elif yeni_alet == "elektrikli şofben" or yeni_alet == "şofben":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 6600)
                elif yeni_alet == "kahve makinesi":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 800)
                elif yeni_alet == "playstation 4" or yeni_alet == "ps4":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 90)
                elif yeni_alet == "elektrikli ocak" or yeni_alet == "ocak":
                    tuketim_miktari = tuketim_miktari + (4 * haftalik_kullanim * gunluk_sure * 1300)

# Çalıştır:
elektrikFaturasi()