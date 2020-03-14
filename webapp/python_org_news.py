import requests
from bs4 import BeautifulSoup

def get_html(url) -> 'html':
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news() -> 'list_dict':
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser') #преобразуем полученный html в дерево soup
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                'published': published
            })
        return result_news
    return False