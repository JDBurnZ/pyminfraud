# coding: utf-8

try:
	from urllib2 import urlopen # Python 2
except ImportError as e:
	from urllib.request import urlopen # Python 3

try:
	from urllib import urlencode # Python 2
except ImportError as e:
	from urllib.parse import urlencode # Python 3

# Efficient Python 2/3-compatible dictionary iterations
def iterdict(dictionary):
	if hasattr(dictionary, 'iteritems'): # Python 2
		return dictionary.iteritems()
	else: # Python 3
		return dictionary.items()
