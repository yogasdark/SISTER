# import SimpleXMLRPCServer bagian serve_forever
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# buat fungsi bernama file_upload()
def file_upload(filedata):
    
    # buka file 
    with open("hasil_upload.txt",'wb') as handle:
        #convert from byte to binary IMPORTANT!
        data1=filedata.data
        
        # tulis file tersebut
        handle.write(data1)
        return True  #IMPORTANT
        
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"
    
    print ("cannot marshal None unless allow_none is enabled")
# buat server
server = SimpleXMLRPCServer( ("10.30.40.62", 8002) )
	                          
# tulis pesan server telah berjalan
print("Server telah berjalan..")

# register fungsi 
server.register_function(file_upload, 'file_upload')

# jalankan server
server.serve_forever()