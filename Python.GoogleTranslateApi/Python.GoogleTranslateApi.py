from google.cloud import translate

# Instantiates a client
# Documenttation: https://cloud.google.com/translate/docs/translating-text#translate-translate-text-csharp
__translate_client__ = translate.Client()

# The text to translate
__text__ = u'Hello, world!'

print(u'Text: {}'.format(__text__))
print(u'Transaction: {}'.format(__translate_client__.translate(__text__, 'tr')['translatedText']))
print(u'Transaction: {}'.format(__translate_client__.translate(__text__, 'ru')['translatedText']))
print(u'Transaction: {}'.format(__translate_client__.translate(__text__, 'de')['translatedText']))
print(u'Transaction: {}'.format(__translate_client__.translate(__text__, 'es')['translatedText']))
