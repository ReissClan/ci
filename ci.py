import amino
import random
import time
print("\033[0;31m"+"""   ___ ___  __  __ __  __ _   _ _  _ ___ _______   __
  / __/ _ \|  \/  |  \/  | | | | \| |_ _|_   _\ \ / /
 | (_| (_) | |\/| | |\/| | |_| | .` || |  | |  \ V / 
  \___\___/|_|  |_|_|  |_|\___/|_|\_|___| |_|   |_|  
                                                     """)
print("\033[0;34m"+"""  ___ _   ___     _____ _____ _____ ____  
 |_ _| \ | \ \   / /_ _|_   _| ____|  _ \ 
  | ||  \| |\ \ / / | |  | | |  _| | |_) |
  | || |\  | \ V /  | |  | | | |___|  _ < 
 |___|_| \_|  \_/  |___| |_| |_____|_| \_\.
                                          """)

time.sleep(0.5)
print("\n")
print("""
DARK KING (FRANCIS) & DASH ©®

YOUTUBE:
	Flame""")
time.sleep(0.5)
print("\n")
email=input("\033[0;32m"+"EMAIL: ")
time.sleep(0.5)
print("\n")
password=input("PASSWORD: ")
time.sleep(0.5)
print("\n")
print("\033[0;34m"+"[Loging in...]")
client=amino.Client()
client.login(email=email, password=password)
print("\033[0;32m"+"[LOGINED IN]")
time.sleep(0.5)
print("\n")
print("\033[0;31m")
		
print("ملاحضة مهمة: حط رابط اي دردشة بالمنتدى الي تبي تنشر فيه، لاتحط رابط المنتدى")
time.sleep(2)
print("\n")
link=input("\033[0;34m"+"THE LINK: ")
gpid=client.get_from_code(link)
chatid=gpid.objectId
comid=gpid.path[1:gpid.path.index("/")]
size=input("\033[0;36m"+"PUT HOW MUCH PEOPLE YOU WANT TO INVITE: ")
time.sleep(0.5)
print("\n")

subclient = amino.SubClient(comId=comid, profile=client.profile)
time.sleep(0.5)
print("\n")
en=(subclient.get_online_users(start=0,size=size).profile.userId)
time.sleep(0.5)
print("\n")
message=input("PUT THE MESSAGE: ")
kkkk=0
while True:
	try:
	    an=random.choice(en)
	    subclient.start_chat(userId=an, message=message)
	    en.remove(an)
	    kkkk+=1
	    print("\033[0;35m"+"[DONE]", kkkk)
	except:
	   print("\033[0;31m")
	   print("اذا طلعت هرسالة يعني صار خطأ، هل خطأ ممكن يكون انه تم حظرك وممكن يكون خلصوا اعضاء الاونلاين")
	   break
			
		
print("""
DARK KING (FRANCIS) & DASH ©®

YOUTUBE:
	Flame""")