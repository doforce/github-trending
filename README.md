# Github trending

![github.png](http://upload-images.jianshu.io/upload_images/2040047-113772827550d86c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

This project is a GitHub trending API power by Python.
It was deployed on Vercel.

---

### All the requests main adrress is this:https://trend.catchmeup.top

### Get the trending repository

request address like this:

> /repo

-   If the language contains '#',you must use '-shuo' to replace it.

#### Parameters

| Name  | Type   | Description                                                               |
| ----- | ------ | ------------------------------------------------------------------------- |
| lang  | string | optional, get method parameter, the language of trending repository       |
| since | string | optional，get method parameter，default is daily,others is weekly,monthly |

For example request this address:
https://trend.catchmeup.top/repo?lang=java&since=weekly

return:

```
//status code: 201
{
  "count": 25,
  "msg": "suc",
  //trending repositories
  "items": [
    {
      //the avatar link of contributors
      "avatars": [
        "https://avatars0.githubusercontent.com/u/16903644?v=3&s=40",
        "https://avatars2.githubusercontent.com/u/8622362?v=3&s=40",
        "https://avatars0.githubusercontent.com/u/10773353?v=3&s=40",
        "https://avatars3.githubusercontent.com/u/6392550?v=3&s=40",
        "https://avatars1.githubusercontent.com/u/3837836?v=3&s=40"
      ],
      //repository link
      "repo_link": "https://github.com/kdn251/interviews",
      //repository desctiption
      "desc": "Everything you need to know to get the job.",
      //repository name
      "repo": "kdn251/interviews",
      //the repository stars count
      "stars": "5,772",
       //the repository forks count
      "forks": "539",
      //the language of repository
      "lang": "Java",
      //the repository stars count for tody or this week or this month
      "added_stars": "4,591 stars this week"
    },
    .
    .
    .
  ]
}
```

### Get all the all the avialiable trending languages in GitHub.

For example,request this address:
https://trend.catchmeup.top/lang

return:

```
//status code: 201
{
    "count": 464,
    "items": [
        "1C-Enterprise",
        "ABAP",
        "ABNF",
        "ActionScript",
        "Ada",
        .
        .
        .
        "YANG",
        "Zephir",
        "Zimpl"
    ],
    "msg": "suc"
}
```

### Exception

If the server does not get the resources,the response will be that:

```
//status code: 404
{
  "msg": "Unavailable.",
  "count":0,
  "items": []
}
```

#### Maintenance

If some of the interface can not be used,please contact me with email:`doforce@pm.me`,I will modify the problem as soon as possible,thank you!
