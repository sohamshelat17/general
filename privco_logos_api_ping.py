#RiteKit Procedure

import urllib.request as req
import requests
#import urllib2


imgurl = ['https://api.ritekit.com/v1/images/logo?domain=diversifiedrestaurantholdings.com&client_id=73ee63c0a381cd1fa879a5aa7bff70a21ffd1d09129a'
]

for i in imgurl:
    try:
        req.urlretrieve(i, "{0}.jpg".format(i[46:]))
    except:
        pass
