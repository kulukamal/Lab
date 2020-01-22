import ntplib
from time import ctime

client = ntplib.NTPClient()
try:
	res = client.request('ntp-b.nist.gov')
	print(ctime(res.tx_time))
except Exception as e:
	print(e)


