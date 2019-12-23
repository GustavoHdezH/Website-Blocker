import time
from datetime import datetime as dt 
"""
    host files for windows  windows c:\windows\system32\drivers\etc
    host files for linux & Mac /ect/hosts
"""
# list paths
hosts_path_system = r"C:\Windows\System32\drivers\etc\hosts"
host_dir = hosts_path_system
#host_dir = "hosts" local
redir = "127.0.0.1"

# list websites to block 
websites_list =[
    "www.facebok.com",
    "www.youtube.com",
    "www.google.com.mx"
]
# Define working hours 
from_hour = 7
to_hour = 16

#Main Program 
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("En hora de trabajar: Bloqueo Activo ")
        with open(host_dir, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redir + " " + website + "\n")
    else:
        with open(host_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Es hora de relajarse: Bloqueo Desactivado")
    time.sleep(1) #Seconds