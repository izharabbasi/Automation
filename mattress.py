# coding: utf-8

from bs4 import BeautifulSoup
import csv, time, xlrd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wpBlogPost import WpHandler

class ScraperHandler():

    def __init__(self, site_url):
        self.site_url = site_url
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('chromedriver.exe')
        self.driver = webdriver.Chrome()

    def getAllMattress(self):
        try:
            with open('Suggestions.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    try:
                        keyword = (row[0]).strip()
                        search_keyword = keyword.replace(' ', '+')
                        site_url = self.site_url+str(search_keyword)
                        print(site_url)
                        pagecontent = self.getNewPageContent(site_url)

                        try:
                            mattress_url = pagecontent.findAll('div', attrs={'class':'related-question-pair'})
                        except:
                            mattress_url = pagecontent.findAll('div', attrs={'class':'related-question-pair'})
                        
                        doc_file = ''
                        count = 0
                        for mattress in mattress_url:
                            try:
                                link = mattress.find('a')['href']
                                print(link)
                                self.getPageContent(link)
                                match_keyword = keyword.split()
                                match_keyword = ["contains(text(), '"+str(item)+"')" for item in keyword.split()]
                                match_keyword = " or ".join(match_keyword)
                                mattress_data = self.driver.find_element_by_xpath("//p["+str(match_keyword)+"]").text
                                mattress_data = mattress_data
                                if len(str(mattress_data).strip()) > 25:
                                    count += 1
                                    synonyms_sheet = xlrd.open_workbook('Synonyms.xlsx')
                                    synonyms_sheet = synonyms_sheet.sheet_by_index(0)
                                    for word in range(synonyms_sheet.nrows):
                                        try:
                                            word_one = synonyms_sheet.cell_value(word, 0).strip()
                                            word_two = synonyms_sheet.cell_value(word, 1).strip()
                                            mattress_data = mattress_data.replace(word_one,word_two)
                                        except:
                                            pass
                                    if count <=4:
                                        doc_file+=str(keyword.title())+'\n'+str(mattress_data)+'\n'
                                    else:
                                        break
                            except:
                                pass
                        if count > 0:
                            objW = WpHandler()
                            objW.saveMattress(keyword.title(), doc_file)
                    except:
                        pass
            
        except:
            pass
        self.driver.quit()

    def getPageContent(self, link):
        try:
            self.driver.get(link)
            time.sleep(2)
            soup = BeautifulSoup(self.driver.page_source, u"html.parser")
        except:
            soup = None
        return soup

    def getNewPageContent(self, link):
        try:
            self.driver.get(link)
            time.sleep(2)
            try:
                self.driver.find_element_by_class_name('match-mod-horizontal-padding').click()
                time.sleep(5)
            except:
                pass
            try:
                self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/g-accordion-expander/div[1]/div').click()
                time.sleep(5)
            except:
                pass
            soup = BeautifulSoup(self.driver.page_source, u"html.parser")
        except:
            soup = None
        return soup

if __name__ == '__main__':
    site_url = 'https://www.google.com/search?q='
    objSH = ScraperHandler(site_url)
    objSH.getAllMattress()