#print(GOOGLE_APPLICATION_CREDENTIALS)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()