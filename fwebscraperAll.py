import requests
import sys as s
import re
from bs4 import BeautifulSoup


class Weather:
    def __init__(self):
        self.citys = ['OSLO', 'BERGEN', 'AMSTERDAM']
        self.URL = ['https://www.yr.no/sted/Norge/Oslo/Oslo/Oslo/time_for_time.html',
                    'https://www.yr.no/sted/Norge/Vestland/Bergen/Bergen/time_for_time.html',
                    'https://www.yr.no/sted/Nederland/Nord-Holland/Amsterdam/time_for_time.html'
                    ]
        self.pages = []
        self.soups = []
        self.results = []
        self.kls = []
        self.printkl = bcolors.UNDERLINE
        self.printmm = bcolors.OKGREEN
        self.printcel = bcolors.UNDERLINE

    def getPages(self):
        for url in self.URL:
            self.pages.append(requests.get(url))

    def getSoup(self):
        for page in self.pages:
            self.soups.append(BeautifulSoup(page.content, 'html.parser'))

    def getDetails(self):
        for soup in self.soups:
            kls = soup.find_all('td', scope="row")
            mms = soup.find_all('td', class_='precipitation')
            cels = soup.find_all('td', class_="temperature")
            self.results.append(City(kls, mms, cels))
            self.kls.append(kls)

    def printResults(self):
        print('----------------------------------------------------------------------------------------')
        print '\t\t\t',
        for city in self.citys:
            print city + '\t\t\t',
        print ' '
        print('----------------------------------------------------------------------------------------')

        # For a new day
        first = None

        # Print everything
        for kl in self.kls[0]:
            if (kl.text[0] != first):
                print '--- new day ---'
            first = kl.text[0]
            if (re.search(r'[a-z]* [0-7]\b', kl.text) is not None):
                self.printkl = bcolors.WARNING

            print self.printkl + kl.text + "\t\t" + bcolors.ENDC,
            self.printkl = bcolors.UNDERLINE

            for city in self.results:
                if len(city.cels) == 0:
                    print 'NaN'
                    print 'Data might not be fully correct!'
                    continue
                cel = city.cels.pop(0)
                mm = city.mms.pop(0)
                if('0 mm' != mm.text):
                    self.printmm = bcolors.OKLIGHTBLUE
                if (re.search(r'[-][0-9]', cel.text) is not None):
                    self.printcel = bcolors.OKBLUE

                print self.printcel + cel.text + bcolors.ENDC + '\t' + self.printmm + mm.text + "\t\t" + bcolors.ENDC,
                self.printmm = bcolors.OKGREEN
                self.printcel = bcolors.UNDERLINE
            print ' '

    def GetTheWeather(self):
        # Get Info
        self.getPages()
        self.getSoup()
        self.getDetails()
        self.printResults()


class City:
    def __init__(self, kls=[], mms=[], cels=[]):
        self.kls = kls
        self.mms = mms
        self.cels = cels


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKLIGHTBLUE = '\033[34m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    weather = Weather()
    weather.GetTheWeather()
