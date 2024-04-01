# TODO реализовать функцию
def insert(result_list, value, index=0):
    # result_list.append(value)
    # result_list[index], result_list[-1] = result_list[-1], result_list[index]
    # return result_list

    return result_list[:index] + [value] + result_list[index:]



print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
