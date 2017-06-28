import socket
import sys
import hashlib
import datetime
import threading

shas=[]
dire={}
direT={}
i=0
p=0
q=0
minute=0
   
def proxysock(sock,s,adddr,i,p,q,minute):                               # FUNCTION TO PASS INTO THREAD
    try:
        data=client.recv(size)                                          #  RECEIVE DATA
    except:                                      
        return                                                          
    print("CLIENT REQUEST:")
    print
    print(data)
    if data:
        get=[]
        for row in data:
            if row:
                ext=[]
                data1=data.split('\r')
                print(data1)
                print
            
                x=[]
                z=3
                ext=data1[0].split('/')
                print(ext)
                if len(ext)>2:
                    while z<=(len(ext)-1):
                        x.append('/'+ext[z])
                        z=z+1
                    print("XXXXXXXXXXXX:",x)
                
                y=''.join(x)
                print("YYYYYYYYYYYYYYY:",y)
                print("EXT:",ext)
                print
                req=data1[1]
                hst=req.split(' ')
                host=hst[1]
                get=data1[0].split(' ')
                print
                print("REQUEST TYPE:",get[0])
                break
    else:
        return    

    if get[0]!="GET":                                                   # IGNORE OTHER REQUESTS THAN GET
        print
        print("INCORRECT METHOD REQUESTS")
        print
        return
    else:
     
        with open("req.txt",'wb') as file:
            file.write(data)
            
        def replace_line(file_name, line_num, text):                        #REPLACE A GET REQUEST LINE 
            
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
            
        replace_line('req.txt', 0, 'GET '+y+'\n')
            
        url=data1[0][11:]
       
        print("URL:",url)

        hash=hashlib.sha256()
        hash.update(url)
        sha=hash.hexdigest()
        print(sha)
        print(shas)
        print(i)
        
        if i!=0 and sha in shas:                                       #SEND THE DATA IF CACHED BEFORE
            
            print(host)
            print(dire.keys())
            if host in dire.keys():
                print(dire[host])
               
                client.sendto(dire[host],(localhost,9876))
                print
                print("SHA AND CACHE FOUND")
                print
                print(dire[host])
                print
                print("DIRECTORY DATA IS SENT TO CLIENT")
                
            
        else:
            print
            print("SHA:",sha)
            print
            shas.append(sha)                                                  # STORE SHA IN A LIST
            
            def TIME(host):                                                    # TIMEOUT FOR CACHE
                
                minute=datetime.datetime.now().minute
                print("MINUTE:",minute)
                direT.update({host:minute})
                for host in direT.keys():
                    if minute>=direT[host]+2:
                        del direT[host]
            
            TIME(host)
                
            print
            print("CACHE LIST:",shas)
            #p=p+1
            print
            print("CACHE LENGTH:",p)
            print
            print("HOSTNAME:",host)
            #I=0
            try:
                print(host)
                I=socket.gethostbyname(host)                                 #GET IP OF HOST
                print
                print(I)
                print
            except:
                print
                print("ERROR:COULD NOT GET IP")
                print
                
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # CREATE A NEW SOCKET TO SEND DATA TO SERVER
            prt=80     
            server_address=(I,prt)
            s.connect(server_address)    
            fh=open("req.txt")
            fh=fh.read()
            print
            print("TO BE SENT:")
            print
            print(fh)        
            
            s.sendto(fh,server_address)
            
            fil=s.recv(size)
            s.close()                                                   #RECEIVE SERVER RESPONSE
            while fil:
                print
                print("SERVER RESPONSE:")
                print
                print(fil)
                print
                break
            
            dire.update({host:fil})                                         # STORE SERVER RESPONSE TO DIRECTORY
            #q=q+1
            print
            print(dire.keys())
            print
            print("DIRECTORY LENGTH:",q)
            
            hstaddr=(localhost,port)
            try:
                client.sendto(fil,hstaddr)
            except socket.error:
                return
            print    
            print("REQUESTED WEBPAGE IS SENT TO CLIENT")
            print
               
        
if len(sys.argv)==2:
    data=sys.argv[1]
    data1=data.split('&')
    port=data1[0]
    port=int(port)
    print
    print'PORT NUMBER:',port
    print
else:
    print("PORT NUMBER ARGUMENT IS MISSING")
    sys.exit()
    
localhost=''                  
size=999999
adddr=(localhost,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                #socket
sock.bind((localhost,port))                                       
sock.listen(10)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
print("SOCKET IS BIND")
print
print("SOCKET IS NOW LISTENING.....")
print

while True:
    
    client,address=sock.accept()
    #threading.Thread(target=proxysock, args=(sock,s,adddr,i,p,q,minute)).start()    #IMPLEMENTING THREAD    
    
    proxysock(sock,s,adddr,i,p,q,minute)    
    i=i+1
    p=p+1
    q=q+1