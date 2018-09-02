from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\sxsx1\Downloads\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://thevc.kr/')


driver.find_element_by_css_selector('body > header > div.header-left_side > div > input').send_keys('kakao')
driver.implicitly_wait(3)
driver.find_element_by_css_selector('body > header > div.header-left_side > div > div > div.r_container_company > ul > li:nth-child(1) > a > div').click()

invest = driver.find_element_by_css_selector('#content > div.content_body > div > div:nth-child(2) > div.graph_container.invest_info > div:nth-child(1) > div.num > p.sum_invest')
invest_data = invest.text
print("총 투자집행금:", invest_data)

dic = {}
li = []
for i in range(2,11):
    i = str(i)
    company = driver.find_element_by_css_selector('#similars_wrapper > table > tbody > tr:nth-child('+i+') > td:nth-child(2)')
    company_data = company.text.replace('\n','/')
    technology = driver.find_element_by_css_selector('#similars_wrapper > table > tbody > tr:nth-child('+i+') > td:nth-child(4)')
    technology_data = technology.text
    years = driver.find_element_by_css_selector('#similars_wrapper > table > tbody > tr:nth-child('+i+') > td:nth-child(5)')
    years_data = years.text
    sum_invest = driver.find_element_by_css_selector('#similars_wrapper > table > tbody > tr:nth-child('+i+') > td:nth-child(6)')
    sum_invest_data = sum_invest.text
    
    li = [technology_data, years_data, sum_invest_data]
    dic[company_data] = li

print(dic)
    

