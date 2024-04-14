INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as input_file:  # TODO перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE, "w") as output_file:
            for line in input_file:
                output_file.writelines(line.upper())


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
