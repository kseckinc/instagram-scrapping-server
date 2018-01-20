from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time,random,names,os,requests,sys
from seleniumwire import webdriver
from random_username.generate import generate_username

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
global DELAYS,CREDS,driver,proxyauth_plugin_path,proxy

import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium import webdriver

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


display = Display(visible=0, size=(800, 600))
display.start()


CREDS={}
DELAYS={
        "keys_min":50,# Delays in miliseconds
        "keys_max":200,
        "min":200,
        "max":1000,
        }


def getProxy():
    a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=US&anonymity=elite&ssl=true').json()
    while a['protocol'] not in ['https','socks4','socks5']:
        a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=US&anonymity=elite&ssl=true').json()
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
    ]
    return random.choice(a)

def startDriver():
    print('------ startDriver init')
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 600))
    display.start()
    opts = webdriver.ChromeOptions()
    opts.binary_location = "/usr/bin/google-chrome"
    opts.add_argument(f'--proxy-server={self.proxy}')
    opts.add_extension(os.getcwd()+"/Proxy Auto Auth.crx")
    opts.add_argument("--proxy-server=http://nataly.ltespace.com:15584")
    opts.add_argument("user-agent=%s" % self.agent())
    opts.add_argument('--disable-gpu')
    # opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    capabilities = DesiredCapabilities.CHROME
    self.driver = webdriver.Chrome(chrome_options=opts, desired_capabilities=capabilities,executable_path=f'{BASE_DIR}/chromedriver')
        
    print('------ driver started')



def openLogin():
    print('open login')
    try:
        driver.get('https://www.instagram.com/accounts/login/')
        print('login page')
        time.sleep(4)
        driver.find_element_by_name("username")
        return True
    except:
        return False

def login(un,pw):
    print('---------- def login init')

    x=openLogin()
    while not x:
        x=openLogin()
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    driver.find_element_by_name("username").send_keys(un)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    driver.find_element_by_name("password").send_keys(pw)
    time.sleep(random.randint(DELAYS["min"], DELAYS["max"])/100.0)
    driver.find_element_by_xpath('''//div[contains(text(),"Log In")]''').click()
    time.sleep(10)

def searchUser(name):
    print('---------- def searchUser init')

    open(os.getcwd()+"/dmlog.txt","a").write('Seraching followers of %s \n' % name)
    driver.get('https://www.instagram.com/accounts/onetap')
    time.sleep(4)
    driver.find_element_by_xpath('''//input[@placeholder='Search']''').send_keys(name)
    time.sleep(2)
    for i in driver.find_elements_by_xpath('//div/a'):
        link=i.get_attribute('href')
        if link=='https://www.instagram.com/':
            pass
        else:
            profileLink=link
            print(profileLink)
            break
    if profileLink[-1]=="/":
        profileLink=profileLink[:-1]
    driver.get(profileLink)
    time.sleep(5)
    driver.find_element_by_xpath('''//a[@href='/%s/followers/']''' % (profileLink.split("/")[-1])).click()
    time.sleep(5)
    driver.find_elements_by_xpath('//div/ul/div/li')[0].click()
    while 1:
        x=len(driver.find_elements_by_xpath('//div/ul/div/li'))
        
        for i in range(500):
            try:
                driver.find_elements_by_xpath('//div/ul/div/li')[-1].click()
            except:
                pass
            ActionChains(driver).send_keys(Keys.DOWN).perform()
        y=len(driver.find_elements_by_xpath('//div/ul/div/li'))
        if not y>x:
            break
    print("Found %d Followers"%(len(driver.find_elements_by_xpath('//div/ul/div/li'))))
    open(os.getcwd()+"/dmlog.txt","a").write("Found %d Followers"%(len(driver.find_elements_by_xpath('//div/ul/div/li'))))
    return driver.find_elements_by_xpath('//div/ul/div/li//span/a')

def dm(user,message):
    print('---------- direct mesasge init')
    driver.get("https://www.instagram.com/"+user)
    time.sleep(5)
    try:
        driver.find_element_by_xpath('''//button[contains(text(),"Message")]''').click()
    except:
        try:
            driver.find_element_by_xpath('''//button[contains(text(),"Follow")]''')
        except:
            print("Cant Send Message")
            open(os.getcwd()+"/dmlog.txt","a").write('Cant send DM to %s \n' % user)
            raise Exception("Cant Send Message")
    time.sleep(5)
    try:
        driver.find_element_by_xpath('''//button[contains(text(),"Not Now")]''').click()
    except:
        pass
    time.sleep(2)
    for i in message:
        driver.find_element_by_xpath('''//textarea[@placeholder='Message...']''').send_keys(i)
        time.sleep(random.randint(DELAYS["keys_min"], DELAYS["keys_max"])/1000.0)
    time.sleep(2)
    driver.find_element_by_xpath('''//button[contains(text(),"Send")]''').click()
    open(os.getcwd()+"/dmlog.txt","a").write('DM send successfully to %s \n' % user)
    

def getFollowers(name):
    print('---------- def getFollowers init')
    un='sajith8827'
    pw='36SJ7QBUphCCkY9'
    startDriver()
    login(un,pw)
    return searchUser(name)

def sendDM(user,message,un,pw):
    print('---------- def sendDM init')

##    un='sajith8827'
##    pw='36SJ7QBUphCCkY9'
    un=un
    pw=pw
    startDriver()
    login(un,pw)
    try:
        for i in user:
            open(os.getcwd()+"/dmlog.txt","a").write('Sending DM to %s \n' % i)
            dm(i,message)
            
        return True
    except:
        return False

# open(os.getcwd()+"/dmlog.txt","a").write('Starting' )
# us=sys.argv[1]
# msg=sys.argv[2]
# un=sys.argv[3]
# pw=sys.argv[4]
# x=getFollowers(us)
# x=list(map(lambda y:y.text, x))
# sendDM(x,msg,un,pw)
#x=getFollowers("shanaka")
    
