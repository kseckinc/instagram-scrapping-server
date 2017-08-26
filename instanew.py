from selenium import webdriver
import time,random,names,os,requests,sys
from seleniumwire import webdriver
from random_username.generate import generate_username

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
global DELAYS,CREDS,driver,proxyauth_plugin_path

import undetected_chromedriver as uc

CREDS={}
DELAYS={
        "keys_min":50,# Delays in miliseconds
        "keys_max":200,
        "min":100,
        "max":800,
        }

sys.path.append(os.getcwd())



def getProxy():
    a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
    while a['protocol'] not in ['https','socks4','socks5']:
        a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
    return a


def agent():
    a=[
        
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',

    'Mozilla/5.0 (X11; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Mozilla/5.0 (Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    
    'Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',




##    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 YaBrowser/20.9.0 Yowser/2.5 Safari/537.36',
##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 YaBrowser/20.9.0 Yowser/2.5 Safari/537.36',
##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
##    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
##    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
##    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'


    ]
    return random.choice(a)

def startDriver():
    global driver

    print ("Using proxy : http://qtsdugh7:f2cc5y3t@regina.ltespace.com:16890")
    opts = Options()
    profile = webdriver.FirefoxProfile()

    profile.set_preference("dom.webnotifications.enabled", False)
    opts.add_argument(f'--proxy-server=http://qtsdugh7:f2cc5y3t@regina.ltespace.com:16890/')
    PROXY = "nataly.ltespace.com:15584"
    opts.add_extension(os.getcwd()+"/Proxy Auto Auth.crx")
    opts.add_argument("--proxy-server=http://nataly.ltespace.com:15584")
    opts.add_argument("user-agent=%s" % agent())
    opts.headless = True
    capabilities = DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=profile, options=opts, desired_capabilities=capabilities, executable_path=f'{BASE_DIR}/geckodriver')
    time.sleep(3)
    driver.get("chrome-extension://ggmdpepbjljkkkdaklfihhngmmgmpggp/options.html")

    driver.find_element_by_id("login").send_keys("4eeebfug")
    driver.find_element_by_id("password").send_keys("vwmqx4qk")
    driver.find_element_by_id("retry").clear()
    driver.find_element_by_id("retry").send_keys("2")

    driver.find_element_by_id("save").click()

def getNumber():
    return requests.get('http://simsms.org/priemnik.php?metod=get_number&country=KG&service=opt16&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i').json()

def setStatus(orderId):
    return requests.get('http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id=%s&status=1' % orderId).text

def getStatus(orderId):
    return requests.get('http://simsms.org/priemnik.php?metod=get_sms&country=KG&service=opt16&id=%s&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i' % orderId).json()

def banNumber(orderId):
    return requests.get('http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id=%s&status=10' % orderId).text
 
def generateDetails():
    passw=''
    f= open("facebook-firstnames.txt")
    for i in range(random.randint(1,2000)):
        line=f.readline()
    passw+=line
    passw+=random.choice(['.', '-',''])
    for i in range(random.randint(1,3)):
        passw+=chr(random.choice(range(64,90)))
    for i in range(random.randint(1,1000)):
        line=f.readline()
    passw+=line
    passw+=str(random.randint(10,2020))
    for i in range(random.randint(0,2)):
        passw+=chr(random.choice(range(43,47)))
    if len(passw)>10:
        passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
    else:
        passw[0]=passw[0].upper()
        passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
    f= open("facebook-firstnames.txt")
    for i in range(random.randint(1,2000)):
        line=f.readline()
        fname=line
        
    f= open("facebook-lastnames.txt")
    for i in range(random.randint(1,2000)):
        line=f.readline()
        lname=line
        
    year=random.randint(1980,1999)
    
    user_name=fname+"_"+lname+str(year)
    tp=getNumber()
    telephone = "+996"+tp['number']
    #setStatus(orderId)
    
    CREDS['username']=user_name
    CREDS['password']=passw
    CREDS['lname']=lname
    CREDS['fname']=fname
    CREDS['year']=year
    CREDS['telephone']=telephone
    CREDS['orderId']=tp['id']
    

    
def fillName():
    fname=CREDS['fname']
    lname=CREDS['lname']
    print ("Filling Full name")
    ActionChains(driver).move_to_element(driver.find_element_by_name('fullName')).perform()
    for i in fname+" "+lname:
        driver.find_element_by_name('fullName').send_keys(i)
        time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    
    
def fillUsername():
    user_name=CREDS['username']
    print ("Filling username")
    ActionChains(driver).move_to_element(driver.find_element_by_name('username')).perform()
    for i in user_name:
        driver.find_element_by_name('username').send_keys(i)
        time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

def fillPassword():
    password=CREDS['password']
    print ("Filling password : "+password)
    ActionChains(driver).move_to_element(driver.find_element_by_name('password')).perform()
    for i in password:
        driver.find_element_by_name('password').send_keys(i)
        time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

def fillTelephone():
    print ("Filling email")
    telephone=CREDS['telephone']
    ActionChains(driver).move_to_element(driver.find_element_by_name('emailOrPhone')).perform()
    for i in telephone:
        driver.find_element_by_name('emailOrPhone').send_keys(i)
        time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

def submit():

    try:
        driver.find_element_by_xpath('''//p[contains(text(),"This username isn")]''')
        ActionChains(driver).move_to_element(driver.find_element_by_name('username')).perform()
        for i in str(random.randint(10,100)):
            driver.find_element_by_name('username').send_keys(i)
            time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    except:
        pass
    time.sleep(random.randint(3,5))
    try:
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(random.randint(3,5))
    except:
        pass

def verify():
    
    verified=False
    for i in range(12):
        code=getStatus(CREDS['orderId'])
        print(code)
        if 'text' in code.keys() and code['text']!=None:
            driver.switch_to.default_content()
            print(code['text'] + "   OK")
            otp= ''.join(list(map(lambda x: x if ord(x)>=48 and ord(x)<=57 else '',code['text'])))
            ActionChains(driver).move_to_element(driver.find_element_by_name('confirmationCode')).perform()
            for i in otp:
                driver.find_element_by_name('confirmationCode').send_keys(i)
                time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
            verified=True
            break
        time.sleep(10)
    if not verified:
        raise Exception("OTP not received")
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''')).perform()
    driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''').click()
    time.sleep(2000)
    
def birthday():
    print ("Filling birthday")
    driver.switch_to.default_content()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Month:']")).perform()
    driver.find_element_by_xpath("//select[@title='Month:']/option[@value='%d']" % random.randint(1,12)).click()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Day:']")).perform()
    driver.find_element_by_xpath("//select[@title='Day:']/option[text()='%d']" % random.randint(1,30)).click()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Year:']")).perform()
    driver.find_element_by_xpath("//select[@title='Year:']/option[text()='%s']" % CREDS['year']).click()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    driver.find_element_by_xpath('''//button[contains(text(),"Next")]''').click()
    
def createAccount():
    print ("Generating Telephone number")
    generateDetails()
    print ("Loading Instagram")
    driver.get('https://www.instagram.com/?hl=en')
    try:
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''')).perform()
        driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''').click()
        time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    except:
        pass
    time.sleep(random.randint(2,4))
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''')).perform()
    driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''').click()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    fillTelephone()
    fillName()
    fillUsername()
    fillPassword()
    submit()
    birthday()
    verify()

try:   
    startDriver()
    createAccount()
except Exception as e:
    print (e)


















# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# import time,random,names,os,requests,sys
# from seleniumwire import webdriver
# from random_username.generate import generate_username

# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver import ActionChains

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.common.proxy import *
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# global DELAYS,CREDS,driver,proxyauth_plugin_path

# import undetected_chromedriver as uc

# CREDS={}
# DELAYS={
#         "keys_min":50,# Delays in miliseconds
#         "keys_max":200,
#         "min":100,
#         "max":800,
#         }

# sys.path.append(os.getcwd())



# def getProxy():
#     a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
#     while a['protocol'] not in ['https','socks4','socks5']:
#         a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
#     return a


# def agent():
#     a=[
        
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',

#     'Mozilla/5.0 (X11; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
#     'Mozilla/5.0 (Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
#     'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
#     'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    
#     'Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
#     'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
#     'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
#     'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',




# ##    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 YaBrowser/20.9.0 Yowser/2.5 Safari/537.36',
# ##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 YaBrowser/20.9.0 Yowser/2.5 Safari/537.36',
# ##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
# ##    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
# ##    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
# ##    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
# ##    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'


#     ]
#     return random.choice(a)

# def startDriver():
#     global driver

#     print ("Using proxy : http://qtsdugh7:f2cc5y3t@regina.ltespace.com:16890")  
#     opts = uc.ChromeOptions()
#     opts.add_argument(f'--proxy-server=http://qtsdugh7:f2cc5y3t@regina.ltespace.com:16890/')
#     PROXY = "nataly.ltespace.com:15584"
#     opts.add_extension(os.getcwd()+"/Proxy Auto Auth.crx")
#     opts.add_argument("--proxy-server=http://nataly.ltespace.com:15584")
#     opts.add_argument("user-agent=%s" % agent())
#     opts.headless = False
#     capabilities = DesiredCapabilities.CHROME
#     driver = uc.Chrome(options=opts, enable_console_log=True,desired_capabilities=capabilities)
#     time.sleep(3)
#     driver.get("chrome-extension://ggmdpepbjljkkkdaklfihhngmmgmpggp/options.html")

#     driver.find_element_by_id("login").send_keys("4eeebfug")
#     driver.find_element_by_id("password").send_keys("vwmqx4qk")
#     driver.find_element_by_id("retry").clear()
#     driver.find_element_by_id("retry").send_keys("2")

#     driver.find_element_by_id("save").click()

# def getNumber():
#     return requests.get('http://simsms.org/priemnik.php?metod=get_number&country=KG&service=opt16&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i').json()

# def setStatus(orderId):
#     return requests.get('http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id=%s&status=1' % orderId).text

# def getStatus(orderId):
#     return requests.get('http://simsms.org/priemnik.php?metod=get_sms&country=KG&service=opt16&id=%s&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i' % orderId).json()

# def banNumber(orderId):
#     return requests.get('http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id=%s&status=10' % orderId).text
 
# def generateDetails():
#     passw=''
#     f= open("facebook-firstnames.txt")
#     for i in range(random.randint(1,2000)):
#         line=f.readline()
#     passw+=line
#     passw+=random.choice(['.', '-',''])
#     for i in range(random.randint(1,3)):
#         passw+=chr(random.choice(range(64,90)))
#     for i in range(random.randint(1,1000)):
#         line=f.readline()
#     passw+=line
#     passw+=str(random.randint(10,2020))
#     for i in range(random.randint(0,2)):
#         passw+=chr(random.choice(range(43,47)))
#     if len(passw)>10:
#         passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
#     else:
#         passw[0]=passw[0].upper()
#         passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
#     f= open("facebook-firstnames.txt")
#     for i in range(random.randint(1,2000)):
#         line=f.readline()
#         fname=line
        
#     f= open("facebook-lastnames.txt")
#     for i in range(random.randint(1,2000)):
#         line=f.readline()
#         lname=line
        
#     year=random.randint(1980,1999)
    
#     user_name=fname+"_"+lname+str(year)
#     tp=getNumber()
#     telephone = "+996"+tp['number']
#     #setStatus(orderId)
    
#     CREDS['username']=user_name
#     CREDS['password']=passw
#     CREDS['lname']=lname
#     CREDS['fname']=fname
#     CREDS['year']=year
#     CREDS['telephone']=telephone
#     CREDS['orderId']=tp['id']
    

    
# def fillName():
#     fname=CREDS['fname']
#     lname=CREDS['lname']
#     print ("Filling Full name")
#     ActionChains(driver).move_to_element(driver.find_element_by_name('fullName')).perform()
#     for i in fname+" "+lname:
#         driver.find_element_by_name('fullName').send_keys(i)
#         time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    
    
# def fillUsername():
#     user_name=CREDS['username']
#     print ("Filling username")
#     ActionChains(driver).move_to_element(driver.find_element_by_name('username')).perform()
#     for i in user_name:
#         driver.find_element_by_name('username').send_keys(i)
#         time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

# def fillPassword():
#     password=CREDS['password']
#     print ("Filling password : "+password)
#     ActionChains(driver).move_to_element(driver.find_element_by_name('password')).perform()
#     for i in password:
#         driver.find_element_by_name('password').send_keys(i)
#         time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

# def fillTelephone():
#     print ("Filling email")
#     telephone=CREDS['telephone']
#     ActionChains(driver).move_to_element(driver.find_element_by_name('emailOrPhone')).perform()
#     for i in telephone:
#         driver.find_element_by_name('emailOrPhone').send_keys(i)
#         time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)

# def submit():

#     try:
#         driver.find_element_by_xpath('''//p[contains(text(),"This username isn")]''')
#         ActionChains(driver).move_to_element(driver.find_element_by_name('username')).perform()
#         for i in str(random.randint(10,100)):
#             driver.find_element_by_name('username').send_keys(i)
#             time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#     except:
#         pass
#     time.sleep(random.randint(3,5))
#     try:
#         driver.find_element_by_xpath('//button[@type="submit"]').click()
#         time.sleep(random.randint(3,5))
#     except:
#         pass

# def verify():
    
#     verified=False
#     for i in range(12):
#         code=getStatus(CREDS['orderId'])
#         print(code)
#         if 'text' in code.keys() and code['text']!=None:
#             driver.switch_to.default_content()
#             print(code['text'] + "   OK")
#             otp= ''.join(list(map(lambda x: x if ord(x)>=48 and ord(x)<=57 else '',code['text'])))
#             ActionChains(driver).move_to_element(driver.find_element_by_name('confirmationCode')).perform()
#             for i in otp:
#                 driver.find_element_by_name('confirmationCode').send_keys(i)
#                 time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
#             verified=True
#             break
#         time.sleep(10)
#     if not verified:
#         raise Exception("OTP not received")
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''')).perform()
#     driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''').click()
#     time.sleep(2000)
    
# def birthday():
#     print ("Filling birthday")
#     driver.switch_to.default_content()
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Month:']")).perform()
#     driver.find_element_by_xpath("//select[@title='Month:']/option[@value='%d']" % random.randint(1,12)).click()
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Day:']")).perform()
#     driver.find_element_by_xpath("//select[@title='Day:']/option[text()='%d']" % random.randint(1,30)).click()
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     ActionChains(driver).move_to_element(driver.find_element_by_xpath("//select[@title='Year:']")).perform()
#     driver.find_element_by_xpath("//select[@title='Year:']/option[text()='%s']" % CREDS['year']).click()
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     driver.find_element_by_xpath('''//button[contains(text(),"Next")]''').click()
    
# def createAccount():
#     print ("Generating Telephone number")
#     generateDetails()
#     print ("Loading Instagram")
#     driver.get('https://www.instagram.com/?hl=en')
#     try:
#         ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''')).perform()
#         driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''').click()
#         time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     except:
#         pass
#     time.sleep(random.randint(2,4))
#     ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''')).perform()
#     driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''').click()
#     time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
#     fillTelephone()
#     fillName()
#     fillUsername()
#     fillPassword()
#     submit()
#     birthday()
#     verify()

# try:   
#     startDriver()
#     createAccount()
# except Exception as e:
#     print (e)
