pyminfraud v1.0.0
=================

`pyminfraud` is a Python 2.6+ and Python 3 compatible library for interfacing
with MaxMind's minFraud Web Service API (http://dev.maxmind.com/minfraud/)

With `pyminfraud`, you decide how your data is treated. Want to push data
directly to the minFraud API without having to worry about validation or
transformations? It does that. Validating your own data? Disable validation.
Want to hash those MD5s yourself? Disable transformations.

This library has been designed to be as explicit or implicit as you want it to
be. If you encounter behaviour other than is desired, please let us know. Or even
better, contribute by patching it yourself!

License
-------
`pyminfraud` by Joshua D. Burns is licensed under the Creative Commons Attribution
3.0 Unported License. To view a copy of this license, please visit:

http://creativecommons.org/licenses/by/3.0/

Source Code
-----------
`pyminfraud` source code, documentation and examples are available on GitHub at:

https://www.github.com/JDBurnZ/pyminfraud

System Requirements
-------------------

`pyminfraud` is designed to be compatible with both the 2.6+ and 3 branches
of Python. Compatibility functions have been implemented for the retention of
clean, readable and manageable code. If you encounter a version-specific
incompatibility, please consider patching the issue and moving the
compatibility-specific functionality into the pyminfraud.compatibility module.

Supports:
* Python 2.6+
* Python 3

Tested On:
* Python 2.7

Needs Testing On:
* Python 2.6
* Python 3.x Variants

Optional Validation Libraries
-----------------------------

To harness the full power of `pyminfraud`'s data validation features, there are
a few libraries we attempt to interface with. If none of those libraries are
available, `pyminfraud` assumes the data is valid without performing any actual
validation.

**IP Address Validation**

Python 3.3+ comes with a standard built-in "ipaddress" library, which
`pyminfraud` takes full advantage of. If running Python 3.3+, IP validation just
works.

Any of the following libraries will fit the needs of IP Address validation for
Python 2.6+ and Python 3 up to and including Python 3.2 (with the exception of
ipaddress for Python 2.6):
* ipaddress 1.0.6: https://pypi.python.org/pypi/ipaddress (not compatible with
  Python 2.6)
* ipaddr 2.1.7: https://pypi.python.org/pypi/ipaddr
* IPy 0.81: https://pypi.python.org/pypi/IPy/

**ISO 3166 (Countries) / ISO 4217 (Currencies)**

Python 2.6+ and Python 3:
* pycountry 1.0:  https://pypi.python.org/pypi/pycountry

Known Issues
------------

* Needs additional unit testing
* Not tested in Python 3 or Python 2.6

To Do
-----

* Test validate.avs()
* Write more unit tests

Quick Reference / Documentation
-------------------------------

**Import pyminfraud**

	import pyminfraud

**Instantiate the pyminfraud Client**

	minfraud = pyminfraud.Client('minfraud-license-key')

**Add a Field/Argument**

	minfraud.add_field('billing_city', 'Grand Rapids')

**Add Multiple Fields/Arguments**

	fields = {
		'billing_city': 'Grand Rapids',
		'billing_state': 'MI',
	}
	minfraud.add_fields(fields)

**Execute a Request**

	minfraud.execute()

**Retrieve the Response**

	# When calling execute(), response is returned as a results dictionary.
	result = minfraud.execute()

	# Alternately, the result can also be retrieved from the instantiated
	# object itself.
	minfraud.execute()
	result = minfraud.result

	# Retrieve the response data, before it was packed into a nifty little
	# dictionary.
	minfraud.execute()
	response = minfraud.response

**Validation or Transformation**

For a look into exactly what field validations and transformations take place,
and what their use cases are for, peak at:
* pyminfraud.fields.py:rules
* pyminfraud.transform.py
* pyminfraud.validate.py

Validation and transformation are enabled by default.

	# Set validation and transformation on object instantiation
	minfraud = pyminfraud.Client('minfraud-license-key', validate=False, transform=False)

	# Toggle validation after object instantiation
	minfraud.validate = False
	minfraud.validate = True

	# Toggle transformation after object instantiation
	minfraud.transform = False
	minfraud.transform = True

**Full Example**

	import pyminfraud

	minfraud = pyminfraud.Client('minfraud-license-key')
	minfraud.add_field('ip', '12.12.12.12')
	billing = {
		'billing_city': 'Grand Rapids',
		'billing_state': 'MI',
		'billing_zip': '49503',
		'billing_country':, 'USA',
	}
	minfraud.add_fields(billing)

	result = minfraud.execute()
	for key in result:
		print(key, '=', result[key])

**Valid Fields**

Fields may be defined in one of two ways.
* minFraud Arguments: As defined at http://dev.maxmind.com/minfraud/
* pyminfraud Fields: Human-readble, more logical field names which more clearly
  define the contents to be included within that particular field.

`pyminfraud` allows you to mix and match pyminfraud-specific fields and
minFraud arguments, or explicitly use one set or the other. All fields specified
are normalized and appended to a single data-structure. If you were to pass "i"
and then separately pass "ip", the value from "ip" would overwrite the value
previously specified in "i".

Required pyminfraud Fields

* **ip** (v4 or v6 IP Address): IP address of the user.
* **billing_city** (String): Billing City.
* **billing_state** (String): Billing State, Region or Province
* **billing_zip** (String): Billing Zip or Postal Code.
* **billing_country** (ISO 3166): ISO 3166-1 alpha-2, alpha-3, numeric or short name of the Billing Country.

Optional pyminfraud Fields

* **shipping_address** (String): Shipping Address.
* **shipping_city** (String): Shipping City.
* **shipping_state** (String): Shipping State, Region or Province.
* **shipping_zip** (String): Shipping Zip or Postal Code.
* **shipping_country** (ISO 3166): ISO 3166-1 alpha-2, alpha-3, numeric or short name of the Shipping Country.
* **user_domain** (String): The domain name of the user's e-mail address entered.
* **user_phone** (String): The phone number entered by the user.
* **user_email** (String): The e-mail address entered by the user. This gets MD5'd before being sent to minFraud (if transform=True).
* **user_login** (String): The username entered by the user. This gets MD5'd before being sent to minFraud (if transform=True).
* **user_password** (String): The password entered by the user. This gets MD5'd before being sent to minFraud (if transform=True).
* **bin_cardnumber** (Numeric String): The credit card number entered by the user. This gets truncated down to the first six digits before being sent to minFraud (if transform=True).
* **bin_name** (String): The name of the credit card's issuing bank.
* **bin_phone** (String): The 800-number listed on the back of the credit card.
* **session_id** (String): Your system's internal Session ID. Helps identify requests from multiple proxies.
* **session_useragent** (String): The "User-Agent" HTTP header passed in the user's request.
* **session_language** (String): The "Accept-Language" HTTP header passed in the user's request.
* **transaction_id** (String): Your system's internal Transaction / Order ID.
* **transaction_amount** (Numeric Decimal String): The amount of the transaction.
* **transaction_currency** (ISO 4217): ISO 4217 currency code.
* **transaction_shopid** (String): If the system used supports multiple Shops/Portals on a single code base / interface, specify the unique identifier of the method used by the user.
* **transaction_type** (Limited To): "creditcard", "debitcard", "paypal", "google", "other", "lead", "survey" or "sitereg".
* **cc_avs** (AVS Code): Must contain one of the codes as defined at http://en.wikipedia.org/wiki/Address_Verification_System#Address_Verification_Service_.28AVS.29_codes
* **cc_cvv** (Limited To): "Y" or "N". Whether or not the CVV code was confirmed as a match by your AVS.
* **service_type** (Limited To): "standard" or "premium". The type of request to minFraud.
* **proxy_ip** (String): The "X-Forwarded-For" or "Client-IP" HTTP header (whichever is present, if present) passed in the user's request.
