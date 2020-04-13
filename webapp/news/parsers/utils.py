import requests

from webapp.news.models import News
from webapp.db import db


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    try:
        result = requests.get(url, headers=headers)  # 1
        result.raise_for_status()  # 2
        return result.text  # возвращает html страницы в тестовом виде
    except (requests.RequestException, ValueError):
        # RequestException если сетевая ошибка (1), ValueError если на стороне сервера возникла проблема (2)
        print('Сетевая ошибка')
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()