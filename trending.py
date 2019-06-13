from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from lxml import etree

GITHUB_URL = 'https://github.com/'
REPOSITORY = GITHUB_URL + 'trending/'
DEVELOPER = REPOSITORY + 'developers/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 ' \
             'Safari/537.36 '
HEADER = {'User-Agent': USER_AGENT}
TIMEOUT = 15
NO_RESULT = {
    'count': 0,
    'msg': 'Unavailable',
    'items': [],
}


async def get_trending(url: str, params: dict = None) -> dict:
    html = await get_html(url, params)
    if html:
        is_blank = await has_trending(html)
        if not is_blank:
            if url.endswith(DEVELOPER):
                return await parse_developer(html)
            else:
                return await parse_repo(html)
        else:
            return NO_RESULT
    else:
        return NO_RESULT


async def parse_repo(html) -> dict:
    items = []
    articles = html.xpath('//article')
    for article in articles:
        item = {'repo': article.xpath('./h1/a/@href')[0][1:]}
        item['repo_link'] = GITHUB_URL + item['repo']
        tmp = article.xpath('./p/text()')
        item['desc'] = tmp[0].replace('\n', '').strip() if len(tmp) > 0 else ''
        tmp = article.xpath('./div[last()]/span[1]/span[2]/text()')
        item['lang'] = tmp[0].replace('\n', '').strip() if len(tmp) > 0 else ''
        tmp = article.xpath('./div[last()]/a[1]/text()')
        item['stars'] = "".join(tmp).replace(' ', '').replace('\n', '')
        tmp = article.xpath('./div[last()]/a[2]/text()')
        item['forks'] = "".join(tmp).replace(' ', '').replace('\n', '')
        tmp = article.xpath('./div[last()]/span[3]/text()')
        item['added_stars'] = "".join(tmp).replace('\n', '').strip()
        item['avatars'] = article.xpath('./div[last()]/span[2]/a/img/@src')
        items.append(item)
    return {
        'count': len(items),
        'msg': 'suc',
        'items': items
    }


async def parse_developer(html) -> dict:
    items = []
    articles = html.xpath('//article')
    for article in articles:
        item = {'user': article.xpath('./div[2]/div[1]/h1/a/@href')[0][1:]}
        item['user_link'] = GITHUB_URL + item['user']
        item['full_name'] = article.xpath('./div[2]/div[1]/h1/a/text()')[0][1:]
        item['developer_avatar'] = article.xpath('./div[1]/a/img/@src')[0]
        items.append(item)
    return {
        'count': len(items),
        'msg': 'suc',
        'items': items
    }


async def has_trending(html):
    blank = html.xpath('//div[contains(@class,"blankslate")]')
    if blank or len(blank) > 0:
        return html.xpath('string(//div[contains(@class,"blankslate")]/h3)') \
            .replace('\n', '').strip()
    else:
        return None


async def get_html(url: str, params: dict = None):
    try:
        if params is not None:
            url = "{0}?since={1}".format(url, params.get('since'))
        req = HTTPRequest(url, headers=HEADER, request_timeout=TIMEOUT)
        response = await AsyncHTTPClient().fetch(req)
    except Exception:
        return None
    else:
        return etree.HTML(response.body)


async def get_all_language():
    html = await get_html(url=REPOSITORY)
    return html.xpath('//div[@class="select-menu-list"]/div/a/span/text()')
