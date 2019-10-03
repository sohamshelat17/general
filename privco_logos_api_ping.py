#RiteKit Procedure

import urllib.request as req
import requests
#import urllib2


imgurl = ['https://logo.clearbit.com/bizongo.in']

for i in imgurl:
    try:
        req.urlretrieve(i, "{0}.jpg".format(i[46:]))
    except:
        pass
