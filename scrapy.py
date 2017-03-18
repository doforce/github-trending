from bs4 import BeautifulSoup
import requests
from requests import exceptions

GITHUB_URL = 'https://github.com'
TRENDING = GITHUB_URL + '/trending/'
DEVELOPERS = GITHUB_URL + '/trending' + '/developers/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 ' \
             'Safari/537.36 '
HEADER = {'User-Agent': USER_AGENT}
TIMEOUT = 20


def get_developers(url=DEVELOPERS, params=None):
    is_not_timeout, soup = get_soup(url, params)
    if is_not_timeout:
        is_not_blank, blank_result = no_trending(soup)
        if is_not_blank:
            leader_avatars = []
            for item in soup.find_all('img', attrs={'class': 'leaderboard-gravatar'}):
                leader_avatars.append(item.attrs['src'].strip())
            user = []
            user_link = []
            full_name = []
            for item in soup.find_all('h2', attrs={'class': 'user-leaderboard-list-name'}):
                temp = item.a.attrs['href'].strip()
                user.append(temp[1:])
                user_link.append(GITHUB_URL + temp)
                full_n = item.a.span
                if full_n is not None:
                    full_name.append(full_n.get_text().strip())
                else:
                    full_name.append('')
            descriptions = []
            for item in soup.find_all('span', attrs={'class', 'repo-snipit-description css-truncate-target'}):
                descriptions.append(item.get_text().strip())

            items = []
            for u, ul, fn, d in zip(user, user_link, full_name, descriptions):
                one = {}
                one.setdefault('user', u)
                one.setdefault('user_link', ul)
                one.setdefault('full_name', fn)
                one.setdefault('description', d)
                items.append(one)

            return {
                'items': items,
            }
        else:
            return {
                'error': blank_result,
            }
    else:
        return {
            'error': soup,
        }


def get_trending(url=TRENDING, params=None):
    is_not_timeout, soup = get_soup(url, params)
    if is_not_timeout:
        is_not_blank, blank_result = no_trending(soup)
        if is_not_blank:
            # Repositories
            repos = []
            # Repository links
            repo_links = []
            for item in soup.find_all('div', attrs={'class': 'd-inline-block col-9 mb-1'}):
                item_temp = item.h3.a.attrs['href']
                repos.append(item_temp)
                repo_links.append(GITHUB_URL + item_temp)

            # Repository descriptions
            desc = []
            for de in soup.find_all('div', attrs={'class': 'py-1'}):
                desc.append(de.get_text().strip())

            items = []
            for item, rep, rep_l, des in zip(soup.find_all('div', attrs={'class': 'f6 text-gray mt-2'})
                    , repos, repo_links, desc):
                one = {}
                one.setdefault('repo', rep)
                one.setdefault('repo_link', rep_l)
                one.setdefault('desc', des)

                lan = item.find('span', attrs={'itemprop': 'programmingLanguage'})
                if lan is not None:
                    one.setdefault('lang', lan.get_text().strip())
                else:
                    one.setdefault('lang', '')

                one.setdefault('starts', item.find('a', attrs={'class': 'muted-link tooltipped tooltipped-s mr-3'})
                               .get_text().strip())

                one.setdefault('forks', item.find('a', attrs={'aria-label': 'Forks'}).get_text().strip())

                avatar = []
                for temp in item.find_all('a', attrs={'class': 'no-underline'}):
                    for con in temp.find_all('img'):
                        avatar.append(con.attrs['src'])
                one.setdefault('avatars', avatar)

                one.setdefault('added_starts', item.find('span', attrs={'class': 'float-right'}).get_text().strip())
                items.append(one)

            return {
                'items': items,
            }
        else:
            return {
                'error': blank_result,
            }
    else:
        return {
            'error': soup,
        }


def no_trending(soup):
    is_nothing = soup.find('div', attrs={'class', 'blankslate'})
    if is_nothing is None:
        return True, "ok"
    else:
        return False, is_nothing.h3.get_text().strip()


def get_soup(url, params=None):
    try:
        r = requests.get(url, params=params, headers=HEADER, timeout=TIMEOUT)
    except exceptions.Timeout as e:
        return False, 'request timeout'
    except exceptions as e:
        return False, e
    else:
        return True, BeautifulSoup(r.text)


def get_all_language():
    ok, result = get_soup(url=TRENDING)
    lang = []
    for res in result.find_all('span',
                               attrs={'class': 'select-menu-item-text js-select-button-text js-navigation-open'}):
        lan = res.get_text().strip().replace(' ', '-', 3)
        lang.append(lan)
    print(len(lang))
    with open('all_language.txt', 'wt') as f:
        for l in lang:
            f.write(l)
            f.write(',')

# get_all_language()
# result=get_trending(url=TRENDING)
# print(result)
