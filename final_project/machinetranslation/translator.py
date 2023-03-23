import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ.get("apikey")
url = os.environ.get("url")

authenticator = IAMAuthenticator(apikey)

# Create a Language Translator client instance
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translates English text to French"""
    return language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

def french_to_english(french_text):
    """Translates French text to English"""
    return language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()