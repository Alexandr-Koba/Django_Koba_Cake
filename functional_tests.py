from selenium import webdriver
import unittest

class BasicInstallTest(unittest.TestCase):
    
    # Гоша набрал в поисковике десерты пангана, кликнул по одной из ссылок.
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере Гоши открылся сайт (по адрессу ...)
        # В заголовке сайта Гоша прочитал "Вкустно жить не запретишь Koba Cake"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Koba Cake', self.browser.title)
        #self.fail('Finish the test!')

    def test_home_page_header(self):
        # В шапке сайта написанно "Koba Cake"
        self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('Koba Cake', header)
        
if __name__ == '__main__':
    unittest.main()

# tests Django page open
#browser = webdriver.Chrome()
#browser.get('http://127.0.0.1:8000')
#assert 'install' in browser.title




