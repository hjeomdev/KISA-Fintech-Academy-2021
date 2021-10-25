from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver.get('https://www.eum.go.kr/web/am/amMain.jsp') # 토지 이음 페이지 열기

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]')) # select element 가져오기
# sidoSelect.select_by_visible_text('강원도') # 강원도로 설정

# work1: 전라남도 고흥군 고흥읍 남계리 45 - 1 번지의 데이터 스크래핑하기
sidoSelect.select_by_visible_text('전라남도')

driver.implicitly_wait(1) # 딜레이

sigunguSelect = Select(driver.find_element_by_xpath('//*[@id="selSgg"]')) 
sigunguSelect.select_by_visible_text('고흥군')

driver.implicitly_wait(1) # 딜레이

eubmyendongSelect = Select(driver.find_element_by_xpath('//*[@id="selUmd"]')) 
eubmyendongSelect.select_by_visible_text('고흥읍')

driver.implicitly_wait(1) # 딜레이

riSelect = Select(driver.find_element_by_xpath('//*[@id="selRi"]'))
riSelect.select_by_visible_text('남계리')

bonbunInput = driver.find_element_by_name('bobn')
bonbunInput.send_keys('45')

bubunInput = driver.find_element_by_name('bubn')
bubunInput.send_keys('1')

searchBtn = driver.find_element_by_xpath('//*[@id="frm"]/fieldset/div[3]/p/span/a')
searchBtn.click()

table = driver.find_element_by_xpath('//*[@id="appoint"]')
print(table.text)