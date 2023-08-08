from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):
    
    # Гоша набрал в поисковике десерты пангана, кликнул по одной из ссылок.
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере Гоши открылся сайт (по адрессу ...)
        # В заголовке сайта Гоша прочитал "Koba Cake"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Koba Cake', self.browser.title)
        #self.fail('Finish the test!')

    def test_home_page_header(self):
        # В шапке сайта написанно "Koba Cake"
        self.browser.get('http://127.0.0.1:8000')
        # Выбираем первый элемент
        header = self.browser.find_elements(By.TAG_NAME, 'h1')[0]
        # Получаем текст из первого элемента с тегом h1
        self.assertIn('Koba Cake - Закажи десерт', header.text)

    def test_home_page_blog(self):
        # Под шапкой расположен блог со статьями о десертах
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element_by_class_name('article_title')
        article_summary = self.browser.find_element_by_class_name('article_summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

        # Статьи открываются с красивым коротким адресом
        
if __name__ == '__main__':
    unittest.main()

# tests Django page open
#browser = webdriver.Chrome()
#browser.get('http://127.0.0.1:8000')
#assert 'install' in browser.title




