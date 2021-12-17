# Github Trending Repos API

> This is a fork of [xxdongs/github-trending](https://github.com/xxdongs/github-trending) with CORS enabled

Requests can be made to: [`https://gh-trending-repos.herokuapp.com/repo`](https://gh-trending-repos.herokuapp.com/repo). No auth is required.

#### Parameters
| Name  | Type  | Description |
| ------| ------ | ------ |
| **`lang`** | `string` | _Optional_ - The language of trending repository. Do not include `#` characters |
| **`since`** | `string` | _Optional_ - The timeframe, can be either `daily`, `weekly` or `monthly`. Defaults to `daily` |

For example request this address:
https://gh-trending-repos.herokuapp.com/repo?lang=java&since=weekly


<details>
 <summary><b>Example Response</b></summary>
	<p>
 
  ```json
  {
  "count": 25,
  "msg": "suc",
  "items": [
    {
      "repo": "TencentARC/GFPGAN",
      "repo_link": "https://github.com/TencentARC/GFPGAN",
      "desc": "GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration.",
      "lang": "Python",
      "stars": "10,767",
      "forks": "1,635",
      "added_stars": "5,356 stars this week",
      "avatars": [
        "https://avatars.githubusercontent.com/u/17445847?s=40&v=4",
        "https://avatars.githubusercontent.com/u/81195143?s=40&v=4",
        "https://avatars.githubusercontent.com/u/18028233?s=40&v=4",
        "https://avatars.githubusercontent.com/u/36897236?s=40&v=4",
        "https://avatars.githubusercontent.com/u/17243165?s=40&v=4"
      ]
    },
    {
      "repo": "dendibakh/perf-book",
      "repo_link": "https://github.com/dendibakh/perf-book",
      "desc": "The book \"Performance Analysis and Tuning on Modern CPU\"",
      "lang": "TeX",
      "stars": "759",
      "forks": "47",
      "added_stars": "445 stars this week",
      "avatars": [
        "https://avatars.githubusercontent.com/u/4634056?s=40&v=4"
      ]
    }
    ...
  ]
}
  ```
 
 </p>
</details>

---

## Deployment

Deploy to Heroku:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/lissy93/gh-trending-no-cors/tree/master)

Or, Run locally:
- Get the code: `git clone https://github.com/Lissy93/gh-trending-no-cors.git`
- Navigate into directory: `cd gh-trending-no-cors`
- Install dependencies: `pip install -r requirements.txt`
- Start the web server: `python manage.py --port=8080`
- Then open your Postman or your browser, and visit `http://localhost:8080/repo`

---

## Info

### Contributing

Pull requests are welcome :)

### Dependencies

- [`lxml`](https://github.com/lxml/lxml) - Python XML toolkit
- [`tornado`](https://github.com/tornadoweb/tornado) - Web framework, developed by FriendFeed
- [`ustudio-tornado-cors`](https://github.com/ustudio/tornado-cors) - Adds CORS support to Tornado, by @ustudio

### Credits

Full credit to the author of the original repo, [@Edgar](https://github.com/xxdongs)

### Privacy

See the [Heroku/ Salesforce Privacy Policy](https://www.salesforce.com/company/privacy/) for the hosted instance, and the [GitHub Privacy Statement](https://docs.github.com/en/github/site-policy/github-privacy-statement) for the data fetched from the GH API.

### License

This fork is licensed under [MIT](https://mit-license.org/) - © [Alicia Sykes](https://aliciasykes.com) 2021

