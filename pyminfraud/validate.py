# coding: utf-8

from . import compatibility

# Supress pycountry logging warnings:
import logging
logging.getLogger('pycountry.db').addHandler(logging.NullHandler())

def avs(field_rules, field_value):
	# http://en.wikipedia.org/wiki/Address_Verification_System#Address_Verification_Service_.28AVS.29_codes
	avs_codes = {
		'A': 'Street address matches, but 5-digit and 9-digit postal code do not match. Standard domestic network.',
		'B': 'Street address matches, but postal code not verified. Standard international network.',
		'C': 'Street address and postal code do not match. Standard international network.',
		'D': 'Street address and postal code match. Code "M" is equivalent. Standard international network.',
		'E': 'AVS data is invalid or AVS is not allowed for this card type. Standard domestic network.',
		'F': 'Card member\'s name does not match, but billing postal code matches. American Express only network.',
		'G': 'Non-U.S. issuing bank does not support AVS. Standard international network.',
		'H': 'Card member\'s name does not match. Street address and postal code match. American Express only network.',
		'I': 'Address not verified. Standard international network.',
		'J': 'Card member\'s name, billing address, and postal code match. American Express only network.',
		'K': 'Card member\'s name matches but billing address and billing postal code do not match. American Express only network.',
		'L': 'Card member\'s name and billing postal code match, but billing address does not match. American Express only network.',
		'M': 'Street address and postal code match. Code "D" is equivalent. Standard international network.',
		'N': 'Street address and postal code do not match. Standard domestic network.',
		'O': 'Card member\'s name and billing address match, but billing postal code does not match. American Express only network.',
		'P': 'Postal code matches, but street address not verified. Standard international network.',
		'Q': 'Card member\'s name, billing address, and postal code match. American Express only network.',
		'R': 'System unavailable. Standard domestic network.',
		'S': 'Bank does not support AVS. Standard domestic network.',
		'T': 'Card member\'s name does not match, but street address matches. American Express only network.',
		'U': 'Address information unavailable. Returned if the U.S. bank does not support non-U.S. AVS or if the AVS in a U.S. bank is not functioning properly. Standard domestic network.',
		'V': 'Card member\'s name, billing address, and billing postal code match. American Express only network.',
		'W': 'Street address does not match, but 9-digit postal code matches. Standard domestic network.',
		'X': 'Street address and 9-digit postal code match. Standard domestic network.',
		'Y': 'Street address and 5-digit postal code match. Standard domestic network.',
		'Z': 'Street address does not match, but 5-digit postal code matches. Standard domestic network.',
	}

	if field_value.upper() in avs_codes:
		return True

def enum(field_rules, field_value):
	if field_value in field_rules['values']:
		return True

def ip(field_rules, field_value):
	ip_libraries = {
		# Set the key to the name of the module to import.
		# The value will be a dictionary with three keys:
		#
		#   - function: The object or function to call, passing the IP
		#     address as the first argument.
		#
		#   - event: If the library in question throws an exception when
		#     passed an invalid IP address, set to "exception". If the
		#     library returns a specific value when passed an invalid IP,
		#     set to "value".
		#
		#   - action: If "event" is set to "exception", specify the
		#     exception class here, NOT as a string. If "event" is set to
		#     "value", specify the value to look for/compare against.
		#
		# If the value specified is encountered or if the exception
		# specified is thrown, validation fails. Otherwise, validation
		# succeeds.

		'ipaddress': {
			'function': 'ip_address',
			'event': 'exception',
			'action': ValueError,
		},
		'ipaddr': {
			'function': 'IPAddress',
			'event': 'exception',
			'action': ValueError,
		},
		'IPy': {
			'function': 'IP',
			'event': 'exception',
			'action': ValueError,
		},
	}

	for ip_library, ip_config in compatibility.iterdict(ip_libraries):
		try:
			ip_handler = __import__(ip_library)

			try:
				# Grab the function we're going to call.
				ip_function = getattr(ip_handler, '{function}'.format(function=ip_config['function']))

				# Call the function passing the IP as an argument.
				ip_result = ip_function(field_value)

				if ip_config['event'] == 'exception' or (ip_config['event'] == 'compare' and ip_result == ip_config['action']):
					return True
			except ip_config['action'] as e:
				# IP module exists, but the IP address isn't valid.
				# Break the iteration, and return None.
				return None
		except ImportError as e:
			# Error importing module try another one (if there is one)
			continue
	return True

def iso3166(field_rules, field_value):
	# http://en.wikipedia.org/wiki/ISO_3166
	try:
		import pycountry
	except ImportError as e:
		return True

	try:
		if len(field_value) == 2:
			pycountry.countries.get(alpha2=field_value.upper()) # alpha-2
		elif len(field_value) == 3:
			try:
				pycountry.countries.get(alpha3=field_value.upper()) # alpha-3
			except KeyError as e:
				pycountry.countries.get(numeric=field_value.upper()) # numeric
		else:
			pycountry.countries.get(name=field_value) # short name
		return True
	except KeyError as e:
		pass

def iso4217(field_rules, field_value):
	# http://en.wikipedia.org/wiki/ISO_4217
	try:
		import pycountry
	except ImportError as e:
		return True

	try:
		pycountry.currencies.get(letter=field_value.upper())
		return True
	except KeyError as e:
		pass
