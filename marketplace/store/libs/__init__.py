from django.conf import settings
from cryptography.fernet import Fernet

try:
	KEY =  open(settings.KEY_STORE_FILE).read()
except:
	KEY = 'EMPTY SECRETE'

CIPHER_SUITE = Fernet(KEY)
