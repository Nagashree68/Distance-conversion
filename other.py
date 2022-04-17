#test if the login is working fine

from selenium import webdriver
import unittest

class TestOrangeHRMHome(unittest.TestCase):
    def testcase1_checkTitle(self):
        browser = webdriver.Chrome(executable_path="I:/NAGASHREE/chromedriver")
        browser.get('https://opensource-demo.orangehrmlive.com/')
        print(browser.title)
        browser.quit()
    def testcase2_checklogin(self):
        browser = webdriver.Chrome(executable_path="I:/NAGASHREE/chromedriver")
        browser.get('https://opensource-demo.orangehrmlive.com/')
        browser.find_element_by_id('txtUsername').send_keys('Admin')
        browser.find_element_by_id('txtPassword').send_keys('admin123')
        browser.find_element_by_id('btnLogin').click()
        browser.quit()
    def testcase3_checkForgotPwdLink(self):
        webdriver.Chrome(executable_path="I:/NAGASHREE/chromedriver")
        browser.get('https://opensource-demo.orangehrmlive.com/')
        browser.find_element_by_partial_link_text('Forgot').click()
        print('url after clicking'+ browser.current_url)
        browser.quit()

if __name__=="__main()__":
    unittest.main()

