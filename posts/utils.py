from translate import Translator


def get_translate(lang_from, lang_to, text):
    translator = Translator(from_lang=lang_from, to_lang=lang_to)
    return translator.translate(text)
