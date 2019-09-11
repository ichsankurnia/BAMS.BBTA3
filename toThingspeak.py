import time
import os
import sys
import urllib            # URL functions
import urllib2           # URL functions

import random

################# Default Constants #################
# These can be changed if required

THINGSPEAKKEY = 'HCRR3NJG1RWYZ6CY'
THINGSPEAKURL = 'https://api.thingspeak.com/update'

def sendData(url,key,field1,field2,temp,pres):
  """
  Send event to internet site
  """

  values = {'api_key' : key,'field1' : temp,'field2' : pres}

  postdata = urllib.urlencode(values)
  req = urllib2.Request(url, postdata)
  response = urllib2.urlopen(req, None, 5)
	html_string = response.read()
	response.close()

  try:
    # Send data to Thingspeak
	response = urllib2.urlopen(req, None, 5)
	html_string = response.read()
	response.close()
	log = log + 'Update ' + html_string

  except urllib2.HTTPError, e:
    log = log + 'Server could not fulfill the request. Error code: ' + e.code
  except urllib2.URLError, e:
    log = log + 'Failed to reach server. Reason: ' + e.reason
  except:
    log = log + 'Unknown error'

  print log

def main():
    while True:
      temperature = random.randint(0,100)
      pressure = random.randint(0,1000)
      sendData(THINGSPEAKURL,THINGSPEAKKEY,'field1','field2',temperature,pressure)
      sys.stdout.flush()

if __name__=="__main__":
   main()