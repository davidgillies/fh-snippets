from django.test import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import requests
import time

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # givess FF response time

    def tearDown(self):
        self.browser.quit()

    def test_dashboard_in_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Dashboard', self.browser.title)
        # self.fail('Finished') # in to make sure test fails til you finished it.

    def test_dashboard_links(self):
        self.browser.get(self.live_server_url)
        links = self.browser.find_elements_by_tag_name('a')
        self.assertTrue(len(links)==3)
        for link in links:     
            status = requests.get(link.get_attribute('href')).status_code
            self.assertTrue(status == 200, msg="%s, %s"%(link.text, status))

    
    def test_can_start_a_biog_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url+'/biogs/')
        first_name_inputbox = self.browser.find_element_by_id('new_biog_first_name')
        self.assertEqual(
            first_name_inputbox.get_attribute('placeholder'),
            'Enter a First Name'
        )
        surname_inputbox = self.browser.find_element_by_id('new_biog_surname')
        self.assertEqual(
            surname_inputbox.get_attribute('placeholder'),
            'Enter a Surname'
        )
        birth_year_inputbox = self.browser.find_element_by_id('new_biog_birth_year')
        self.assertEqual(
            birth_year_inputbox.get_attribute('placeholder'),
            'Enter Birth Year'
        )
        first_name_inputbox.send_keys('Bert')
        surname_inputbox.send_keys('Konterman')
        birth_year_inputbox.send_keys('1976')
        birth_year_inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('biog_list')
        time.sleep(0)
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Konterman, Bert, 1976' for row in rows)
        )

        self.browser.get(self.live_server_url+'/biogs/') 
        links = self.browser.find_elements_by_tag_name('a')
        for link in links:
            page = requests.get(link.get_attribute('href'))
            status = page.status_code
            self.assertTrue(status == 200, msg="%s, %s"%(link.text, status))       


if __name__ == '__main__':
    unittest.main()



