# coding: utf-8

rules = {
	# Instantiation Field(s)
	'license_key': {'arg': 'license_key',},

	# Required Field(s)
	'ip': {
		'arg':'i',
		'datatype':'ip',
	},
	'billing_city': {'arg':'city',},
	'billing_state': {'arg':'region',},
	'billing_zip': {'arg':'postal',},
	'billing_country': {
		'arg':'country',
		'datatype': 'iso3166',
	},

	# Shipping Field(s)
	'shipping_address': {'arg':'shipAddr',},
	'shipping_city': {'arg':'shipCity',},
	'shipping_state': {'arg':'shipRegion',},
	'shipping_zip': {'arg':'shipPostal',},
	'shipping_country': {
		'arg':'shipCountry',
		'datatype': 'iso3166',
	},

	# User Data Field(s)
	'user_domain': {'arg':'domain',},
	'user_phone': {'arg':'custPhone',},
	'user_email': {
		'arg':'emailMD5',
		'transform':'md5',
	},
	'user_login': {
		'arg':'usernameMD5',
		'transform':'md5',
	},
	'user_password': {
		'arg':'passwordMD5',
		'transform':'md5',
	},

	# BIN Field(s)
	'bin_cardnumber': {
		'arg':'bin',
		'transform':'bin',
	},
	'bin_name': {'arg':'binName',},
	'bin_phone': {'arg':'binPhone',},

	# Transaction Linking Field(s)
	'session_id': {'arg':'sessionID',},
	'session_useragent': {'arg':'user_agent',},
	'session_language': {'arg':'accept_language',},

	# Transaction Information Field(s)
	'transaction_id': {'arg':'txnID',},
	'transaction_amount': {'arg':'order_amount',},
	'transaction_currency': {
		'arg':'order_currency',
		'datatype': 'iso4217', # 3-Character currency code: http://en.wikipedia.org/wiki/ISO_4217
	},
	'transaction_shopid': {'arg':'shopID',},
	'transaction_type': {
		'arg':'txn_type',
		'datatype': 'enum',
		'values': ['creditcard', 'debitcard', 'paypal', 'google', 'other', 'lead', 'survey', 'sitereg',],
	},

	# Credit Card Check Field(s)
	'cc_avs': {
		'arg':'avs_result',
		'datatype': 'avs',
	},
	'cc_cvv': {
		'arg':'cvv_result',
		'datatype': 'enum',
		'values': ['Y', 'N',]
	},

	# Miscellaneous Field(s)
	'service_type': {
		'arg':'requested_type',
		'datatype': 'enum',
		'values': ['standard', 'premium'],
	},
	'proxy_ip': {
		'arg':'forwardedIP',
		'datatype':'ip',
	},
}

required = [
	'license_key',
	'ip',
]

# Resolve minFraud arguments to pyminfraud field names
lookup = {
	'license_key': 'license_key',
	'i': 'ip',
	'city': 'billing_city',
	'region': 'billing_state',
	'postal': 'billing_zip',
	'country': 'billing_country',
	'shipAddr': 'shipping_address',
	'shipCity': 'shipping_city',
	'shipRegion': 'shipping_state',
	'shipPostal': 'shipping_zip',
	'shipCountry': 'shipping_country',
	'domain': 'user_domain',
	'custPhone': 'user_phone',
	'emailMD5': 'user_email',
	'usernameMD5': 'user_login',
	'passwordMD5': 'user_password',
	'bin': 'bin_cardnumber',
	'binName': 'bin_name',
	'binPhone': 'bin_phone',
	'sessionID': 'session_id',
	'user_agent': 'session_useragent',
	'accept_language': 'session_language',
	'txnID': 'transaction_id',
	'order_amount': 'transaction_amount',
	'order_currency': 'transaction_currency',
	'shopID': 'transaction_shopid',
	'txn_type': 'transaction_type',
	'avs_result': 'cc_avs',
	'cvv_result': 'cc_cvv',
	'requested_type': 'service_type',
	'forwardedIP': 'proxy_ip',
}
