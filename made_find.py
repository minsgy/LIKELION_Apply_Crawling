
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Login_Page_Connection(browser):
    browser.find_element_by_xpath("/html/body/main/div/div/div/div/a/button").send_keys(Keys.ENTER)

def Id_Password_Submit(browser):
    browser.find_element_by_id('id_username').send_keys('28@likelion.org')
    browser.find_element_by_id('id_password').send_keys('37599397')
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div/div/form/div[3]/button').click()

def apply_page_click(browser, number):
    global information
    browser.find_element_by_xpath(f'//*[@id="likelion_num"]/div[3]/a[{number}]').click()
    name = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[1]/h3').text
    phone_number = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[2]/div[2]/p[1]').text
    information.append([name, phone_number])
    browser.back()


browser = webdriver.Chrome('./chromedriver')
information = []

# url
browser.get("https://apply.likelion.org/")
Login_Page_Connection(browser)
Id_Password_Submit(browser)

# 로그인 후, 지원자 리스트 페이지 버튼 클릭
browser.find_element_by_xpath('//*[@id="likelion_num"]/div[2]/a/button').send_keys(Keys.ENTER)

test = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[3]')

user = test.text.split('\n')
user_list = []

for i in range(len(user)//4):
    user_list.append(user[0+i*4:4+i*4])

for i in range(len(user_list)):
    apply_page_click(browser, i+1)
    information[i].append(user_list[i][3])

print(information)
