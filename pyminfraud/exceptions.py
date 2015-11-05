# coding: utf-8

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
