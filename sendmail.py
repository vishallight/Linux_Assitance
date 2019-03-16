from selenium import webdriver
import gmailf

def send_mail(mail,sub,msg,driver):
	try:
		#to=" 	"
		#sub="Testing"
		#msg="woking fine ......."
		driver=webdriver.Chrome(driver)

		url="https://gmail.com"
		driver.get(url)
		driver.find_element_by_id("identifierId").send_keys(gmailf.username)
		driver.find_element_by_id("identifierNext").click()

		driver.implicitly_wait(9)

		driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(gmailf.passwd)
		#for clicking ligin
		driver.find_element_by_id("passwordNext").click()


		#compose click
		#driver.find_element_by_xpath("//*[@id=':kg']/div/div").click()
		driver.find_element_by_css_selector(".z0").click()	
		driver.implicitly_wait(3)

		driver.find_element_by_name("to").send_keys(mail)				#to address

		driver.find_element_by_name("subjectbox").send_keys(sub)		#subject

		driver.find_element_by_css_selector(".Al ").send_keys(msg)		#message

		driver.find_element_by_css_selector(".aoO").click()			#click to send
		print("mail sucessfully Sent")
		return "mail sucessfully Sent"
	except :
		print("Username or Password Incorrect , pls check the gmailf.py change the username and Password")
		return "Username or Password Incorrect , pls check the gmailf.py change the username and Password"
			

