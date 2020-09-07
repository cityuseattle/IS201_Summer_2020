from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signup")
#find input id="firstName" and fill "Thomas" as firtname
firstname = browser.find_element_by_id('firstName')
firstname.send_keys ('Thomas')
#find input id="lastName" and fill "Anderson" as lastname
lastname = browser.find_element_by_id('lastName')
lastname.send_keys ('Anderson')
#find input id="username" and fill "Neo" as username
username = browser.find_element_by_id('username')
username.send_keys ('Neo')
#find input name="passwd" and fill "noPassword"
passwd = browser.find_element_by_class_name("passwd")
passwd.send_keys ('noPassword')
#find input name="ConfirmPasswd" and fill 'noPassword" in a confirm box
passwd = browser.find_element_by_class_name('confirmPasswd')
passwd.send_keys ('noPassword')
