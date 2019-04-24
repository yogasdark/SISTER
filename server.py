#DOWNLOAD
# import SimpleXMLRPCServer bagian serve_forever
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
# import xmlrpc bagian client
import xmlrpc.client

# buatlah fungsi bernama download()
def file_download():
    # buka file bernama "file_didownload.txt"
    with open("GOT.jpg",'rb') as handle:
        # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary()
        return xmlrpc.client.Binary(handle.read())

# buat fungsi bernama file_upload()
def file_upload(filedata):
    
    # buka file 
    with open("Endgame_nih.jpg",'wb') as handle:
        #convert from byte to binary IMPORTANT!
        data1=filedata.data
        
        # tulis file tersebut
        handle.write(data1)
        return True  #IMPORTANT
# else error messsage: "cannot marshal None unless allow_none is enabled"
    
print ("cannot marshal None unless allow_none is enabled")
       
# buat server pada IP dan port yang telah ditentukan
server = SimpleXMLRPCServer(("192.168.0.102", 8001))

# print bahwa "server mendengarkan pada port xxx"
print ("Listening on port 8001")

# register fungsi download pada server
server.register_function(file_download, 'file_download')

# register Fungsi upload
server.register_function(file_upload, 'file_upload')

# jalankan server
server.serve_forever()