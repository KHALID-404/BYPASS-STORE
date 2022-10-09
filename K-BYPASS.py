import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 

 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from BYPASS import khalid
 
        khalid()
 
 
 
elif bit == "32bit":
 
        from BYPASS import khalid
 
 
        khalid()
        
 
