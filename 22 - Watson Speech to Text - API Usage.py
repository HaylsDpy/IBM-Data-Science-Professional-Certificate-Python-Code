# Watson Speech to Text
from ibm_watson import SpeechToTextV1

url_s2t='https://stream.watsonplatform.net/speech-to-text/api'

#This would be your API key
iam_apikey_s2t = '###xxx'

s2t = SpeechToTextV1(iam_apikey_s2t, url = url_s2t)


filename = 'hello_this_is_python.wav'

with open(filename, mode = 'rb') as wav:
   response = s2t.recognize(audio = wav, content_type = 'audio/wav')

response.result

recognized_text = response.result['results'][0]['alternatives'][0]['transcript']

print(recognized_text)

#Watson Language Translator
from ibm_watson import LanguageTranslatorV3

url_lt = 'https://gateway.watsonplatform.net/language-translator/api'

apikey_lt = 'ahuBKS8IWOnIqe3NHrNaGGHBJbn1v7Goe5G7rs1Np374'

version_lt = '2018-05-01'

language_translator = LanguageTranslatorV3(iam_apikey = apikey_lt, url = url_lt, version = version_lt)

language_translator.list_identifiable_languages().get_result()


recognized_text = 'hello this is python'

translation_response = language_translator.translate(text = recognized_text, model_id = 'en-es')

translation = translation_response.get_result()

print(translation)


spanish_translation = translation['translations'][0]['translation']

print(spanish_translation)

translation_new = language_translator.translate(text = spanish_translation, model_id = 'es-en').get_result()

translation_eng = translation_new['translations'][0]['translation']

print(translation_eng)


French_translation = language_translator.translate(text = translation_eng, model_id = 'en-fr').get_result()

French_translation['translations'][0]['translation']
