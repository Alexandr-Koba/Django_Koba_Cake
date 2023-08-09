from django.urls import resolve
from django.test import TestCase
from blog.views import home_page, article_page
from blog.models import  Article
from django.http import HttpRequest
from datetime import datetime




class HomePageTest(TestCase):
    # Проверяет главную страницу
    def test_home_page_displays_articles(self): 
        # Создает статью 1
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            pubdate=datetime.now()
        )
        # Создает статью 2
        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            pubdate=datetime.now() # Время сейчас
        )
        # Открывает главную страницу
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        # проверить содержимое ответа:
        self.assertIn('title 1', html)
        self.assertIn('/blog/title-1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)
        
        self.assertIn('title 2', html)
        self.assertIn('/blog/title-2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('full_text 2', html)


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Koba Cake</title>', html)
        self.assertIn('<h1>Koba Cake</h1>', html)
        self.assertTrue(html.endswith('</http>'))

class ArticleModelTest(TestCase):
    # Проверяет статьи
    def test_article_model_seve_and_retrive(self):
        # создай статью 1
        # сохрани статью 1
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='symmary 1',
            category='category 1',
            pubdate=datetime.now(),
        )
        article1.save()

        # создай статью 2
        # сохрани статью 2
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='symmary 2',
            category='category 2',
            pubdate=datetime.now(),
        )
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)

        # проверь: первая загруженная статья должна быть == 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # проверь: вторая загруженная статья должна быть == 2
        self.assertEqual(
        all_articles[1].title,
        article2.title
        )

        # Некоторые статьи есть в админке но они не опубликованы

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1 + 1, 3)
