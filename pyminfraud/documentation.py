# coding: utf-8

# TODO: These field descriptions were pulled directly from MaxMind's minFraud
# documentation page (http://dev.maxmind.com/minfraud/), and could be greatly
# elaborated/expanded upon.
documentation = {
	'license_key': 'String. Your MaxMind license key. Get your own license key from https://www.maxmind.com/en/my_license_key',
	'ip': 'String. String. Must be a properly v4 or v6 formatted. The IP address of the customer placing the order. This should be passed as a string like "44.55.66.77" or "2001:db8::2:1".',
	'billing_city': 'String. The billing city for the customer.',
	'billing_state': 'String. The billing region/state for the customer.',
	'billing_zip': 'String. The billing postal (zip) code for the customer.',
	'billing_country': 'String. The billing country for the customer. This can be passed as the full country name or as an ISO 3166 (http://en.wikipedia.org/wiki/ISO_3166) code.',
	'shipping_address': 'String. The shipping street address.',
	'shipping_city': 'String. The shipping address city.',
	'shipping_state': 'String. The shipping address region/state.',
	'shipping_zip': 'String. The shipping address postal (zip) code.',
	'shipping_country': 'The shipping address country. This can be passed as the full country name or as an ISO 3166 (http://en.wikipedia.org/wiki/ISO_3166) code.',
	'user_domain': 'The domain for the user\'s email address. This field should not be hashed.',
	'user_phone': 'The customer\'s phone number, including area code and local exchange. This is used to verify that the customer\'s phone number is in the same billing location as the cardholder. Most formats are acceptable. We strip out all non-numeric characters from the input.',
	'user_email': 'An MD5 hash of the user\'s email address.',
	'user_login': 'An MD5 hash of the user\'s username.',
	'user_password': 'An MD5 hash of the user\'s password.',
	'bin_cardnumber': 'The credit card BIN number. This is the first 6 digits of the credit card number. It identifies the issuing bank.',
	'bin_name': 'The name of the bank which issued the credit card, based on the BIN number. This is used to verify that cardholder is in possession of credit card. You must set the "bin-cardnumber" field if you set this one.',
	'bin_phone': 'The customer service phone number listed on the back of the credit card. This is used to verify that cardholder is in possession of credit card. You must set the bin field if you set this one.',
	'session_id': 'Your internal session ID.',
	'session_useragent': 'The "User-Agent" HTTP header.',
	'session_language': 'The "Accept-Language" HTTP header.',
	'transaction_id': 'Your internal transaction ID for the order. We can use this to locate a specific transaction in our logs, and it will also show up in email alerts and notifications from us to you.',
	'transaction_amount': 'The customer\'s order amount.',
	'transaction_currency': 'The currency used for the customer\'s order as an ISO 4217 code.',
	'transaction_shopid': 'Your internal ID for the shop, affiliate, or merchant this order is coming from.',
	'transaction_type': 'The transaction type. This can be set to one of the following strings: "creditcard", "debitcard", "paypal", "google" (Google Checkout), "other", "lead" (Lead Generation), "survey" (Online Survey) or "sitereg" (Site Registration). The "lead", "survey", and "sitereg" types are used for non-purchase transactions.',
	'cc_avs': 'The AVS check result, as returned to you by the credit card processor. The minFraud service supports the standard AVS codes (http://en.wikipedia.org/wiki/Address_Verification_System#Address_Verification_Service_.28AVS.29_codes).',
	'cc_cvv': 'The CVV check result. This should be either "N" or "Y". Do not pass the CVV code itself.',
	'service_type': 'This can be set to either "standard" or "premium". By default, we use the highest level of service available for your account. If you have both the premium and standard minFraud service, you can choose to use the standard service to save on costs.',
	'proxy_ip': 'The end user\'s IP address, as forwarded by a transparent proxy. Transparent proxies set the HTTP headers "X-Forwarded-For" or "Client-IP" to the IP address of the end user. This should be passed as a string like "44.55.66.77" or "2001:db8::2:1". Note that the forwarded IP should not be set in the "ip" field. We check that the IP address passed to the "ip" input field is a legitimate transparent proxy before using the value in the forwardedIP input field.',
}
