from tkinter import *
from tkinter import ttk
from main import input_data_about_employee, permission_list, get_dict_from_json


class Window(Tk):
    def __init__(self, title):
        super().__init__()

        # конфигурация окна
        self.title(title)
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for c in range(11):
            self.columnconfigure(index=c, weight=1)
            self.rowconfigure(index=c, weight=1)

        # определение кнопки
        self.button = ttk.Button(self, text="закрыть")
        self.button["command"] = self.button_clicked

        self.button.grid(column=0, row=10, columnspan=11)

    def button_clicked(self):
        self.destroy()


def new_window_on_click(text):
    new_window = Window(title=text)
    btn7 = Button(new_window, text='проба', width=30)
    btn7.grid(column=0, row=0, columnspan=11)

    # for i in range(1, 10):
    #     for j in range(1, 10):
    #         btn = Button(new_window, text=f'{i} {j}')
    #         btn.grid(column=i, row=j)


main_window = Tk()
main_window.title("Приложение для турникета")
main_window.geometry('900x600')
main_window.resizable(width=False, height=False)

for c in range(3): main_window.columnconfigure(index=c, weight=1)
for r in range(2): main_window.rowconfigure(index=r, weight=1)

btn1 = Button(main_window, text="Добавить новые данные", command=lambda: new_window_on_click("Окно1"))
btn2 = Button(main_window, text="Изменить данные", command=lambda: new_window_on_click("Окно2"))
btn3 = Button(main_window, text="Удалить данные", command=lambda: new_window_on_click("Окно3"))
btn4 = Button(main_window, text="Открыть логи", command=lambda: new_window_on_click("Окно4"))
btn5 = Button(main_window, text="Открыть локальную базу", command=lambda: new_window_on_click("Окно5"))
btn6 = Button(main_window, text="Вернуться в режим консоли", command=lambda: new_window_on_click("Окно6"))


btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=2, row=0)
btn4.grid(column=0, row=1)
btn5.grid(column=1, row=1)
btn6.grid(column=2, row=1)


main_window.mainloop()