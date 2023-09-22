#Guild Wars 2 ArcDps Tool Updated on 09/21/2023
#by vishnuk.5082

import requests
import os
import time
#import win32api
import psutil

def pathSearcher():
    drives = []
    allDrives = (psutil.disk_partitions())
    for elem  in allDrives:
        drives.append(elem.device)
    exe = "Gw2-64.exe"

    pathVar = ""
    for drive in drives: 
        print("Searching for GW2 Directory in Drive " + drive + " . . .")
        for root, dirs, files in os.walk(drive):
            for name in files:
                if name == exe:
                    pathVar = os.path.abspath(os.path.join(root, name))
                    print("Gw2-64.exe found at " + pathVar)
                    break

    if(pathVar == ""):
        print("Guild Wars 2 Could Not Be Found On Your Computer")
        input("The Program Will Now Exit . . .")
        exit()
    
    return pathVar

print("Welcome to Guild Wars 2 ArcDps Updater!")
print("by vishnuk.5082")
print(" ")
input("Press Any Key to Continue . . . ") 
gw2Path = ""
pathInput = input("Would you like to provide the Path for the GW2 Directory? (y/n): ")
if(pathInput == 'y' or pathInput == 'Y' or pathInput == 'yes' or pathInput == 'YES'): 
    print("Example: C:\Program Files (x86)\Guild Wars 2")
    gw2Path = input("Enter Path: ").strip() + '\Gw2-64.exe'
    if not os.path.exists(gw2Path):
        print("Path Does not Exist, Please Try Again")
    else:
        print("Gw2-64.exe found at " + gw2Path)
elif(pathInput == 'n' or pathInput == 'N' or pathInput == 'no' or pathInput == 'NO'):
    print("Proceeding to Search for GW2 on your Computer")
    print("This could take a few minutes, please don't close this window")
    gw2Path = pathSearcher()
else: 
    print("Invalid Input Received")
    print("Proceeding to Search for GW2 on your Computer")
    print("This could take a few minutes, please don't close this window")
    gw2Path = pathSearcher()


os.chdir(os.path.dirname(gw2Path))

print("Deleting old ArcDps DLL Files . . .")
try: 
    os.remove(os.getcwd() + '\d3d11.dll')
    os.remove(os.getcwd() + '\d3d11.dll.md5sum')
except:
    print("No DLL Files Found, Proceeding to Installation . . . ")

print("Installing new ArcDps DLL Files . . . ")


url = "https://www.deltaconnected.com/arcdps/x64/d3d11.dll"
r = requests.get(url, allow_redirects=True)
open('d3d11.dll','wb').write(r.content)

url ="https://www.deltaconnected.com/arcdps/x64/d3d11.dll.md5sum"
r = requests.get(url, allow_redirects=True)
open('d3d11.dll.md5sum','wb').write(r.content)

print("Installation Successful!")
print("The Program Will Now Exit . . . ")
time.sleep(2)
exit()
