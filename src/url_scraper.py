from seleniumbase import sb_cdp
from bs4 import BeautifulSoup

sb = sb_cdp.Chrome()
sb.open('https://bikroy.com/en/ads/rajshahi/laptops?sort=date&order=desc&buy_now=0&urgent=0&page=1')
sb.solve_captcha()

def go_next():
    next_button = sb.find_element('.gtm-next-page')
    next_button.click()

def grab_urls():
    sb.assert_element('.gtm-normal-ad')
    normal_cards = sb.find_elements('.gtm-normal-ad', timeout = 30)
    try:
        sponsored_cards = sb.find_elements('.gtm-top-ad', timeout = 1)
        cards = normal_cards + sponsored_cards
    except:
        cards = normal_cards
    links = []
    for card in normal_cards:
#       global g
#      g = (card)
        link = BeautifulSoup(str(card),'html.parser').find('a').get('href')
        links.append(link)
    return links


#print(grab_urls())
#print('next')
#go_next()
links = []
for i in range(5):
    links = links + grab_urls()
    go_next()

import json
with open('outputs/output.json','w') as f:
    json.dump(links, f)
