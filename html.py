import re, datetime, random

from detectmobilebrowser import *

HOST = 'wordpicker'

TITLE    = 'Word Picker'
SUBTITLE = 'Word Finder for Popular Word Games and Crosswords'
YEAR     = datetime.date.today().year

PROMO    = 'Word Finder for Popular Word Games and Crosswords'

#PUBLISHERS = ['bannerplay','amazon-us-1','amazon-us-2','amazon-us-3','revenuehits']
PUBLISHERS = ['google']

def html_defaults(host,user_agent=None):
  DOMAIN   = re.search('%s.*'%HOST,host, re.IGNORECASE).group()
  URL      = 'www.' + DOMAIN.lower()
  WWW      = 'http://' + URL

  return {
    'domain':     DOMAIN,
    'www':        WWW,
    'title':      TITLE,
    'subtitle':   SUBTITLE,
    'year':       YEAR,
    'promo':      PROMO,
    'publisher1': PUBLISHERS[random.randint(0,len(PUBLISHERS)-1)],
    'publisher2': PUBLISHERS[random.randint(0,len(PUBLISHERS)-1)],
    'is_mobile':  is_mobile_browser(user_agent)
  }
