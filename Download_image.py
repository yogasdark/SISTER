# import xmlrpc bagian client
import xmlrpc.client
# buat proxy untuk mengakses server. Gunakan parameter URL server yang akan diakses berupa IP dan port. Bentuk http://IP:port
proxy = xmlrpc.client.ServerProxy('http://192.168.0.102.8001')

# buat/buka file baru dengan nama "hasil_download.txt" sebagai hasil download dari server
with open("GOT_download.jpg","wb") as handle:
    handle.write(proxy.file_download().data)
 
    # tulis/isi file hasil_download.jpg dengan hasil dari memanggil fungsi "download" yang berada server
    #with write("hasil_download.jpg", "wb") as handle:
    # ubah file menjadi binary dengan menambahkan .data