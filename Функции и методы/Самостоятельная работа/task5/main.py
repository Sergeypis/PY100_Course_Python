# TODO реализовать функцию
def get_sentences_list(text):
    text_list = text.split('.')
    text_list_without_whitespace = []
    for str_ in text_list:
        if str_:
            text_list_without_whitespace.append(str_.strip())
    return text_list_without_whitespace


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
