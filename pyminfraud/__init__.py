# coding: utf-8

__project__ = 'pyminfraud'
__author__ = 'Joshua D. Burns'
__email__ = 'joshuadburns@hotmail.com'
__license__ = '''pyminfraud by Joshua D. Burns is licensed under the Creative Commons Attribution
3.0 Unported License. To view a copy of this license, please visit:
http://creativecommons.org/licenses/by/3.0/'''
__version__ = '1.0.3'
__created__ = '2013-10-01'
__status__ = 'Production'
__description__ = 'Python library for interfacing with MaxMind\'s minFraud Web Service API.',
__url__ = 'https://www.github.com/JDBurnZ/pyminfraud'
__packages__ = ['pyminfraud']
__keywords__ = 'python maxmind minfraud pyminfraud'

# Import standard modules
import hashlib
import sys

# Import pyminfraud-Specific modules
from . import exceptions
from . import errors
from . import validate
from . import transform
from . import compatibility
from .documentation import documentation
from .fields import rules, required, lookup

request_hosts = [
	'minfraud.maxmind.com',
	'minfraud-us-east.maxmind.com',
	'minfraud-us-west.maxmind.com',
]

request_protocol = 'https'
request_uri = '/app/ccv2r'

class Client:
	def __init__(self, license_key, validate=True, transform=True, debug=False, **add_fields):
		self.validate = validate
		self.transform = transform
		self.debug = debug
		self.fields = {}
		self.response = None
		self.result = None

		# Add "license-key" to field names/values.
		self.add_field('license_key', license_key)

		# Add additional keyword arguments as field names/values.
		self.add_fields(add_fields)

	def add_field(self, field_name, field_value):
		# Validate the field's name
		if field_name not in fields.rules:
			# Field name doesn't exist, check if minFraud-named field was
			# passed and resolve it to a pyminfraud compatible field name.
			lookup_field_name = self._lookup(field_name)
			if lookup_field_name:
				field_name = lookup_field_name
			else:
				raise exceptions.InvalidFieldName(errors.invalid_field_name.format(field_name = field_name))

		# Grab rules associated with the field name passed.
		field_rules = fields.rules[field_name]

		# Validate the field value's data-type (if applicable)
		if self.validate and 'datatype' in field_rules:
			if not self._validate(field_rules, field_value):
				raise exceptions.InvalidFieldValue(errors.invalid_field_value.format(datatype=field_rules['datatype'], field_name=field_name, field_value=field_value))

		# Perform field transformation (if applicable)
		if self.transform and 'transform' in field_rules:
			field_value = self._transform(field_rules['transform'], field_value)

		self.fields[field_name] = field_value

		return field_value

	def add_fields(self, fields):
		for field_name, field_value in compatibility.iterdict(fields):
			self.add_field(field_name, field_value)

	def remove_field(self, field_name):
		if field_name in self.fields:
			del self.fields[field_name]
			return True

	def get_field(self, field_name):
		if field_name in self.fields:
			return self.fields[field_name]

	def get_fields(self):
		return self.fields

	def execute(self, timeout=30, protocol=request_protocol, host=request_hosts[0], uri=request_uri):
		# Ensure all required fields have been defined.
		missing = self._missing()
		if missing:
			raise exceptions.MissingRequiredFields(errors.missing_required_field.format(field_names=', '.join(missing)))

		self.response = compatibility.urlopen(self._request_url(protocol, host, uri), self._request_arguments(), timeout)

		# Parse the response into a usable dictionary.
		self.result = self._response_parse(self.response.read())

		# Check if resulting response contains errors.
		if self._response_errors(self.result):
			raise exceptions.ResponseError(errors.response_errors[self.result['err']])

		# Check if resulting response contains warnings.
		if self._response_warnings(self.result):
			raise exceptions.ResponseWarning(errors.response_warnings[self.result['err']])

		return self.result

	def explain(self, field_name):
		if field_name not in documentation:
			field_name = self._lookup(field_name)
			if not field_name:
				raise exceptions.InvalidFieldName(errors.documentation_not_found.format(field_name = field_name))

		return documentation[field_name]

	"""
	HELPER FUNCTIONS
	"""

	def _transform(self, transform_action, field_value):
		# If transformation is disabled, immediately return the value
		# un-modified.
		if not self.transform:
			return field_value

		# Dynamically retrieve the appropriate transformation function.
		transformer = getattr(transform, transform_action)

		return transformer(field_value)

	def _validate(self, field_rules, field_value):
		# If a datatype has been defined or if validation is disabled, then
		# the value automatically passes validation.
		if not self.validate or 'datatype' not in field_rules:
			return True

		# Dynamically retrieve the appropriate validation function.
		validator = getattr(validate, field_rules['datatype'])

		return validator(field_rules, field_value)

	# Resolve minFraud argument names to pyminfraud-friendly field names.
	def _lookup(self, field_name):
		if field_name in fields.lookup:
			return fields.lookup[field_name]

	# Returns a list of required fields which have not yet been specified. If
	# all required fields have been specified, None is returned.
	def _missing(self):
		missing = set(fields.required) - set(self.fields.keys())
		if missing:
			return missing

	def _response_errors(self, response):
		if 'err' in response and response['err'] in errors.response_errors:
			return response['err']

	def _response_warnings(self, response):
		if 'err' in response and response['err'] in errors.response_warnings:
			return response['err']

	def _response_parse(self, response):
		if sys.version_info >= (3, ):
			try:
				response = response.decode('utf-8')
			except UnicodeError:
				response = response.decode('latin_1')
		return dict((key, value) for (key, value) in [row.split('=') for row in response.split(';')]) # Python 2 and 3?

	def _request_arguments(self):
		arguments = {}
		for field_name, field_value in compatibility.iterdict(self.fields):
			argument = fields.rules[field_name]['arg'];
			arguments[argument] = field_value
		data = compatibility.urlencode(arguments)
		if sys.version_info >= (3, ):
			data = data.encode('utf-8')
		return data


	def _request_url(self, protocol, host, uri):
		return protocol + '://' + host + '/' + uri
