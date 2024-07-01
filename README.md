### Github trending

This repository is a GitHub trending API power by [FastAPI](https://fastapi.tiangolo.com) and [Scrapy parsel](https://github.com/scrapy/parsel).</br>
It was deployed to [Vercel](https://vercel.com).

---

#### Run & Deploy

##### Run in development

```bash
python -m venv .venv
.venv/Scripts/Activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Run in Docker

```bash
docker build -t trending . && docker run --rm -p 8000:80 trending
```

#### Deploy to Vercel

Just fork this repository, and import it in your Vercel dashboard.

#### All the requests main adrress is this:https://trend.doforce.us.kg

[Swagger Docs](https://trend.doforce.us.kg/docs)

#### Get the trending repositories from `/repo`

##### Parameters

| Name  | Type   | Description                                                  |
| ----- | ------ | ------------------------------------------------------------ |
| lang  | string | optional, default is "", the language of trending repository |
| since | string | optional，default is "daily", daily/weekly/monthly           |

For example request this address:
https://trend.doforce.us.kg/repo?lang=java&since=weekly

```json
//status code: 200
// up to 25 items
[
    {
        "repo": "/StarRocks/starrocks",
        "desc": "StarRocks, a Linux Foundation project, is a next-generation sub-second MPP OLAP database for full analytics scenarios, including multi-dimensional analytics, real-time analytics, and ad-hoc queries. InfoWorld’s 2023 BOSSIE Award for best open source software.",
        "lang": "Java",
        "stars": 6338,
        "forks": 1437,
        "build_by": [
            {
                "avatar": "https://avatars.githubusercontent.com/u/57167462?s=40&v=4",
                "by": "/amber-create"
            },
            {
                "avatar": "https://avatars.githubusercontent.com/u/98087056?s=40&v=4",
                "by": "/evelynzhaojie"
            },
            {
                "avatar": "https://avatars.githubusercontent.com/u/4351040?s=40&v=4",
                "by": "/sduzh"
            },
            {
                "avatar": "https://avatars.githubusercontent.com/u/104624482?s=40&v=4",
                "by": "/EsoragotoSpirit"
            },
            {
                "avatar": "https://avatars.githubusercontent.com/u/34912776?s=40&v=4",
                "by": "/stdpain"
            }
        ],
        // How many stars did it gain this week/day/month
        "change": 619
    }
]
```

#### Get the trending developers from `/user`

##### Parameters

| Name        | Type   | Description                                                                                |
| ----------- | ------ | ------------------------------------------------------------------------------------------ |
| lang        | string | optional, default is "", the language of trending repository                               |
| since       | string | optional，default is "daily", daily/weekly/monthly                                         |
| sponsorable | string | optional，default is "", Whether the developer was sponsored, "1" is true, others is false |

For example request this address:
https://trend.doforce.us.kg/user?lang=java&since=weekly

```json
//status code: 200
// up to 25 items
[
    {
        // developer's GitHub avatar
        "avatar": "https://avatars.githubusercontent.com/u/322311?s=96&v=4",
        // developer's nickname
        "name": "Ben McCann",
        // developer's GitHub name
        "github_name": "/benmccann",
        "popular": {
            // developer's popular repository
            "repo": "/benmccann/NameMatching",
            // developer's popular repository description
            "desc": "My entry (Yet Another Team Challenge) to MITRE's name matching competition"
        }
    }
]
```

### Get all the avialiable trending languages in GitHub from `/lang`

For example,request this address:
https://trend.doforce.us.kg/lang

```json
//status code: 200
// about 700 items
[
    {
        // The display language name
        "label": "Unknown languages",
        // the language name which is used to search repositories and developers
        "key": "unknown"
    },
    {
        "label": "Python",
        "key": "python"
    },
    {
        "label": "C#",
        "key": "c%23"
    }
]
```

#### Exception

If the server does not get the resources, or the query parameters you input don't match anything, the response will be like:

```
//status code: 200
[]
```

#### Maintenance

If some of the api can not be used, please contact me with email:`doforce@pm.me`,I will modify the problem as soon as possible,thank you!
