from parsel import Selector
from trending.base import BaseRequest


class LangItem():
    def __init__(self, label='', key=''):
        self.label = label
        self.key = key


class LangSpider(BaseRequest):

    def get_url(self):
        return self.base

    def parse(self, text: str):
        sel = Selector(text=text)
        li = sel.css(
            '#languages-menuitems').css('[data-filter-list]')[0].css("a")
        items: list[LangItem] = []
        for a in li:
            key = a.css('::attr(href)').get().replace(
                "/trending", "").replace("/", "").split("?")[0]
            label = a.css("span::text").get().replace("\n", "").strip()
            items.append(LangItem(label=label, key=key))
        return items
