from requests.auth import HTTPBasicAuth
from lxml import etree
import requests
import schedule
import time
from mailer import Mailer
import datetime

def job():
    ns = {'kos': 'http://kosapi.feld.cvut.cz/schema/3',
          'atom': 'http://www.w3.org/2005/Atom'}
    response = requests.get('https://kosapi.fit.cvut.cz/api/3/exams/627548816405', auth=HTTPBasicAuth('kroupvla', 'pass'))
    root = etree.fromstring(response.content)

    capacity = root.xpath('/atom:entry/atom:content/kos:capacity/text()', namespaces=ns)[0]
    occupied = root.xpath('/atom:entry/atom:content/kos:occupied/text()', namespaces=ns)[0]

    free = int(capacity) - int(occupied)
    time = datetime.datetime.now().time()
    print(time, ': ', occupied, '/', capacity, sep='')	

    if (free > 0):
        mailer = Mailer()
        mailer.email('uvolnilo se misto na zkousce', 'volno: '+ str(free))


if __name__ == '__main__':
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
