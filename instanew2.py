from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time,random,names,os,requests,sys
#from seleniumwire import webdriver
from random_username.generate import generate_username

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
global DELAYS,CREDS,driver,proxyauth_plugin_path

import undetected_chromedriver as uc
sys.path.append(os.getcwd())

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

class Insta:
    def __init__(self,delays,proxy):
        self.proxy=proxy
        self.DELAYS= delays
        self.CREDS={}
        self.verified = False
##        DELAYS={
####                "keys_min":50,# Delays in miliseconds
##                "keys_max":1000,
##                "min":200,
##                "max":2000,
##                }

    



    def getProxy(self):
        a=requests.get('api v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
        while a['protocol'] not in ['https','socks4','socks5']:
            a=requests.get('https://api.proxyflow.io/v1/proxy/random?token=c9997120aae549e43c4b45a3&country=RU&anonymity=elite&ssl=true').json()
        return a


    def agent(self):
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

    def startDriver(self):
        print ("Using proxy : %s" % self.proxy)
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
        print ("Using proxy : http://qtsdugh7:f2cc5y3t@regina.ltespace.com:16890")  
        opts = webdriver.ChromeOptions()
        opts.binary_location = "/usr/bin/google-chrome"
        opts.add_argument(f'--proxy-server={self.proxy}')
        PROXY = "nataly.ltespace.com:15584"
        opts.add_extension(os.getcwd()+"/Proxy Auto Auth.crx")
        opts.add_argument("--proxy-server=http://nataly.ltespace.com:15584")
        opts.add_argument("user-agent=%s" % self.agent())
        opts.add_argument('--disable-gpu')
        # opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        # opts.headless = True
        capabilities = DesiredCapabilities.CHROME
        # self.driver = webdriver.Chrome(options=opts, enable_console_log=True,desired_capabilities=capabilities, executable_path=)
        self.driver = webdriver.Chrome(chrome_options=opts, desired_capabilities=capabilities,executable_path=f'{BASE_DIR}/chromedriver')
        # self.driver.get("chrome-extension://ggmdpepbjljkkkdaklfihhngmmgmpggp/options.html")
        
        # self.driver.find_element_by_id("login").send_keys("4eeebfug")
        # self.driver.find_element_by_id("password").send_keys("vwmqx4qk")
        # self.driver.find_element_by_id("retry").clear()
        # self.driver.find_element_by_id("retry").send_keys("2")

        self.driver.find_element_by_id("save").click()

    def getNumber(self):
        req = requests.get('http://simsms.org/priemnik.php?metod=get_number&country=KG&service=opt16&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i')
        print('----------request', req)
        print('----------request text', req.text)
        print('----------request content', req.content)
        return req.json()

    def setStatus(self,orderId):
        return requests.get(f'http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id={orderId}&status=1').text

    def getStatus(self,orderId):
        return requests.get(f'http://simsms.org/priemnik.php?metod=get_sms&country=KG&service=opt16&id={orderId}&apikey=JBg460AFkOwR4bMIxoETSaiytVol6i').json()

    def banNumber(self,orderId):
        return requests.get(f'http://api2.5sim.net/stubs/handler_api.php?api_key=fe58de3b584c4cbf93fd5df36fbb1efb&action=setStatus&id={orderId}&status=10').text
    
    def generateDetails(self):
        print('-------------1 ge')
        passw=''
        f= open(f"{os.getcwd()}/facebook-firstnames.txt")
        for i in range(random.randint(1,2000)):
            line=f.readline()
        passw+=line
        passw+=random.choice(['.', '-',''])
        print('-----------2-- ge')

        for i in range(random.randint(1,3)):
            passw+=chr(random.choice(range(64,90)))
        print('---------3---- ge')

        for i in range(random.randint(1,1000)):
            line=f.readline()
        passw+=line
        passw+=str(random.randint(10,2020))
        print('----------4--- ge')

        for i in range(random.randint(0,2)):
            passw+=chr(random.choice(range(43,47)))
        print('--------5----- ge')

        if len(passw)>10:
            passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
        else:
            passw[0]=passw[0].upper()
            passw=passw[:10]+random.choice(['#', '$','&','*','!',".",'',''])
        f= open(f"{os.getcwd()}/facebook-firstnames.txt")
        for i in range(random.randint(1,2000)):
            line=f.readline()
            fname=line
        print('----------6--- ge')
            
        f= open(f"{os.getcwd()}/facebook-lastnames.txt")
        for i in range(random.randint(1,2000)):
            line=f.readline()
            lname=line
            
        year=random.randint(1980,1999)
        print('-------7------ ge')
        
        user_name=fname+"_"+lname+str(year)
        print('-------8------ ge')

        tp=self.getNumber()
        # tp='1234567'

        print('-------9------ ge')

        telephone = "+996"+str(tp['number'])
        # telephone = "+996"+tp

        print('-------10------ ge')

        #setStatus(orderId)
        print('------telephone', telephone)
        
        self.CREDS['username']=user_name
        self.CREDS['password']=passw
        self.CREDS['lname']=lname
        self.CREDS['fname']=fname
        self.CREDS['year']=year
        print('-------11------ ge')

        self.CREDS['telephone']=telephone
        self.CREDS['orderId']=tp['id']
        # self.CREDS['orderId']=tp

        print('---------', self.CREDS['username'])
        

        
    def fillName(self):
        fname=self.CREDS['fname']
        lname=self.CREDS['lname']
        print ("Filling Full name")
        open(os.getcwd()+"/accountlog.txt","a").write("Filling Full name\n")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('fullName')).perform()
        for i in fname+" "+lname:
            self.driver.find_element_by_name('fullName').send_keys(i)
            time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        
        
    def fillUsername(self):
        user_name=self.CREDS['username']
        print ("Filling username")
        open(os.getcwd()+"/accountlog.txt","a").write("Filling username "+ user_name.strip()+'\n')
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('username')).perform()
        for i in user_name:
            self.driver.find_element_by_name('username').send_keys(i)
            time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)

    def fillPassword(self):
        password=self.CREDS['password']
        print ("Filling password : "+password)
        open(os.getcwd()+"/accountlog.txt","a").write("Filling password : "+password.strip() + "\n")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('password')).perform()
        for i in password:
            self.driver.find_element_by_name('password').send_keys(i)
            time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)

    def fillTelephone(self):
        print ("Filling email")
        open(os.getcwd()+"/accountlog.txt","a").write("Filling email\n")
        # self.driver.implicitly_wait(3)
        # print('--,--,', self.driver.page_source)
        print('--,--,', self.driver.current_url)
        self.driver.save_screenshot('screenie.png')
        email_or_phone = self.driver.find_element_by_name('emailOrPhone')
        self.driver.implicitly_wait(3)
        telephone=self.CREDS['telephone']
        print('---telephone', telephone)
        # print('--- dir', dir(self.driver))
        # print('--- drive', self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(email_or_phone).perform()
        print('--------yeaaaaaaapppppppppppp thanks Allah')
        for i in telephone:
            self.driver.find_element_by_name('emailOrPhone').send_keys(i)
            time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)

    def submit(self):

        try:
            self.driver.find_element_by_xpath('''//p[contains(text(),"This username isn")]''')
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('username')).perform()
            print('----------------qqqqqqqqqqqqqqqqqqqqqqqq')
            for i in str(random.randint(10,100)):
                self.driver.find_element_by_name('username').send_keys(i)
                time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
        except:
            print('-------except--1')
            pass
        time.sleep(random.randint(3,5))
        try:
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            time.sleep(random.randint(3,5))
        except:
            print('-------except--2')

            pass

    def verify(self):
        
        verified=False
        for i in range(12):
            code=self.getStatus(self.CREDS['orderId'])
            print(code)
            open(os.getcwd()+"/accountlog.txt","a").write(str(code)+'\n')
            if 'text' in code.keys() and code['text']!=None:
                self.driver.switch_to.default_content()
                print(code['text'] + "   OK")
                otp= ''.join(list(map(lambda x: x if ord(x)>=48 and ord(x)<=57 else '',code['text'])))
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_name('confirmationCode')).perform()
                for i in otp:
                    self.driver.save_screenshot('confirm.png')
                    self.driver.find_element_by_name('confirmationCode').send_keys(i)
                    time.sleep(random.randint(self.DELAYS["keys_min"], self.DELAYS["keys_max"])/1000.0)
                verified=True
                print('-------------confirmation code verified')
                
                # v = self.driver.find_element_by_xpath('//button[@type="submit"]')
                time.sleep(3)
                # v.click()
                # time.sleep(1)
                self.verified = True
                self.driver.save_screenshot('ventry.png')
                break
                # return 'Varification True'
            time.sleep(10)
        if not verified:
            open(os.getcwd()+"/accountlog.txt","a").write("OTP not received\n")
            raise Exception("OTP not received")
        
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''')).perform()
        self.driver.find_element_by_xpath('''//button[contains(text(),"Confirm")]''').click()
        time.sleep(2000)
        
    def birthday(self):
        print ("Filling birthday")
        open(os.getcwd()+"/accountlog.txt","a").write("Filling birthday\n")
        self.driver.switch_to.default_content()
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        self.driver.save_screenshot('sc.png')
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@title='Month:']")).perform()
        self.driver.find_element_by_xpath(f"//select[@title='Month:']/option[@value='{random.randint(1,12)}']").click()
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@title='Day:']")).perform()
        self.driver.find_element_by_xpath(f"//select[@title='Day:']/option[text()='{random.randint(1,30)}']").click()
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//select[@title='Year:']")).perform()
        self.driver.find_element_by_xpath(f"//select[@title='Year:']/option[text()='{self.CREDS['year']}']").click()
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        self.driver.find_element_by_xpath('''//button[contains(text(),"Next")]''').click()
        
    def createAccount(self):
        print ("Generating Telephone number")
        open(str(os.getcwd())+"/accountlog.txt","a").write("Generating Telephone number\n")
        self.generateDetails()
        print ("Loading Instagram")
        open(os.getcwd()+"/accountlog.txt","a").write("Generating Telephone number\n")
##        self.driver.get('https://www.google.com/search?sxsrf=ALeKk023EYkddJRZlnlbMQFj10_JmMCycw%3A1603723429555&source=hp&ei=peCWX4LgH5Lt9QOLgJJI&q=Instagram+English&oq=Instagram+English&gs_lcp=CgZwc3ktYWIQAzIFCAAQyQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCC46BwgjEOoCECdQ-LIGWPiyBmDBtgZoAXAAeACAAdMBiAHTAZIBAzItMZgBAKABAqABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwjCxtaqv9LsAhWSdn0KHQuABAkQ4dUDCAY&uact=5')
##        time.sleep(4)
##        self.driver.find_element_by_xpath('''//span[contains(text(),"Instagram")]''').click()
        self.driver.get('https://www.instagram.com/?hl=en')
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''')).perform()
            self.driver.find_element_by_xpath('''//button[contains(text(),"Accept")]''').click()
            time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        except:
            pass
        time.sleep(random.randint(3,5))
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''')).perform()
            self.driver.find_element_by_xpath('''//span[contains(text(),"Sign up")]''').click()
        except:
            # self.driver.get('https://chromedriver.chromium.org/')
            self.driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
        
        time.sleep(random.randint(2,4))
        time.sleep(random.randint(self.DELAYS["min"], self.DELAYS["max"])/100.0)
        self.fillTelephone()
        self.fillName()
        self.fillUsername()
        self.fillPassword()
        self.submit()
        self.birthday()
        self.verify()
        print('------------------------------------------------------------------------------')
        print('###############################################################################')
        self.driver.save_screenshot('finish.png')
        self.driver.close()
    def generate(self):
        try:   
            self.startDriver()
            self.createAccount()
            print("Account Created Successfully")
            open(os.getcwd()+"/accountlog.txt","a").write("Account Created Successfully\n")
            return self.CREDS
        except Exception as e:
            print (e)
            open(os.getcwd()+"/accountlog.txt","a").write(str(e)+"\n\n")
            try:
                os.system(f"rm {os.getcwd()}/account.lock")
            except:
                pass
            return False
        open(os.getcwd()+"/accountlog.txt","a").write("\n\n")

# if __name__ == '__main__':
#     d={"keys_min":int(sys.argv[1]),"keys_max":int(sys.argv[2]),"min":int(sys.argv[3]),"max":int(sys.argv[4])}
#     a=Insta(d,sys.argv[5])
#     for i in range(int(sys.argv[6])):
#         a.generate()
