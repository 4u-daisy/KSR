from bs4 import BeautifulSoup
import requests
import re

url = 'https://xn--b1aew.xn--p1ai/wanted'


def parsing(_url: str) -> list:
    r = requests.get(_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all('img')


def write_file(persons: list, path: str) -> None:
    f = open(path, 'w', encoding='UTF-8')
    for i in range(len(persons)):
        f.write(str(persons[i]))


def read_file(path: str) -> list:
    result = []
    template = r'//static.mvd.ru/upload/'
    f = open(path, 'r', encoding='UTF-8')

    for line in f:
        tmp = line.split('"')
        for _str in tmp:
            if re.match(template, _str) and (_str not in result):
                result.append(_str)

    return result


def get_url_photo(persons: list) -> None:
    for i in range(len(persons)):
        p = requests.get('https:' + str(persons[i]))
        path = 'photo/' + str(i) + '.jpg'
        out = open(path, "wb")
        out.write(p.content)
        out.close()


imgs = parsing(url)
write_file(imgs, 'text.txt')
res = read_file('text.txt')
get_url_photo(res)
