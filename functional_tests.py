from selenium import webdriver
import unittest

class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_install(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Congratulations!', self.browser.title)
        #self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main()

# tests Django page open
#browser = webdriver.Chrome()
#browser.get('http://127.0.0.1:8000')
#assert 'install' in browser.title