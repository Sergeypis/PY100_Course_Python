# Функция, которая удаляет в строке все лишние пробелы
def remove_whitespace(string):
    list_ = string.split(" ")
    list_word = []
    for word in list_:
        if word:
            list_word.append(word)
    result = " ".join(list_word)
    return result


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))


# def remove_whitespace(str_):
#     words_list = str_.split(" ")
#     print(words_list)
#     words_list_without_empty_string = []
#     for word in words_list:
#         if word:
#             words_list_without_empty_string.append(word)
#
#     return " ".join(words_list_without_empty_string)


