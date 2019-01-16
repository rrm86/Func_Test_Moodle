
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='geo/geckodriver')

    def tearDown(self):
        pass
        #self.browser.quit()

    def test_can_login(self):
        # Go to the page
        self.browser.get('https://ead.puc-rio.br/login/')

        # Check header mention
        self.assertIn('Ambiente', self.browser.title)
        
        #Login as student
        self.browser.find_element_by_id('alunobotao').click()
        ##Fill username field
        inputbox = self.browser.find_element_by_id('maluno')
        inputbox.send_keys('user')
        ##Fill the password fil
        passbox = self.browser.find_element_by_id('pass')
        passbox.send_keys('pass')
        ##Login
        self.browser.find_element_by_id('btnloginaluno').click()
        self.assertIn('https://ead.puc-rio.br/my/', self.browser.current_url)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

