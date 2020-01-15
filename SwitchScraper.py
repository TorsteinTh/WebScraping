import requests
import sys as s
from bs4 import BeautifulSoup


def GetSwitchPrice():

    URLSwitch = 'https://www.netonnet.no/art/gaming/spillogkonsoll/nintendo/nintendo-konsoll/nintendo-switch-grey-2019/1009346.15692/'

    # Get Info
    page = requests.get(URLSwitch)

    # Pretty
    soup = BeautifulSoup(page.content, 'html.parser')

    # Print
    names = soup.find_all('div', class_='subTitle big')
    prices = soup.find_all('div', class_='price-big')
    print('Pris:')
    print('--------------------------------------')
    for price, name in zip(prices, names):
        print(name.text.strip() + '\t\t' + price.text.strip())
    print('--------------------------------------')


GetSwitchPrice()
