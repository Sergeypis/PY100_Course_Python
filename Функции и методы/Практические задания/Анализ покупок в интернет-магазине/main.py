# TODO Напишите функцию find_common_items
def find_common_items(last_week_purchases, current_week_purchases):
    common_items = list(set(last_week_purchases).intersection(current_week_purchases))
    common_items.sort()
    return common_items


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")
