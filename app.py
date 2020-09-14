from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


def write_to_csv(data):
    headers = ['serial', 'rule', 'Identify_the_time', 'Identify_the_results','Temperature', 'If_fever','Whether_wear']
    with open('data.csv','w',encoding='utf-8') as f:
        writer= csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)

def get(element_list):
    try:
        return element_list.pop(0)
    except:
        return ''


driver = webdriver.Chrome()
url = 'http://touchlessguardian.ddns.net:8088/'

driver.get(url)

driver.find_element_by_xpath('//*[@id="login_language"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="lan2"]').click()
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('12345')
driver.find_element_by_xpath('//*[@id="login_ok"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//li[@id="FaceMenu"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="facerecordDiv"]').click()
driver.implicitly_wait(5)


extracted_records = []
iframe = driver.find_element_by_xpath("//iframe")
driver.switch_to.frame(iframe)
records = driver.find_elements_by_xpath("//table[@class='l-grid-body-table']/tbody/tr")

for record in records:
    r = {
        'serial': get(record.find_elements_by_xpath(".//td[1]/div[@class='l-grid-row-cell-inner']")).text,
        'rule': get(record.find_elements_by_xpath(".//td[2]/div[@class='l-grid-row-cell-inner']")).text,
        'Identify_the_time': get(record.find_elements_by_xpath(".//td[5]/div[@class='l-grid-row-cell-inner']")).text,
        'Identify_the_results': get(record.find_elements_by_xpath(".//td[6]/div[@class='l-grid-row-cell-inner']")).text,
        'Temperature': get(record.find_elements_by_xpath(".//td[7]/div[@class='l-grid-row-cell-inner']")).text,
        'If_fever': get(record.find_elements_by_xpath(".//td[9]/div[@class='l-grid-row-cell-inner']")).text,
        'Whether_wear': get(record.find_elements_by_xpath(".//td[10]/div[@class='l-grid-row-cell-inner']")).text
    }
    extracted_records.append(r)

print(extracted_records)
write_to_csv(extracted_records)
driver.quit()
