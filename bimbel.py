import json, os, time, datetime

BIMBEL = "data_murid.json"

def clean():
    os.system('cls')

def read_json():
    try: 
        with open(BIMBEL, 'r') as output:
            data = json.load(output)
        return data
    except FileNotFoundError:
        blank_data = []
        with open(BIMBEL, 'w') as output:
            json.dump(blank_data, output, indent = 4)
        return blank_data

def write_json(data):
    with open(BIMBEL, 'w') as output:
        json.dump(data, output, indent = 4)

def login():
    clean()
    username = input("Silahkan masukkan namamu : ")
    password = input("Silahkan masukkan passwordmu : ")
    user = read_json()

    status_login = False
    if len(user) != 0:
        for row in user:
            if row["username"] == username and row["password"] == password: 
                status_login = True
    else:
        print("Wah rupanya kamu masih belum mempunyai akun, nih! Silahkan daftar terlebih dahulu, ya!")
        time.sleep(5)
        main()

    if status_login:
        clean()
        print("Selamat " + username + "! Kamu berhasil login. Selamat belajar " + username + "!")
        print("Tanggal : ", datetime.datetime.now())
        lesson()
    else:
        print("Mohon maaf! Kamu gagal login. Silahkan masukkan kembali nama dan password dengan benar, ya!")
        time.sleep(5)
        main() 

def register():
    clean()
    username = input("Masukkan namamu untuk didaftar : ")
    password = input("Masukkan passwordmu untuk didaftar : ")
    user = read_json()
    
    register_data = {
        "username" : username,
        "password" : password
    }

    user.append(register_data)
    write_json(user)
    print("Selamat! Kamu berhasil register! Silahkan login untuk melanjutkan proses belajarmu, ya!")
    time.sleep(5)
    main()

def logout():
    clean()
    username = input("Masukkan namamu : ")
    password = input("Masukkan passwordmu : ")
    user = read_json()
    logout_data = {
        "username" : username,
        "password" : password
    }

    status_logout = False
    
    if len(user) != 0:
        for row in user:
            if row["username"] == username and row["password"] == password: 
                status_logout = True
    else:
        print("Wah saat ini kamu tidak dapat logout dari sistem, nih! Rupanya kamu tidak memiliki akun. Silahkan mendaftar terlebih dahulu, ya!")
        time.sleep(3)
        main()

    if status_logout:
        clean()
        user.remove(logout_data)
        write_json(user)
        print("Selamat! Data kamu telah logout dari sistem! Terima kasih!")
        print("Tanggal : ", datetime.datetime.now())
        time.sleep(5)
        main()
    else:
        print("Mohon maaf! Kamu gagal logout. Silahkan masukkan kembali nama dan password dengan benar, ya!")
        time.sleep(3)
        main() 


def about():
    clean()
    print("""
    Tentang Gater Course

    Selamat datang Gaters di bimbel online! Gater Course menyediakan platform belajar yang dikhususkan kepada murid SMP
    yang akan menjalani Ujian Nasional (UN) di akhir tingkat SMP. Gater Course akan menemani masa sekolah kalian untuk 
    membantu para Gaters berjuang dalam langkah lolos masuk SMA impian kalian! Selamat belajar Gaters!

    0. Kembali ke awal
    """)
    tentang = input("""
    Silahkan memasukkan angka [0]: """)
    if tentang == "0":
        main()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        about()

def lesson():
    clean()
    pelajaran = input("""
    Halo Gaters! Mau belajar apa hari ini?
    1. Bahasa Indonesia
    2. Bahasa Inggris
    3. IPA
    4. Matematika
    5. Kembali ke awal
    
    Silahkan memilih angka [1] [2] [3] [4] [5] :
    """)

    if pelajaran == "1":
        time.sleep(3)
        indonesian()
    elif pelajaran == "2":
        time.sleep(3)
        english()
    elif pelajaran == "3":
        time.sleep(3)
        science()
    elif pelajaran == "4":
        time.sleep(3)
        mathematics()
    elif pelajaran == "5":
        main()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        lesson()

def indonesian():
    clean()
    materi1 = input("""
    Selamat datang di pelajaran Bahasa Indonesia!
    1. Teks Tantangan
    2. Teks Rekaman Percobaan
    3. Pidato
    4. Kembali ke pilihan pelajaran

    A = Materi
    B = Video
    C = Latihan Soal

    Silahkan pilih dengan format angka dan huruf untuk belajar. Contoh : 1A
    """)

    if materi1 == "1A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi1 == "1B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi1 == "1C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi1 == "2A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi1 == "2B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi1 == "2C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi1 == "3A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi1 == "3B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi1 == "3C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi1 == "4":
        time.sleep(3)
        lesson()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        indonesian()

def english():
    clean()
    materi2 = input("""
    Selamat datang di pelajaran Bahasa Inggris!
    1. Descriptive Text
    2. Recount Text
    3. Functional Text
    4. Kembali ke pilihan pelajaran

    A = Materi
    B = Video
    C = Latihan Soal

    Silahkan pilih dengan format angka dan huruf untuk belajar. Contoh : 1A
    """)

    if materi2 == "1A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi2 == "1B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi2 == "1C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi2 == "2A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi2 == "2B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi2 == "2C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi2 == "3A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi2 == "3B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi2 == "3C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi2 == "4":
        time.sleep(3)
        lesson()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        english()

def science():
    clean()
    materi3 = input("""
    Selamat datang di pelajaran Ilmu Pengetahuan Alam!
    1. Klasifikasi Makhluk Hidup
    2. Kemagnetan
    3. Bioteknologi
    4. Kembali ke pilihan pelajaran

    A = Materi
    B = Video
    C = Latihan Soal

    Silahkan pilih dengan format angka dan huruf untuk belajar. Contoh : 1A
    """)

    if materi3 == "1A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi3 == "1B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi3 == "1C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi3 == "2A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi3 == "2B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi3 == "2C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi3 == "3A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi3 == "3B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi3 == "3C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi3 == "4":
        time.sleep(3)
        lesson()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        science()

def mathematics():
    clean()
    materi4 = input("""
    Selamat datang di pelajaran Matematika!
    1. Kesebangunan
    2. Garis dan Sudut
    3. Peluang
    4. Kembali ke pilihan pelajaran

    A = Materi
    B = Video
    C = Latihan Soal

    Silahkan pilih dengan format angka dan huruf untuk belajar. Contoh : 1A
    """)

    if materi4 == "1A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi4 == "1B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi4 == "1C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi4 == "2A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi4 == "2B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi4 == "2C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi4 == "3A":
        print("Selamat belajar! kasih link ntar")
        time.sleep(6)
        lesson()
        if materi4 == "3B":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
        elif materi4 == "3C":
            print("Selamat belajar! kasih link ntar")
            time.sleep(6)
            lesson()
    elif materi4 == "4":
        time.sleep(3)
        lesson()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(5)
        mathematics()

def main():
    clean()
    
    print("-" * 35 + " GATER COURSE " + "-" * 35)
    print("""
    Selamat datang Gaters! Silahkan masukkan angka yang akan kamu pilih, ya!
    1. Tentang Gaters Course
    2. Login
    3. Register
    4. Logout""")
    print(" ")
    print("-" * 84)
    
    user_choice = input("""
    Silahkan memilih angka [1] [2] [3] [4] : """)
    
    if user_choice == "1":
        about()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        register()
    elif user_choice == "4":
        logout()
    else:
        print("Mohon cek kembali angka yang kamu masukkan! Terima kasih!")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()