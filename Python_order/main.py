import re
import tkinter as tk
from tkinter.filedialog import askopenfilename
from textwrap import wrap

# filename = input("Имя файла для замены: ")
# words = input("Имя файла со словами для замены: ")
# result = input("Сохранить в: ")


def main():
    global text
    for w in words:
        try:
            if '/-' in w:
                word, key = map(str, w.split("/-"))
                text = text.split()
                for i in range(len(text)):
                    if not (text[i] in words_keep):
                        text[i] = re.sub(word.strip(), f'{key.strip()}', text[i])
                text = ' '.join(text)
                print(text)

            elif '\-' in w:
                word, key = map(str, w.split("\-"))
                if not (word.strip() in words_keep):
                    text = re.sub(f'(?<=^\b|\W){word.strip()}(?=\W|\b$)', f'{key.strip()}', text, flags=re.IGNORECASE)

            elif '/r-' in w:
                regexp, key = map(str, w.split("/r-"))
                if not (regexp.strip() in words_keep):
                    text = re.sub(regexp.strip(), key.strip(), text)
        except:
            print('Unable to open file')

    with open(f"{result.get()}.srt", "w", encoding="utf-8") as f:
        f.write(text)


def add_words():
    global words

    words_filename = askopenfilename()
    path_words["text"] = "Выбранный файл: "+words_filename
    with open(words_filename, encoding="utf-8") as g:
        words = g.read().split("\n")


def add_words_keep():
    global words_keep

    words_filename = askopenfilename()
    path_words_keep["text"] = "Выбранный файл: "+words_filename
    with open(words_filename, encoding="utf-8") as g:
        words_keep = g.read().split("\n")


def add_main_text():
    global text

    text_filename = askopenfilename()
    path_text["text"] = "Выбранный файл: "+text_filename
    with open(text_filename, encoding="utf-8") as f:
        text = f.read()


text = ""
words = []
words_keep = []
text_filename = ""
root = tk.Tk()
root.geometry('460x400')

btn_words_keep = tk.Button(root, text="Выбрать словарь зарезервивованных слов",
                   command=add_words_keep).place(x=30, y=10)
path_words_keep = tk.Label(state="disabled")
path_words_keep["text"] = "Выбранный файл:"
path_words_keep.place(x=30, y=40)

btn_text = tk.Button(root, text="Выбрать текст для замены",
                  command=add_main_text).place(x=30, y=90)
path_text = tk.Label(state="disabled")
path_text["text"] = "Выбранный файл:"
path_text.place(x=30, y=120)

btn_words = tk.Button(root, text="Выбрать словарь для замены",
                   command=add_words).place(x=30, y=170)
path_words = tk.Label(state="disabled")
path_words["text"] = "Выбранный файл:"
path_words.place(x=30, y=200)

result = tk.StringVar()
result_text = tk.Label(
    text="Под каким названием сохранить файл (без .srt):").place(x=30, y=310)
result_entry = tk.Entry(textvariable=result, width=30).place(x=32, y=335)
btn_save = tk.Button(root, text="Запустить", width=10, height=2,
                  command=main).place(x=320, y=340)
names = tk.Label(
    text="alexlife\nЕвгений Сапронов\n\nИнструкция:", fg="red").place(x=300, y=20)


# Текст для инструкции:
text = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'
instr_entry = tk.Label(text=text,
                    fg="black")
instr_entry.place(x=260, y=90)

root.update()
width = instr_entry.winfo_width()


if instr_entry.winfo_width() > root.winfo_width():
    average_char_width = instr_entry.winfo_width() / len(text)
    chars_per_line = int(200 / average_char_width)
    while instr_entry.winfo_width() > 200:
        wrapped_text = '\n'.join(wrap(text, chars_per_line))
        instr_entry['text'] = wrapped_text
        root.update()
        chars_per_line -= 1


# Дальше много строчек страшного base64 кода изображения, необходимо для отображения иконки в приложении.
with open("icon.txt") as file:
    icon = file.readlines()[0]

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=icon))
root.title("Замена символов")
root.mainloop()
