'Demonstrate screen scraping (HTML parsing) using regular expressions'

import urllib
import re
import smtplib
from email.mime.text import MIMEText

class Shopping:
    'Dictionary-style real-time price lookups'

    def __init__(self, root_url, pattern):
        self.root_url = root_url
        self.pattern = pattern
    
    def __getitem__(self, product):
        url = self.root_url + product
        u = urllib.urlopen(url)
        page = u.read()
        mo = re.search(self.pattern, page)
        return float(mo.group(1))


def notify_parties(price):
    # echo 'hi' | mail -s "your subject" avaneesh.kadam@gmail.com
    msg = MIMEText('Go get it')
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Hey, its cheap now.. %s' % price
    msg['From'] = 'avaneesh.kadam@gmail.com'
    msg['To'] = 'avaneesh.kadam@gmail.com'

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail('avaneesh.kadam@gmail.com', ['avaneesh.kadam@gmail.com'], msg.as_string())
    s.quit()

if __name__ == '__main__':

    nikon_lens_bh = '606792-USA'
    nikon_lens_fry = '6641324'

    looking_for = 180

    # B&H Photo Video
    bh = Shopping('http://www.bhphotovideo.com/c/product/', r'itemprop="price">\$([0-9\.]+)')
    valbh = bh[nikon_lens_bh]
    print valbh
    if valbh < looking_for:
        print 'cheap:', valbh
#notify_parties(r'$%d on B&H (Product code %s)' % (valbh, nikon_lens_bh))
        

    # Frys
    frys = Shopping('http://www.frys.com/product/', r'<label id="l_price1_value_\d+" class="">\$([0-9.]+)')
    valfry = frys[nikon_lens_fry]
    print valfry
    if valfry < looking_for:
        print 'cheap:', valfry
#        notify_parties(r'$%s on Frys (Product code %s)' % (valfry, nikon_lens_bh))


