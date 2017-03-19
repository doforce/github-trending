from bs4 import BeautifulSoup
import requests
from requests import exceptions

GITHUB_URL = 'https://github.com'
REPOSITORY = GITHUB_URL + '/trending/'
DEVELOPER = REPOSITORY + 'developers/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 ' \
             'Safari/537.36 '
HEADER = {'User-Agent': USER_AGENT}
TIMEOUT = 20


# to be continued
class Trending:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.result = {}
        self.one = {}
        self.items = []
        try:
            r = requests.get(self.url, params=self.params, headers=HEADER, timeout=TIMEOUT)
        except exceptions as e:
            self.soup = None
        else:
            self.soup = BeautifulSoup(r.text)

    def __del__(self):
        self.url = None
        self.params = None
        self.result = {}
        self.one = {}
        self.items = []

    def get_repos(self):
        if self.soup is not None:
            if self.no_trending() is None:
                repos, repo_links, desc = self.get_repo_desc()
                for item, rep, rep_l, des in zip(self.soup.find_all('div', attrs={'class': 'f6 text-gray mt-2'})
                        , repos, repo_links, desc):
                    self.one = {}
                    self.one.setdefault('repo', rep)
                    self.one.setdefault('repo_link', rep_l)
                    self.one.setdefault('desc', des)
                    self.set_label_text(item, 'span', {'itemprop': 'programmingLanguage'}, 'lang')
                    self.set_label_text(item, 'a', {'class': 'muted-link tooltipped tooltipped-s mr-3'}, 'starts')
                    self.set_label_text(item, 'a', {'aria-label': 'Forks'}, 'forks')
                    self.set_label_text(item, 'span', {'class': 'float-right'}, 'added_starts')
                    avatar = []
                    for temp in item.find_all('a', attrs={'class': 'no-underline'}):
                        for con in temp.find_all('img'):
                            avatar.append(con.attrs['src'])
                    self.one.setdefault('avatars', avatar)
                    self.items.append(self.one)
                self.result = {
                    'items': self.items,
                }
                self.items = []
                return self.result

            else:
                self.result = {
                    'error': self.no_trending()
                }
        else:
            self.result = {
                'error', 'requests exceptions exist'
            }
            return self.result

    def get_repo_desc(self):
        repos = []
        repo_links = []
        for item in self.soup.find_all('div', attrs={'class': 'd-inline-block col-9 mb-1'}):
            item_temp = item.h3.a.attrs['href']
            repos.append(item_temp)
            repo_links.append(GITHUB_URL + item_temp)

        desc = []
        for de in self.soup.find_all('div', attrs={'class': 'py-1'}):
            desc.append(de.get_text().strip())
        return repos, repo_links, desc

    def find_label(self, label, attrs):
        return self.soup.find_all(label, attrs=attrs)

    def set_label_text(self, soup, label, attrs, key):
        temp = soup.find(label, attrs=attrs)
        if temp is not None:
            self.one.setdefault(key, temp.get_text().strip())
        else:
            self.one.setdefault(key, '')

    def no_trending(self):
        is_nothing = self.find('div', attrs={'class', 'blankslate'})
        if is_nothing is None:
            return None
        else:
            return is_nothing.h3.get_text().strip()


