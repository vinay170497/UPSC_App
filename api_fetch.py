import requests

def fetch_current_affairs():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=YOUR_NEWSAPI_KEY"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    return [{"title": article["title"], "url": article["url"]} for article in articles]
