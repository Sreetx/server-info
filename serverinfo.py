import socket, time, sys

print ("#----------------------------------------------------------------#")
print ("<|----------------------| Server Info |-------------------------|>")
print (" | Author:             RX77E, Security Syber Team Indonean      |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print (" |--------------------------------------------------------------|")
print (" |    Jangan gunakan script ini untuk tindak kejahatan. Kami    |")
print (" |    tidak bertanggung jawab atas apapun yang anda lakukan.    |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

try:
    host = sys.argv[1]
except IndexError: print('\n [INFO] Ketikan '+sys.argv[0]+' target.com  untuk menjalankan script. Contoh: '+sys.argv[0]+' situsweb.com | Ingat tulis kepala alamat website tanpa https:// atau http://\n');sys.exit()

try:
    print('\n [*] Mencari Informasi....')
    
    user = socket.gethostname()
    
    print(' [*] Mendapatkan Informasi....\n')
    try:
        ip = socket.gethostbyname(host)
        print(' [*] Alamat IP: '+ip)
    except socket.error: print(' [!] Tidak dapat menampilkan alamat IP')
    try:
        port = socket.getservbyname(host)
        print(' [*] Port: '+port)
    except OSError: print(' [!] Tidak dapat menampilkan port')
    try:
        hosting = socket.gethostbyaddr(host)
        print(' [*] Layanan Penghosting: '+hosting)
    except socket.herror: print(' [!] Layanan penghosting tidak tersedia')
    try:
        proto = socket.getprotobyname(host)
        print(' [*] Protocol yang digunakan: '+proto)
    except OSError: print(' [!] Tidak dapat menampilkan protokol')
    print(' [*] Nama perangkat ini: '+user)
    print(' ');sys.exit()
 
except KeyboardInterrupt: print(' [!] Keluar dari program....');sys.exit()
except socket.error: print(' [!] Gagal mendapatkan informasi. Harap periksa koneksi internet anda\n');sys.exit()
    
