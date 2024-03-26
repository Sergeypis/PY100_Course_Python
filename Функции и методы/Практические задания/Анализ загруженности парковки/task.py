# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    if total_parking_spaces >= occupied_parking_spaces:
        return round((occupied_parking_spaces / total_parking_spaces) * 100)

