def add_words_from_input(filename, word_from_input, regular_statement):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")
        lines[-1] = f'{word_from_input} - {regular_statement}'
    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            print(line)
            file.write(line + '\n')
