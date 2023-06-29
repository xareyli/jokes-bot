import requests
from bs4 import BeautifulSoup
import random


def get_random_joke() -> str:
    random_page = random.randint(1, 600)

    if random_page == 1:
        page_uri = "/"
    else:
        page_uri = "/page/{}/index.htm".format(random_page)

    try:
        response = requests.get("https://anekdotus.com" + page_uri)
        response.encoding = response.apparent_encoding

        if not str(response.status_code).startswith("2"):
            return "False"

        bs4 = BeautifulSoup(response.text, "html.parser")

        dle_content = bs4.find("div", {"id": "dle-content"})

        jokes = dle_content.find_all("div", {"class": "tecst"})

        random_joke = random.choice(jokes)

        random_joke.find("div", {"class": "wrrating"}).extract()

        return random_joke.get_text()
    except:
        return False
