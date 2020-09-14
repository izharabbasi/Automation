# coding: utf-8
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class WpHandler():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def saveMattress(self, keyword, data):
        try:
            self.loginWp()
            self.saveBlog(keyword, data)
        except:
            pass
        self.driver.quit()

    def saveBlog(self, keyword, data):
        try:
            self.driver.get('http://wordpress.mg-mg.xyz/wp/wp-admin/post-new.php?post_type=page')
            time.sleep(1)
            self.driver.find_element_by_id('post-title-0').send_keys(keyword)
            time.sleep(2)
            self.driver.find_element_by_class_name('block-editor-inserter__toggle').click()
            time.sleep(2)
            self.driver.find_element_by_class_name('editor-block-list-item-paragraph').click()
            time.sleep(2)
            self.driver.find_element_by_class_name('block-editor-rich-text__editable')
            ActionChains(self.driver).send_keys(data).perform() 
            time.sleep(2)            
            self.driver.find_element_by_class_name('editor-post-save-draft').click()
            time.sleep(1)
        except:
            import sys
            print(sys.exc_info())
            pass

    def loginWp(self):
        try:
            self.driver.get('http://wordpress.mg-mg.xyz/wp/wp-admin/')
            time.sleep(1)

            # Please Write userName here in send_keys('')

            self.driver.find_element_by_id('user_login').send_keys('admin')
            time.sleep(1)

            # Please Write PASSWORD here in send_keys('')

            self.driver.find_element_by_id('user_pass').send_keys('wsNZvC)AxHzr2m&@cakRdU6S')
            time.sleep(1)
            self.driver.find_element_by_id('wp-submit').click()
            time.sleep(1)
        except:
            pass