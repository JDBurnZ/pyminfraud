# coding: utf-8

documentation_not_found = 'No documentation found for "{field_name}"'
invalid_country_value = 'Expected 2-character, 3-character or numeric ISO 3166-compliant country code for "{field_name}", encountered "{field_value}"'
invalid_field_name = 'Unexpected/unrecognized field name "{field_name}"'
invalid_field_value = 'Expected "{datatype}" datatype for field "{field_name}", encountered "{field_value}" instead'
missing_required_field = 'Missing required fields: {field_names}'
response_unknown_error = 'Encountered unknown type of error in MinFraud Response: "{error}"'

response_errors = {
	'COUNTRY_REQUIRED': 'Country Required',
	'INVALID_LICENSE_KEY': 'The license key passed is invalid',
	'IP_NOT_FOUND': 'IP address is not valid, is not public, or is not in the MaxMind GeoIP database',
	'IP_REQUIRED': 'IP Address Required',
	'LICENSE_REQUIRED': 'License Required',
	'MAX_REQUESTS_REACHED': 'Trial account is out of free queries. Now may be a great time to move onto a paid service.',
}

response_warnings = {
	'CITY_NOT_FOUND': 'City Not Found',
	'CITY_REQUIRED': 'City Required',
	'COUNTRY_NOT_FOUND': 'Country Not Found',
	'POSTAL_CODE_NOT_FOUND': 'Zip Not Found',
	'POSTAL_CODE_REQUIRED': 'Zip Required',
}
