from translate import Translator


def split_into_sentences(text):
    delimiters = ".!?;"
    current_sentence = ""
    sentences = []

    for char in text:
        current_sentence += char
        if char in delimiters:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    if current_sentence:
        sentences.append(current_sentence.strip())

    return sentences


def get_translate(lang_from, lang_to, text):
    translator = Translator(from_lang=lang_from, to_lang=lang_to)
    sentences = split_into_sentences(text)
    translated_sentences = [translator.translate(i) for i in sentences]

    if "PLEASE SELECT TWO DISTINCT LANGUAGES" in translated_sentences:
        return text

    translated_text = ' '.join(translated_sentences)
    return translated_text
