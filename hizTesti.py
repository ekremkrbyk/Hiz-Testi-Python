import speedtest
import pyfiglet
import requests
import socket

class HizTesti:
    def IslemYap(secim : int):
        if(secim == 1):
            print("\n")
            try: 
                con = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                con.settimeout(0)
                con.connect(('8.8.8.8',80))
                localIP = con.getsockname()[0] 
                response = requests.get("https://httpbin.org/ip")
                print(f"Makinenin IP adresi: {response.text[15:29]}")
                print(f"Dış IP adresi: {localIP}")
                test = speedtest.Speedtest()
                test.get_best_server()
                server = test.results.server
                print(f"{server['host']} sunucusuna bağlanıldı.\n")
                print(f"Ülke: {server['country']} -- {server['cc']} \n")

                print("Lütfen bekleyiniz veriler alınıyor..\n")

                dowloand = round(test.download() / 1_000_000, 2) # Veriyi Mbps cinsinden almak için 1,000,000 e bölüyoruz çünkü 1,000,000 bit/s (bps) = 1 Mb/s (MB)
                upload = round(test.upload() / 1_000_000, 2)
                ping = server['latency']

                print(f"İndirme hızı: {dowloand} MB/S \nYükleme hızı: {upload} MB/S \nPing: {ping} MS") 
                input("Çıkmak için herhangi bir tuşa basınız.")
            except Exception as e:
                print(e)
                print("Bir hata oluştu lütfen internet bağlantınızı kontrol edip tekrar deneyiniz.")

        else:
            print("Çıkış yapılıyor.")

print(pyfiglet.figlet_format("HOŞGELDİNİZ\n"))
secim = input("1/Hız Testi \nYapmak istediğiniz işlemi seçiniz: ")
if secim == "1":
    HizTesti.IslemYap(1)
else:
    print("Lütfen sadece rakam giriniz! ")
    
