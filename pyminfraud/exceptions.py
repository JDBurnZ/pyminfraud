# coding: utf-8

import warnings

class AuthException(Exception):
	pass

class InvalidFieldName(Exception):
	pass

class InvalidFieldValue(Exception):
	pass

class MissingRequiredFields(Exception):
	pass

class ResponseError(Exception):
	pass

def ResponseWarning(message):
	warnings.warn(message, 'UserWarning', stacklevel=2)
