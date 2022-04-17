from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearchEngineTest(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path='I:/NAGASHREE/chromedriver')

    def setUp(self):
        self.browser.get('https://www.google.com/')
        self.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def testcase1_searchPuneetRajkumar(self):
        self.browser.find_element_by_name('q').send_keys('Puneeth Rajkumar')
        self.browser.find_element_by_name('btnK').click()

    def testcase2_searchMicroDegreeKannada(self):
        self.browser.find_element_by_name('q').send_keys('MicroDegree Kannada')
        self.browser.find_element_by_name('btnK').click()

    def testcase3_searchdarabendre(self):
        self.browser.find_element_by_name('q').send_keys('da ra bendre')
        self.browser.find_element_by_name('btnK').click()

    def testcase4_searchTumkur(self):
        self.browser.find_element_by_name('q').send_keys('Tumkur')
        self.browser.find_element_by_name('btnK').click()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\html_reports"))



