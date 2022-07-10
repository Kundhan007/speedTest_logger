# speed test using python
import math

import speedtest
import subprocess

def modifier(numbr):
    # rounding the number
    ten6 = math.pow(10, 6)
    mb = numbr / ten6
    rnumb = round(mb)
    return rnumb


def test():
    try:
        return testWrapper()
    except:
        print('some internet issue')
        return 0,0, 'not connected'

def testWrapper():
    wifi = speedtest.Speedtest()
    down = modifier(wifi.download())
    up = modifier(wifi.upload())
    print("wifi down and up speed ", down, up)
    return down, up

