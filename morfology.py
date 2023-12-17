import requests
from bs4 import BeautifulSoup


def analysis(word):
    page = requests.get(f"https://ru.wiktionary.org/wiki/{word.lower()}").text
    soup = BeautifulSoup(page, "html.parser")

    data = soup.find(class_="mw-content-ltr mw-parser-output").text.split('\n')
    res = [x for x in data if 'корень' in x.lower()][0]
    res = res.replace('; ', '\n')

    if '[' in res:
        i = res.find('[')
        res = res[:i]
    
    return res[0].lower() + res[1:]



