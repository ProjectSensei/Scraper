import requests
from bs4 import BeautifulSoup
import json
import link_converter
import time
from urllib.parse import unquote
directlinks = []
brokenlinks = []
animes = {}
proxies = {}
if input('[?] Do you want to use a proxy? (Y/N): ').upper() == 'Y':
    print('[i] Use a socks4 proxy')
    a = input('[?] Enter ip:port: ')
    proxies['https'] = 'socks4://'+a
    proxies['http'] = 'socks4://'+a
titlecheck = ''
def createkey(key, value):
    animes[key] = value
def StringFinalizer(animelink): 
        str1 = " "
        return (str1.join(animelink))
try:
    with open('links.json', 'r') as f:
        file = f.read()
        jsonfile = json.loads(file)
        animes = jsonfile
except KeyError:
    pass
with open('page.txt', 'r') as f:
    page_num = int(f.read())
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
while page_num < 55:
    page_num = page_num + 1
    if proxies == {}:
        print('[i] Sending request to https://kissanime.rest/all_anime/?page={}&alphabet=all'.format(str(page_num)))
        page = requests.get('https://kissanime.rest/all_anime/?page={}&alphabet=all'.format(str(page_num)), headers=headers)
    else:
        print('[i] Sending request to https://kissanime.rest/all_anime/?page={}&alphabet=all using proxy {}'.format(str(page_num),proxies['https']))
        page = requests.get('https://kissanime.rest/all_anime/?page={}&alphabet=all'.format(str(page_num)), headers=headers, proxies=proxies)
    soup = BeautifulSoup(page.content, 'html.parser')
    listingresults = soup.find('ul', class_='listing')
    results = listingresults.findChildren('a', href=True)
    links = []
    links2 = []
    eplinks = []
    for result in results:
        if result['href'].startswith('/anime/'):
            links.append('https://kissanime.rest'+result['href'])
    for link in links:
        if proxies == {}:
            print('[i] Sending request to {}'.format(link))
            page = requests.get(link, headers=headers)
        else:
            print('[i] Sending request to {} using proxy {}'.format(link, proxies['https']))
            page = requests.get(link, headers=headers, proxies=proxies)
        soup = BeautifulSoup(page.content, 'html.parser')
        eplinksli = soup.find('ul', id='episode_related')
        eplinks = eplinksli.findChildren('a', href=True,class_='')
        name = str(soup.find('div',class_='anime_info_body_bg').findChild('h1').text)
        for eplink in eplinks:
            if eplink['href'].startswith('/ep/'):
                print('[i] Appending https://kissanime.rest' + eplink['href'].format(str(page_num)))
                links2.append('https://kissanime.rest' + eplink['href'])
            elif eplink['href'].startswith(' /ep/'):
                try:
                    print('[i] Appending https://kissanime.rest' + eplink['href'].replace(' ',''))
                    links2.append('https://kissanime.rest' + eplink['href'].replace(' ',''))
                except:
                    print('[!] Cannot remove space from ' + eplink['href'])
            else:
                print(eplink['href'] + ' is not a URL starting with /ep/')
    links2 = list(dict.fromkeys(links2))
    for link in links2:
        emptylistcheck = True
        if proxies == {}:
            print('[i] Sending request to {}'.format(link))
            page = requests.get(link, headers=headers)
        else:
            print('[i] Sending request to {} using proxy {}'.format(link,proxies['https']))
            page = requests.get(link, headers=headers, proxies=proxies)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('a', {'class':'active'})
        try:
            anime_title_from_link = str(link_converter.convert(results[0]['data-video'])[0])
        except IndexError:
            print('[!] Results is an empty list, skipping')
            emptylistcheck = False
        if emptylistcheck:
            anime_title_from_link = str(unquote(anime_title_from_link))
            if titlecheck == anime_title_from_link:
                pass
            elif titlecheck != anime_title_from_link:
                directlinks = []
                titlecheck = anime_title_from_link
            elif titlecheck == '':
                titlecheck = anime_title_from_link
            try:
                if results[0]['data-video'].startswith('https://'):
                    print('[i] Appending video link - ' + results[0]['data-video'])
                    directlinks.append(results[0]['data-video'])
                    animes[anime_title_from_link] = directlinks
                elif results[0]['data-video'].startswith('//'):
                    print('[i] Appending video link - ' + 'https:' + results[0]['data-video'])
                    directlinks.append('https:' + results[0]['data-video'])
                    animes[anime_title_from_link] = directlinks
                else:
                    print('[i] Appending video link - ' + 'httpsdude://' + results[0]['data-video'])
                    directlinks.append('https://' + results[0]['data-video'])
                    animes[anime_title_from_link] = directlinks
            except IndexError:
                print('[!] Website returned a broken link, skipping')
    directlinks = list(dict.fromkeys(directlinks))
    directlinks = []
    for key in animes:
        if animes[key] == []:
            brokenlinks.append(key)
    for key in brokenlinks:
        animes.pop(key)
    with open('links.json', 'w') as f:
        json.dump(animes, f, indent=4)
    with open('page.txt', 'w') as f:
        f.write(str(page_num))
    directlinks = []
with open('links.json', 'w') as f:
    json.dump(animes, f, indent=4) 
print('[✓] Script finished scraping links!')
