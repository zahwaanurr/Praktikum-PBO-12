import datetime
import pytz

print("=============================")
nama = "Zahwa Nur Azkia Putri   |"
nim = "064002300038             |"
print("Nama:", nama)
print("NIM:", nim)
print("=============================")

def display_current_time():
    # Mendapatkan waktu UTC
    utc_now = datetime.datetime.now(pytz.utc)
    # Mengubah waktu UTC menjadi UTC+7 (Asia/Jakarta)
    jakarta_tz = pytz.timezone('Asia/Jakarta')
    jakarta_now = utc_now.astimezone(jakarta_tz)
    
    # Menampilkan waktu saat ini di timezone Asia/Jakarta
    print("Timezone : Asia/Jakarta")
    print("Tanggal : ", jakarta_now.strftime('%Y-%m-%d'))
    print("Waktu : ", jakarta_now.strftime('%H:%M:%S.%f')[:-3])  # Menghapus 3 digit terakhir untuk milidetik
    
    print("\nBerubah menjadi")
    
    # Mendapatkan waktu UTC kembali untuk melihat perubahan
    utc_now = datetime.datetime.now(pytz.utc)
    jakarta_now = utc_now.astimezone(jakarta_tz)
    
    # Menampilkan waktu yang baru di timezone Asia/Jakarta
    print("Tanggal : ", jakarta_now.strftime('%Y-%m-%d'))
    print("Waktu : ", jakarta_now.strftime('%H:%M:%S.%f')[:-3])  # Menghapus 3 digit terakhir untuk milidetik

if __name__ == "__main__":
    display_current_time()
