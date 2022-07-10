# speed test using python
import math

import speedtest
def modifier(numbr):
    # rounding the number
    ten6 = math.pow(10, 6)
    mb =  numbr/ten6
    rnumb = round(mb)
    return rnumb

def return_on_failure(value):
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         return f(*args,**kwargs)
      except:
         print('some issue with internet')
         return value

def test():
    wifi = speedtest.Speedtest()
    down = modifier(wifi.download())
    up = modifier(wifi.upload())
    print("wifi down and up speed ", down, up)
    return down, up






