from parsel import Selector
from trending.base import BaseRequest
from utils import get_list_num


class PopItem():
    def __init__(self, repo='', desc=""):
        self.repo = repo
        self.desc = desc


class UserItem():
    def __init__(self, avatar='', name="", github_name='', popular: PopItem = None):
        self.avatar = avatar
        self.name = name
        self.github_name = github_name
        self.popular = popular


class UserSpider(BaseRequest):

    def __init__(self, since: str, lang: str, sponsorable: str):
        self.since = since
        self.lang = lang
        self.sponsorable = sponsorable

    def get_url(self):
        return f"{self.base}/developers/{self.lang}?since={self.since}&sponsorable={self.sponsorable}"

    def parse(self, text: str):
        li = Selector(text=text).css('article[id^=pa-]')
        if len(li) == 0:
            return []
        items: list[UserItem] = []
        for article in li:
            avatar = article.css('div > a:has(img)').css('img')[
                0].css('::attr(src)').get()
            name = article.css('div > h1:has(a)')
            if len(name) > 0:
                name = name.css('a::text')[0].get()
            else:
                name = None
            github_name = article.css('div > p:has(a)')
            if len(github_name) > 0:
                github_name = github_name.css("a::attr(href)")[0].get()
            else:
                github_name = ""
            repo = article.css('article article').css(
                'h1 a::attr(href)').get()
            desc = article.css(
                'article article > h1 + div').css("::text").get()
            pop = PopItem(repo=repo if repo is not None else "",
                          desc=desc.strip() if desc is not None else "")
            items.append(UserItem(avatar=avatar, name=name.strip(
            ) if name is not None else "", github_name=github_name, popular=pop))
        return items
