# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
s = xmlrpc.client.ServerProxy('http://192.168.0.102:8001')

# buka file yang akan diupload
with open("ENDGAME_U.jpg",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    data=xmlrpc.client.Binary(handle.read())


# panggil fungsi untuk upload yang ada di server
    s.file_upload(data)
    print('File berhasil diupload')