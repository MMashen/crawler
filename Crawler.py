import urllib.request as req
import bs4


def get_data(url):
    request = req.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    return data


def parse_data(data):
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    title_text = []
    for title in titles:
        if title.a is not None:
            title_text.append(title.a.string)
            print(title.a.string)

    next_link = root.find("a", string="‹ 上頁")
    if next_link:
        return title_text, next_link["href"]
    else:
        return title_text, None


url = "https://www.ptt.cc/bbs/Stock/index.html"

page = 7301
page_zero = 7299

if __name__=="__main__":
    with open("data.txt", "w", encoding="utf-8") as file:
        while url and page_zero <= page:
            data = get_data(url)
            titles, next_url = parse_data(data)

            for title in titles:
                file.write(title + "\n")

            print(page)

            if next_url:
                url = "https://www.ptt.cc" + next_url
                page -= 1
            else:
                break
