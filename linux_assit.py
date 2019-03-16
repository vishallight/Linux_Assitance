import os
import platform,datetime
	
from  selenium import webdriver
import webbrowser,pyttsx
import gmailf,wiki_file,sendmail
import speech_recognition as sr


greeting={"hey":"hey","hi":"hi","hello":"hello"}
r = sr.Recognizer()
											#FIND OS	
if platform.system()=="Windows":
	OS=1			#windows platform	selenium driver			
	driver_path= os.getcwd()+"/driver/windows/chromedriver.exe"
	clear=lambda:os.system("cls")
else:
	OS=0			#other Platform		selenium driver
	driver_path= os.getcwd()+"/driver/linux/chromedriver"
	
	clear=lambda:os.system("clear")			#clear()


def speak(wd):				#speak func
	engine=pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-30)	
	engine.say(wd)
	engine.runAndWait()

def salut():
    current_time = int(datetime.datetime.now().hour)
    print("All service are started,Ready")
    if current_time >= 0 and current_time < 12:
        speak('Good Morning!')

    if current_time >= 12 and current_time < 18:
        speak('Good Afternoon!')

    if current_time >= 18 and current_time !=0:
        speak('Good Evening!')
    speak("All service are started,Ready")   
	

def sysinfo():

	print("System   :"+ platform.system())
	print('Node     :'+ platform.node())
	print('Release  :'+ platform.release())
	print('Version  :'+ platform.version())
	print('Machine  :'+ platform.machine())
	print('Processor:'+ platform.processor())



def listen():
		
        with sr.Microphone() as source:
			try:															#ai name
				AI = open("ai_name.txt","r");   
				ai_name = AI.read();   
  
				if ai_name=="":  
					ai_name="Computer"  
				#for i in range (1):					#clear the main scren at first time
				#	clear()
				#	ban()
				#	print("All service are started,Ready")
					
				print(ai_name.replace("\n"," ") + ": ")
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				print(ai_name.replace("\n"," ") +": done")
			
			except IOError:
				print("Error in openning a ai_name File")
				speak("Error in openning a ai_name File")
				print("Rebuilding the ai_name File")
				speak("Rebuilding the ai_name File")
				print("Error Solved")
				speak("Error Solved")
				AI = open("ai_name.txt","w");   
				ai_name="Computer "
				spek()
				
			

        try:
	        cmd = r.recognize_google(audio)
	        print("User : {}".format(cmd))
			#os.system("espeak 'You said : {}'".format(cmd))
		speak("You said "+cmd)

        except sr.UnknownValueError:
					print("cann\'t hear your voice Properly")
					cmd = listen()
	return cmd


def gmail():
	try:
		url="https://www.gmail.com"
						
		driver=webdriver.Chrome(driver_path)		#drier chrome
		driver.get(url)
		print("Login to your gmail")
		#os.system("espeak 'Login to your gmail'")
		speak("Login to your gmail")
		#entering username & passwd
		driver.find_element_by_id("identifierId").send_keys(gmailf.username)
		driver.find_element_by_id("identifierNext").click()
		#time.sleep(5)
		driver.implicitly_wait(5)

		driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(gmailf.passwd)
		#for clicking ligin
		driver.find_element_by_id("passwordNext").click()


		driver.implicitly_wait(30)
		#logout in t-30
		#driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()
		#driver.find_element_by_xpath("//*[@id='gb_71']").click()
	except  :
		print("error in opening gmail")
		speak("error in opening gmail")
		spek()


def spek():
    #os.system("espeak 'how can i help you?'")
    
    
    while True:
		cmd=listen()			#listening the voice
		
		if 'exit' in cmd or 'Exit' in cmd  or 'goodbye' in cmd or 'see you later' in cmd :			#exit programm
			print("Goodbye,And see you later")			
			#os.system("espeak 'Goodbye'")
			speak("Goodbye, And see you later")
			break
			
		elif  "hi" in cmd or "what's up" in cmd or 'how are you' in cmd:
			if cmd=="hey" or "hi":
				print("what should i do  ?")
				speak("what should i do ?")
		
			elif "what's up" in cmd or 'how are you' in cmd:
				print ("i'm fine ")
				speak("i'm fine ")
				
			elif "hi" in cmd:
				print("yeah i'm here")
				speak("yeah i'm here")
		elif "open text editor" in cmd or "open Notepad" in cmd:
			print ("opening leafpad.......")
			speak("opening leafpad.......")
			#os.system("espeak 'opening leafpad' && gnome-terminal --command=leafpad")
			if OS==1:
				os.system("Notepad")
			else:
				os.system("gnome-terminal --command=leafpad")
		elif "execute dos" in cmd or "start dos" in cmd:
			for i in range(1,10):
					print("executing dos attack........ \n server crashing")
					speak(" executing dos attack    server crashing")
			speak("dos attack sucessfully executed   server crashed")
			for i in range (1,3):
					print("repeat server  down")
					speak("repeat server  down")
		elif "who are you" in cmd:
				print("i'm a computer program")
				#os.system("espeak 'i am a computer program'")
				speak("i'm a computer program")
				#break	

		elif "kill" in cmd:	
				print("closing program......see you later")
				speak("closing program ,see you later")
				#os.system("espeak 'closing program'")
				#os.system("exit")
				break
		elif "activate code 990" in cmd:
				if OS==0:	#linux
				 print("shutting system down.......")
				 speak("shutting system down ")
		      		 #os.system("espeak 'shutting system down'") 	 
				 os.system("poweroff")
				elif OS==1:					#windows
					 os.system("shutdown -l")
	
		elif "sleep" in cmd or "Sleep" in cmd or "screen off" in cmd:
			print("sleep .......")
			speak("sleep enabled,i'm gonna sleep ")
			os.system("gnome-screensaver-command -a")		#sleep the system
			
			
		elif "lock" in cmd or "Lock" in cmd or "lock the screen" in cmd:
			print("lock .......")
			speak("lock  enabled,system Locked")
			os.system("gnome-screensaver-command -l")		#lock the system
			
			
		elif "search" in cmd:									#browsing onn web
				
				val=cmd.find('search')					# val = to find the "search" place charcter number in  the sentence(ie:in cmd)
				#print(val)								print the "search" place no
				query=cmd[val+7:]						# only taking the words after the word "search" then the remaing string equal to "query"
				webbrowser.open("https://www.google.com/search?q="+query)				
				print("opening browser")
				speak("opening browser")
				#os.system("espeak 'opening browser'")
				print("searching "+query)
				#os.system("espeak 'searching {} '".format(query)) 	 	
				speak("searching "+query) 	 		
				#webbrowser.open("https://www.google.com/search?q="+query)
 

		
		elif "login my Gmail" in cmd or "login my mail" in cmd:				#gmail login in selenium
					
					print("opening browser")
					speak("opening browser")			
					#os.system("espeak 'opening browser'")
					gmail()					
					#print("Login to your gmail")				send to inside the fun to get perfect
					#os.system("espeak 'Login to your gmail'")
					print('Login sucessfully finished')
					speak('Login sucessfully finished')
					#os.system("espeak 'Login sucessfully finished' ")
		
		elif "talk to me" in cmd:
			 print("are sure?,i really wanna to say a story!")
			 speak("are sure?,i really wanna to say a story!")
			 with sr.Microphone() as source:
	              		print("yes or no")
	   			r.adjust_for_ambient_noise(source)
	  			audio = r.listen(source)
				try:			
			 		a = listen()
					if "yes " in a:
						print("A grasshopper walks into a bar, and the bartender says, Hey, we have a drink named after you! The grasshopper looks surprised and asks, You have a drink named Steve? ")
						speak("A grasshopper walks into a bar, and the bartender says, Hey, we have a drink named after you! The grasshopper looks surprised and asks, You have a drink named Steve? ")
					else:
						print("ok i didn't")	
						speak("ok i didn't")
						#os.system("espeak 'ok i didn't' ")
				except:
					pass

		elif "ping" in cmd:
			 
			 #os.system("espeak 'Target ip or Hostname '")
		       	 speak("Target ip or Hostname")
			 print("Target ip or Hostname")
			 speak()                          	   #ping="ping   "+ip
			 if OS==1:
				 ping="start ping"+cmd
			 else:
				ping="gnome-terminal --command='ping {}'".format(cmd)
			 print(ping)
			 os.system(ping)
				 
		
		elif "send mail" in cmd:			#mail sending
				val=cmd.find('to')	
				mail=cmd[val+3:]
				mail=mail.replace(" ",'')		#mail=to address
				print("what is Subject \n ")					
				speak("what is Subject")

				sub=listen()			#sub of teh mail
				print ("Done")
				print(sub)
				if "cancel" in sub:
					spek()				
				


				print("what is message ")					
				speak("what is message")
				try:
				   msg= listen()			#msg of teh mail
				   print ("Done")
				   if "cancel" in msg:
						spek()	
				   print(msg)				
				except sr.UnknownValueError:
						print('Sorry could not recognize the message')
						speak('Sorry could not recognize the message')
						#os.system("espeak 'Sorry could not recognize the message'")
						spek()	
				except sr.RequestError as e:
						print("cannot obtain results the message")
						speak("cannot obtain results the message")
						#os.system("espeak 'Sorry could not recognize the message'")
						spek()	
				resl=sendmail.send_mail(mail,sub,msg,driver_path)
				speak(resl)

		elif "who is " in cmd or "what is meant by " in cmd or "tell about " in cmd or "what is an " in cmd:
				if "who is " in cmd:				
					fin=cmd.find("who is")
					wrd=cmd[fin+7:]
					res=wiki_file.wiki(wrd)
					print(res)				
					speak(res)
				elif "what is meant by " in cmd:				
					fin=cmd.find("what is meant by")
					wrd=cmd[fin+16:]
					res=wiki_file.wiki(wrd)
					print(res)				
					speak(res)
				elif "tell about " in cmd:				
					fin=cmd.find("what is meant by")
					wrd=cmd[fin+11:]
					res=wiki_file.wiki(wrd)
					print(res)				
					speak(res)
					

		elif "screenshot" in cmd or "Screenshot" in cmd:
				leng=int((len(cmd))/2)
				pyautogui.screenshot("screenshot"+str(leng)+".png")

		elif "display command list" in cmd or "help" in cmd:
				clear()
				print("""Exit	kill	Open Text Editor \n Who are you	Activate code 990(power off code)	Search \n Login my Gmail	
				Talk to me		System informations		ping\n Send Mail	Who is	What is mean by \n Screenshot
				open my gmail	Hold on		Stop talking	 Talk back 	Back on 	Date 	Time	send mail to (reciver mail ID)		
				system info		system Details		Lock the system 	sleep 	Screen off""")

		elif "superb" in cmd or "you are awesome" in cmd :
				print(" thank you")
				speak(" thank you")
		elif "system info" in cmd or "system information" in cmd or "system details" in cmd:		#system details 
				print("Scaning the server, Details found ,here")
				speak("Scaning the server, Details found ,here")
				sysinfo()
		elif "time" in cmd:
				TIME()	
			
		elif "date" in cmd:
				DATE()
		elif "hold on" in cmd or "stop talking" in cmd:
			print("ok,I stop talking  ........ say BACK ON or TALK BACK to start talk again")
			speak("ok,I stop talking........ say BACK ON or TALK BACK to TALK") 
			while 1:
				rest=holdon()
				if "back on" in rest or "talk back" in rest:
					print("\n \t\tGood to hear you back")
					speak("Good to hear you back")
					spek()
				
		else:
			print("oh, I see.")
			speak("oh, I see.") 


def holdon():
		
		with sr.Microphone() as source:
			try:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				stop = r.recognize_google(audio)
			except sr.UnknownValueError:
						stop = holdon()
		return stop

def TIME():
	
	now = datetime.datetime.now()
	hr=str(now.hour)
	mi=str(now.minute)
	if mi=="0":
		mi="O Clock"
	
	time=hr+" Hours:"+mi+" Minutes"	 
	
	print(time)
	speak(hr+" "+mi)

def DATE():
	months=["January","February","March","April","May","June","July","August","September","October","November","December"]
	now = datetime.datetime.now()
	year=str(now.year)
	mont=str(now.month)
	day=str(now.day)

	month=months[int(mont)-1]
	
	date=month+" "+day+" "+year
	
	print(date)
	speak(month+" "+day+" "+year)


			    
def ban():
	print("         +-+      +")
	print("           | +-+  |   +-+")
	print("     +-+   |   |  |   |    +--+")
	print("       |   |   |  |   |    |")
	print("       |   |   |  |   |    |")
	print("   +---+---+---+--+---+----+----+")
	print("   |                            |")
	print("   |   +-------+     +-------+  |")
	print("+--+   |       |     |       |  +--+")
	print("|  |   |       |     |       |  |  |")
	print("|  |   |    +--+     |    +--+  |  |")
	print("+--+   |    |-@|     |    |-@|  +--+")
	print("   |   +-------+     +-------+  |")
	print("   |             +-+            |")
	print("   |             | |            |")
	print("   |             +-+            |")
	print("   |  +--+               +--+   |")
	print("   |    +-----------------+     |")
	print("   |          welcome           |")
	print("   +----------------------------+")
	print("")

def main():
	
	ban()
	salut()			#wishing
	spek()			#main pro starts
   


main()

	 






