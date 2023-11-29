import requests
from fake_useragent import UserAgent

ua = UserAgent()


class BaseRequest:
    base = "https://github.com/trending"

    def get_url(self) -> str:
        pass

    def parse(self, text: str):
        pass

    def begin_parse(self):
        r = requests.get(self.get_url(), headers={"user-agent": ua.random})
        if r.status_code >= 300:
            return None
        return r.text

    def get_items(self):
        text = self.begin_parse()
        if text is None:
            return []
        return self.parse(text)
