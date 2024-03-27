# TODO реализовать функцию
def get_unique_words(string):
    set_word = set(string.split())
    list_word = list(set_word)
    list_word.sort()
    return list_word


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
