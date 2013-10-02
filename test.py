# coding: utf-8

import sys
import unittest
import tests
import tests.dictdiffer

import pyminfraud

license_key = sys.argv[1]

if len(sys.argv) < 2:
	raise Exception('License Key should be passed as argument')

class PyMinFraudTests(unittest.TestCase):
	def test_valid_fields(self):
		minfraud = pyminfraud.Client(license_key)
		minfraud.add_fields(tests.valid_fields_dict)
		result = minfraud.execute()

		self.failUnless(isinstance(result, dict))
		self.failUnless(len(result['err'].strip()) == 0)

	def test_valid_field_mappings(self):
		minfraud1 = pyminfraud.Client(license_key)
		minfraud1.add_fields(tests.valid_fields_dict)

		minfraud2 = pyminfraud.Client(license_key)
		minfraud2.add_fields(tests.valid_arguments_dict)

		dict_differ = tests.dictdiffer.DictDiffer(minfraud1.get_fields(), minfraud2.get_fields())

		self.failUnless(len(dict_differ.added()) == 0)
		self.failUnless(len(dict_differ.removed()) == 0)
		self.failUnless(len(dict_differ.changed()) == 0)
		self.failUnless(len(dict_differ.unchanged()) == len(minfraud1.get_fields()))

def main():
    unittest.main(argv=[sys.argv[0]])

if __name__ == '__main__':
    main()
