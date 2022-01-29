import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#from dotenv import load_dotenv

#load_dotenv()

apikey = "IhQL58x6uSgPgfTr_ff4zf7avnJdkZ4rrx94Phibzrmv" #os.environ['apikey']
url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c99b430b-d06c-4d29-9bfa-6ebe697b33c1" #os.environ['url']



authenticator = IAMAuthenticator('IhQL58x6uSgPgfTr_ff4zf7avnJdkZ4rrx94Phibzrmv')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c99b430b-d06c-4d29-9bfa-6ebe697b33c1')


def english_to_french(english_text):
    ''' englishToFrench which takes in the englishText as a string argument '''
    french_text = language_translator.translate(
    text=english_text,model_id='en-fr').get_result()
    json_text=json.dumps(french_text)
    #print(json.dumps(french_text, indent=2)) 
    json_object = json.loads(json_text)
    for jobj in json_object:
      resptext  = jobj
    print(resptext)
    #print(json_object['translations']['translation'])
    # Returns
    return json_object


def french_to_english(french_text):
    ''' frenchToEnglish which takes in the frenchText as a string argument '''
    english_text = language_translator.translate(
    text=french_text,model_id='fr-en').get_result()
    res = english_text["translations"]
    json_text=json.dumps(english_text)
        #print(json.dumps(french_text, indent=2)) 
    json_object = json.loads(json_text)
    for jobj in json_object:
        resptext  = jobj
    print(resptext)
#return
    return json_object
