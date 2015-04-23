# coding: utf-8

import requests
from bs4 import BeautifulSoup


def build_url(megye, telepules, szavazokor):
    return 'http://valasztas.hu/dyn/pv14/szavossz/hu/M{:02d}/T{:03d}/szkjkv_{:03d}.html'.format(megye, telepules, szavazokor)

print build_url(1, 1, 1)


def format_nev(keresztnev, vezeteknev):
    return 'A keresztnevem {:s}, a vezetéknevem {:s}'.format(keresztnev, vezeteknev)

print format_nev('Rita', 'Zágoni')


def get_page(megye, telepules, szavazokor):
    url = build_url(megye, telepules, szavazokor)
    page = requests.get(url)
    #ha a lap nem létezik, hibát kapunk vissza
    if page.status_code == requests.codes.ok:
        return page.content


def get_all_szavazokor(megye, telepules):
    data = dict()
    szavazokor = 1
    while szavazokor <  4:
        document = get_page(megye, telepules, szavazokor)
        data[szavazokor] = document
        szavazokor += 1
    return data

print get_all_szavazokor(1, 1)

documents = get_all_szavazokor(1, 1)
print documents.keys()


for szavazokor, html_by_szavazokor in documents.items():
    print 'szavazokor: {:d}'.format(szavazokor)
    print 'html_by_szavazokor: {:.20s}'.format(html_by_szavazokor)

content = get_page(1, 1, 1)

soup = BeautifulSoup(content)

print soup.title.text
print soup.p
print soup.table

tables = soup.find_all('table')

print tables[0]

results = soup.find(text='Országos listás szavazás')
listas_table = results.find_next('table')
print listas_table
