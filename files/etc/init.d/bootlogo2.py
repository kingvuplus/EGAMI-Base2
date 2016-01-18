import pygeoip
import json
from urllib2 import urlopen
import os

os.system("rm /etc/egami/.egami")

def getBoxType():
	try:
		f = open("/proc/stb/info/vumodel","r")
		machine = f.read().strip()
		f.close()
		return machine
	except:
		return _("unknown")

try:      
	gi = pygeoip.GeoIP("/usr/lib/python2.7/pygeoip/GeoIP.dat")

	if getBoxType() in ("vusolo2", "vuduo2", "vusolose"):
		address_ip = json.load(urlopen('http://httpbin.org/ip'))['origin']
		country_code = gi.country_code_by_addr(address_ip)
		if country_code in ("PL"):
			os.system("touch /etc/egami/.egami")
	else:
		print "[EGAMI] Running on : ", getBoxType()
except:
	print "[EGAMI] Will not run correctly. CLONE DETECTED !!!"
