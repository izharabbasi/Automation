from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_path = which("chromedriver.exe")
chrome_option = Options()
chrome_option.add_argument('--headless')

url = 'https://www.google.com'
driver = webdriver.Chrome(executable_path=chrome_path ,options=chrome_option)
driver.get(url)

search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("My user agent")
btn = driver.find_element_by_xpath("(//input[@name='btnK'])[2]").click()
driver.implicitly_wait(5)

print(driver.page_source)
driver.quit()