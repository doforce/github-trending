from bs4 import BeautifulSoup
import re
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

GITHUB_URL = 'https://github.com'
REPOSITORY = GITHUB_URL + '/trending/'
DEVELOPER = REPOSITORY + 'developers/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 ' \
             'Safari/537.36 '
HEADER = {'User-Agent': USER_AGENT}
TIMEOUT = 15


async def get_trending(url, params):
    if url.startswith(DEVELOPER):
        return await get_developers(url, params)
    elif url.startswith(REPOSITORY):
        return await get_repository(url, params)


async def get_repository(url, params):
    conn_ok, soup = await get_soup(url, params)
    if conn_ok:
        is_not_blank, blank_result = no_trending(soup)
        if is_not_blank:
            repos = []
            repo_links = []
            for item in soup.find_all('div', attrs={'class': 'd-inline-block col-9 mb-1'}):
                item_temp = item.h3.a.attrs['href']
                repos.append(item_temp[1:])
                repo_links.append(GITHUB_URL + item_temp)

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
                    one.setdefault('lang', 'unknown')

                star = item.find('a', attrs={'href': re.compile(rep + "/" + "stargazers")})
                if star is not None:
                    one.setdefault("stars", star.get_text().strip())
                else:
                    one.setdefault('stars', '')

                fork = item.find('a', attrs={'href': re.compile(rep + "/" + "network")})
                if fork is not None:
                    one.setdefault('forks', fork.get_text().strip())
                else:
                    one.setdefault('forks', '')

                avatar = []
                for temp in item.find_all('a', attrs={'href': re.compile(rep + "/" + "graphs/contributors")}):
                    for con in temp.find_all('img'):
                        avatar.append(con.attrs['src'])
                one.setdefault('avatars', avatar)

                added = item.find('span', attrs={'class': 'd-inline-block float-sm-right'})
                if added is not None:
                    one.setdefault('added_stars', added.get_text().strip())
                else:
                    one.setdefault('added_stars', '')
                items.append(one)
            return {
                'count': len(items),
                'msg': 'suc',
                'items': items,
            }
    return {
        'count': 0,
        'msg': 'Unavialiable.',
        'items': [],
    }


async def get_developers(url, params):
    conn_ok, soup = await get_soup(url, params)
    if conn_ok:
        is_not_blank, blank_result = no_trending(soup)
        if is_not_blank:
            developer_avatars = []
            for item in soup.find_all('img', attrs={'class': 'rounded-1'}):
                developer_avatars.append(item.attrs['src'].strip())
            user = []
            user_link = []
            full_name = []
            for item in soup.find_all('h2', attrs={'class': 'f3 text-normal'}):
                temp = item.a.attrs['href'].strip()
                user.append(temp[1:])
                user_link.append(GITHUB_URL + temp)
                full_n = item.a.span
                if full_n is not None:
                    full_name.append(full_n.get_text().strip())
                else:
                    full_name.append('')

            items = []
            for u, ul, fn, da in zip(user, user_link, full_name, developer_avatars):
                one = {}
                one.setdefault('user', u)
                one.setdefault('user_link', ul)
                one.setdefault('full_name', fn)
                one.setdefault("developer_avatar", da)
                items.append(one)
            return {
                'count': len(items),
                'msg': 'suc',
                'items': items,
            }
    return {
        'count': 0,
        'msg': 'Unavialiable.',
        'items': [],
    }


def no_trending(soup):
    is_nothing = soup.find('div', attrs={'class', 'blankslate'})
    if is_nothing is None:
        return True, "ok"
    else:
        return False, is_nothing.h3.get_text().strip()


async def get_soup(url, params):
    try:
        if params is not None:
            url = "{0}?since={1}".format(url, params.get('since'))
        req = HTTPRequest(url, headers=HEADER, request_timeout=TIMEOUT)
        response = await AsyncHTTPClient().fetch(req)
    except Exception as e:
        return False, e
    else:
        return True, BeautifulSoup(response.body)


async def get_all_language():
    ok, result = await get_soup(url=REPOSITORY, params=None)
    lang = []
    for res in result.find_all('span',
                               attrs={'class': 'select-menu-item-text js-select-button-text js-navigation-open'}):
        if res is not None:
            lang.append(res.get_text().strip().replace(' ', '-', 3))
    return lang
