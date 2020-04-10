from datetime import datetime

import requests
from bs4 import BeautifulSoup
from webapp.db import db
from webapp.news.models import News

def get_html(url) -> 'html':
    try:
        result = requests.get(url) # 1
        result.raise_for_status() # 2
        return result.text # возвращает html страницы в тестовом виде
    except(requests.RequestException, ValueError): # RequestException если сетевая ошибка (1), ValueError если на стороне сервера возникла проблема (2)
        print('Сетевая ошибка')
        return False

def get_python_news() -> 'in_db':
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser') #преобразуем полученный html в дерево soup
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
    

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()