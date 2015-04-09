#coding: utf-8

import requests
from bs4  import BeautifulSoup


def build_url(megye, telepules, szavazokor):
    return 'http://www.valasztas.hu/dyn/pv14/szavossz/hu/M{:02d}/T{:03d}/szkjkv_{:03d}.html'.format(megye, telepules, szavazokor)
 
 
def get_page(megye, telepules, szavazokor):
    url = build_url(megye, telepules, szavazokor)
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        return page.content
 
 
def get_all_szavazokor(megye, telepules):
    '''
   Returns a dictionary of pages.
   key = szavazokor
   value = text of html
   '''
    data = {}
    szavazokor = 1
    while szavazokor < 4:
        document = get_page(megye, telepules, szavazokor)
        data[szavazokor] = document
        szavazokor += 1
    return data


def get_all_telepules(megye):
    data = {}
    telepules = 1
    while telepules < 4:
        document = get_all_szavazokor(megye, telepules)
        data[telepules] = document
        telepules += 1
    return data
 

def get_all_megye():
    data = {}
    megye = 1
    while megye < 4:
        data[megye] = get_all_telepules(megye)
        megye += 1
    return data

all_data = get_all_megye()


for megye, adat in all_data.items():
    for telepules, telepules_adat in adat.items():
        for szavazokor, html in telepules_adat.items():
            print 'megye: ', megye
            print 'telepules: ', telepules
            print 'szavazokor: {:d}'.format(szavazokor)
            print 'html: {:.20s}'.format(html)

"""
adatszerkezet:
{megye: {telepules: {szavazokor:html}, telepules: {szavazokor:html},..}, telepules: {}, megye:{}}

"""


def jegyzekben_megjelent(content):
    result = {}
    soup = BeautifulSoup(content)
    jegyzokonyv = soup.find(text='Jegyzőkönyv')
    voter_table = jegyzokonyv.find_next('table')

    voter_data = voter_table.find_all('td')
    osszes = voter_data[0].text
    megjelentek = list(voter_data[1])

    """
    a következő változott, órán így nézett ki:
    return megjelentek[0], megjelentek[1].text
    nem tudom, mi működött máshogy akkor ott, de valószínűbb, hogy ez fog helyes eredményt adni nálatok is:
    a teljesség kedvéért még beleteszem egy dictionarybe az eredményeket
    """

    result['osszes'] = osszes
    result['megjelenetek_szama'] = megjelentek[0]
    result['megjelentek_aranya'] = megjelentek[2]
    return result


content = get_page(1, 1, 1)
print jegyzekben_megjelent(content)


def get_parteredmenyek(content):
    results = list()
    soup = BeautifulSoup(content)

    jelolt_table = soup.find('p', text='A szavazatok száma jelöltenként').find_next('table')

    rows = jelolt_table.find_all('tr')
    for row in rows[1:]:
        result = {}
        cells = row.find_all('td')
        result['part'] = cells[2].text
        result['szavazat'] = cells[3].text
        results.append(result)

    return results

print get_parteredmenyek(content)
