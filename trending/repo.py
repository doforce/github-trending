from parsel import Selector
from trending.base import BaseRequest
from utils import get_list_num


class BuildBy():
    def __init__(self, avatar='', by=''):
        self.avatar = avatar
        self.by = by


class RepoItem():
    def __init__(self, repo='', desc='', lang='', stars=0, forks=0, build_by: list[BuildBy] = [], change=0):
        self.repo = repo
        self.desc = desc
        self.lang = lang
        self.stars = stars
        self.forks = forks
        self.build_by = build_by
        self.change = change


class RepoSpider(BaseRequest):

    def __init__(self, since: str, lang: str):
        self.since = since
        self.lang = lang

    def get_url(self):
        return f"{self.base}/{self.lang}?since={self.since}"

    def parse(self, text: str):
        li = Selector(text=text).css('[data-hpc]')[0].css("article")
        items: list[RepoItem] = []
        for article in li:
            repo = article.css('h2')[0].css('::attr(href)').get()
            desc = article.css("p").css("::text").getall()
            footer = article.css("div")[2]
            stars = 0
            forks = 0
            for s_or_f in footer.css('div > a'):
                tmp_href = s_or_f.css('::attr(href)').get()
                if tmp_href.endswith("/forks"):
                    forks = get_list_num(
                        s_or_f.css("::text").getall())
                else:
                    stars = get_list_num(
                        s_or_f.css("::text").getall())
            item = RepoItem(repo=repo, desc="".join(desc).strip(
            ), stars=stars, forks=forks)

            lang_span = footer.css('div > span:has(span)')
            lang = lang_span[0].css('span')[2].css(
                "::text").get() if len(lang_span) > 0 else ""
            item.lang = lang

            build_span = footer.css('div > span:has(a)')
            bb_list = []
            if (len(build_span) > 0):
                build_links = build_span[0].css('a')
                for link in build_links:
                    avatar = link.css('img')[0].css('::attr(src)').get()
                    by = link.css('::attr(href)').get()
                    bb_list.append(BuildBy(avatar=avatar, by=by))
            item.build_by = bb_list

            change_span = footer.css('div > span:has(svg)')
            if len(change_span) > 0:
                item.change = get_list_num(
                    change_span[0].css("::text").getall())
            else:
                item.change = 0

            items.append(item)
        return items
