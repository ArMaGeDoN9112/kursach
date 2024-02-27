from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self, title):
        super().__init__()

        # конфигурация окна
        self.title(title)
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        # определение кнопки
        self.button = ttk.Button(self, text="закрыть")
        self.button["command"] = self.button_clicked
        self.button.pack(anchor="s", expand=2)


    def button_clicked(self):
        self.destroy()


def new_window_on_click(text):
    new_window = Window(title=text)


main_window = Tk()
main_window.title("Приложение для турникета")
main_window.geometry('900x600')
main_window.resizable(width=False, height=False)

btn1 = Button(main_window, text="Добавить новые данные", width=30, height=18, command=lambda: new_window_on_click("хуй"))
btn2 = Button(main_window, text="Изменить данные", width=30, height=18, command=lambda: new_window_on_click("пизда"))
btn3 = Button(main_window, text="Удалить данные",  width=30, height=18, command=lambda: new_window_on_click("член"))
btn4 = Button(main_window, text="Открыть логи",  width=30, height=18, command=lambda: new_window_on_click("хуесос"))
btn5 = Button(main_window, text="Открыть локальную базу",  width=30, height=18, command=lambda: new_window_on_click("пидорас"))
btn6 = Button(main_window, text="Вернуться в режим консоли",  width=30, height=18, command=lambda: new_window_on_click("очко"))

btn1.grid(column=1, row=0)
btn2.grid(column=2, row=0)
btn3.grid(column=3, row=0)
btn4.grid(column=1, row=1)
btn5.grid(column=2, row=1)
btn6.grid(column=3, row=1)


main_window.mainloop()