import googletrans
from googletrans import Translator

# Running the library
translator = Translator()

# Get the language code
def lang_code(language):
    language = language.lower()
    languagedict = googletrans.LANGUAGES

    for key in languagedict.keys():
        if language == languagedict[key]:
            return key

    return "None"

def translator_func(msg, language="english"):
    
    if language.lower == "chinese":
        lc = "zh-cn"
    else:
        lc = lang_code(language)

    if lc == "None":
        return "Sorry, Language Not Found"

    return language + ":" + translator.translate(text=msg, dest=lc).text


print(translator_func("Hello, how are you", "French"))
