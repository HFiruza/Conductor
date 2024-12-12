import tkinter
from fileinput import filename
from tkinter import ttk

from tkinter import filedialog
import os

from pyglet import window
from pyglet.window.mouse import buttons_string



def file_select():
    filename = filedialog.askopenfilename(initialdir=r"C:\Users\ladyf\PycharmProjects\UrbanLesson_7", title="Выберите файл", filetypes=(("Текстовый файл", ".txt"),
                                                                                            ("Все файлы", "*")))

    with open(filename, 'r', encoding='utf-8') as f:
        f.read()
        text['text'] = text['text'] + '' + filename
    os.startfile(filename)


def file_select_info():
    filename_info = filedialog.askopenfilename(initialdir=r'C:\Users\ladyf\PycharmProjects\UrbanLesson_7\info.txt',
                                               title='Info', filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))

    with open(filename_info, 'r', encoding='utf-8') as f:
        f.read()
    text['text'] = text['text'] + '' + filename_info
    os.startfile(filename_info)

def file_select_about():
    filename_about = filedialog.askopenfilename(initialdir=r'C:\Users\ladyf\PycharmProjects\UrbanLesson_7\about.txt',
                                               title='About', filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))

    with open(filename_about, 'r', encoding='utf-8') as f:
        f.read()
    text['text'] = text['text'] + '' + filename_about
    os.startfile(filename_about)

def new_file():
    filename_new = filedialog.askopenfilename(initialdir=r"C:\Users\ladyf\PycharmProjects\UrbanLesson_7\new_file.txt",
                                          title="Новый файл", filetypes=(("Текстовый файл", ".txt"),
                                                                            ("Все файлы", "*")))

    with open(filename_new, 'w', encoding='utf-8') as f:
        f.write('')
        text['text'] = text['text'] + '' + filename_new
    os.startfile(filename_new)

# Создание меню
window = tkinter.Tk()
window.title('Проводник')
window.geometry('650x405')
window.configure(bg='blue')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл: ', height=4, width=81, background='silver', foreground='black')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='silver', foreground='black',
                               command=file_select)
button_select_info = tkinter.Button(window, width=20, height=3, text='Info', background='silver', foreground='black',
                                    command=file_select_info)
button_select_about = tkinter.Button(window, width=20, height=3, text='About', background='silver', foreground='black',
                                    command=file_select_about)
button_select_new = tkinter.Button(window, width=20, height=3, text='Новый файл', background='silver', foreground='black',
                                    command=new_file)
button_select.grid(column=1, row=2, pady=1)
button_select_info.grid(column=1, row=3, pady=2)
button_select_about.grid(column=1, row=4, pady=3)
button_select_new.grid(column=1, row=5, pady=4)
window.mainloop()
