import requests
import sys as s
from bs4 import BeautifulSoup


def GetTheWeather():
    if len(s.argv) == 2:
        by = s.argv[1] 
    else:
        by = 'ams'

    URL = ''
    if(by == 'ams' or by == 'amsterdam'):
        URL = 'https://www.yr.no/sted/Nederland/Nord-Holland/Amsterdam/time_for_time.html'
        by = 'AMSTERDAM'
    elif(by == 'be' or by == 'bergen'):
        URL = 'https://www.yr.no/sted/Norge/Vestland/Bergen/Bergen/time_for_time.html'
        by = 'BERGEN'
    elif(br == 'os' or by == 'oslo'):
        URL = 'https://www.yr.no/place/Norway/Oslo/Oslo/Oslo/hour_by_hour.html'
        by = 'OSLO'
    else:
        assert('No city was selected')


    #Get Info 
    page = requests.get(URL)

    # Pretty
    soup = BeautifulSoup(page.content, 'html.parser')
    

    # Print
    cels = soup.find_all('td',class_="temperature plus")    
    kls = soup.find_all('td', scope="row")
    mms = soup.find_all('td', class_='precipitation')
    print('This is the weather for the next days:')
    print('--------------------------------------')
    print(by)
    print('--------------------------------------')
    for cel, kl, mm  in zip(cels, kls, mms):
        print(kl.text + "\t \t" + cel.text + "\t" + mm.text)
    
   

GetTheWeather()
