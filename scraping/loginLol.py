from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver') # 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver.get('https://kr.leagueoflegends.com/ko-kr/') # 롤 페이지 열기

loginBtn = driver.find_element_by_xpath(
    '//*[@id="riotbar-right-content"]/div[3]/div[1]'
) # 롤페이지 로그인 버튼

loginBtn.click() # 클릭