from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import requests

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # givess FF response time
    def tearDown(self):
        self.browser.quit()

    def test_dashboard_in_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Dashboard', self.browser.title)
        # self.fail('Finished') # in to make sure test fails til you finished it.

    def test_dashboard_links(self):
        self.browser.get('http://localhost:8000')
        links = self.browser.find_elements_by_tag_name('a')
        self.assertTrue(len(links)==3)
        for link in links:     
            status = request.get(link.get_attribute('href'))
            self.assertTrue(status == 200)
if __name__ == '__main__':
    unittest.main()



