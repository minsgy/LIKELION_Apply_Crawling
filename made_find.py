from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import json

def Login_Page_Connection(browser):
    browser.find_element_by_xpath("/html/body/main/div/div/div/div/a/button").send_keys(Keys.ENTER)

def Id_Password_Submit(browser):
    with open('secret.json') as token:
        json_data = json.loads(token.read())
        APPLY_ID = json_data["APPLY_ID"] # APPLY_ID
        APPLY_PW = json_data["APPLY_PW"] # APPLY_PW

    browser.find_element_by_id('id_username').send_keys(APPLY_ID)
    browser.find_element_by_id('id_password').send_keys(APPLY_PW)
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div/div/form/div[3]/button').click()

def User_append(browser):
    # 지원자 리스트 담기
    global user_list
    test = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[3]')
    user = test.text.split('\n')
    for i in range(len(user)//4):
        user_list.append(user[0+i*4:4+i*4])


def apply_page_click(browser, number):
    global information
    browser.find_element_by_xpath(f'//*[@id="likelion_num"]/div[3]/a[{number}]').click()
    name = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[1]/h3').text
    phone_number = browser.find_element_by_xpath('//*[@id="likelion_num"]/div[2]/div[2]/p[1]').text
    information.append([name, phone_number]) # 지원자 이름, 휴대폰 번호 저장
    browser.back() # 페이지 뒤로가기


''' 메인 함수 '''

user_list = [] # 지원자 리스트 저장 (학번/이름/학과/합불상태)
information = [] # CSV에 들어 갈 상태 (이름/전화번호/합불상태)

browser = webdriver.Chrome('./chromedriver') # 셀레니움 크롬드라이브 실행
browser.get("https://apply.likelion.org/") # Url
Login_Page_Connection(browser) # 로그인 전 지원하기 버튼 클릭.
Id_Password_Submit(browser) # 로그인 페이지에서 로그인 하기

browser.find_element_by_xpath('//*[@id="likelion_num"]/div[2]/a/button').send_keys(Keys.ENTER) # 로그인 후, 지원자 리스트 페이지 버튼 클릭

User_append(browser) # 지원자 리스트 저장함.

for i in range(len(user_list)):
    apply_page_click(browser, i+1) # 지원자의 이름/전화번호를 추가하는 함수
    information[i].append(user_list[i][3]) # 해당 지원자의 합불 여부를 추가합니다.

browser.quit()

''' Pandas CSV 파일 생성 파트 '''
dataFrame = pd.DataFrame(information,  columns=['이름','전화번호', '합불 여부']) 
dataFrame = dataFrame.sort_values(by=['합불 여부', '이름']) # 합불 여부 정렬 후, 이름 순 정렬(ㄱ,ㄴ,ㄷ,ㄹ)
dataFrame.to_csv('UserList.csv', sep=',', index = False) # CSV 파일 생성 , 구분자','
