from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver.get('https://www.melon.com/chart/index.htm') # 멜론 차트 페이지 열기

title = driver.find_element_by_xpath(
    '//*[@id="frm"]/div/table'
)
print(title.text)