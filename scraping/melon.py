from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver.get('https://www.melon.com/chart/index.htm') # 멜론 차트 페이지 열기

table = driver.find_element_by_xpath(
    '//*[@id="frm"]/div/table/tbody'
) # 멜론 차트 테이블

tableRow = table.find_elements_by_tag_name('tr') # 차트 행 가져오기. 반복되는 요소는 elements로 구하기.

for index, row in enumerate(tableRow):
    songTitle = row.find_elements_by_tag_name('td')[5] # 인덱스 5에 있는 노래 제목과 가수명 
    print(songTitle.text)