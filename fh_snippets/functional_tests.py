from selenium import webdriver
import unittest

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

if __name__ == '__main__':
    unittest.main()



