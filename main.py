from fastapi import FastAPI
from trending.repo import RepoSpider
from trending.lang import LangSpider
from trending.user import UserSpider

app = FastAPI(title="GitHub Trending APIs", version="2.0.2", contact={
    "name": "Edgar",
    "url": "https://github.com/doforce/github-trending",
})


@app.get("/")
def root():
    return {"message": "Hello GitHub trending"}


@app.get('/lang')
def lang():
    spider = LangSpider()
    return spider.get_items()


@app.get('/repo')
def repo(lang: str = "", since: str = "daily"):
    spider = RepoSpider(since, lang)
    return spider.get_items()


@app.get('/user')
def repo(lang: str = "", since: str = "daily", sponsorable=""):
    spider = UserSpider(since, lang, sponsorable)
    return spider.get_items()
