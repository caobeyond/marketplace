from django.db import models
from . import CIPHER_SUITE

class EncryptedCharField(models.CharField):
	def to_python(self, value):
		return value

	def from_db_value(self, value, expression, connection, context):
		return value

	def get_prep_value(self, value):
		if value is None:
			return value
		return CIPHER_SUITE.encrypt(str(value))
