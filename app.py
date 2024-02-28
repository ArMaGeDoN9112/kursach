from   customtkinter import *
from main import input_data_about_employee, permission_list, get_dict_from_json
from time import sleep


class Window(CTk):
    def __init__(self, title):
        super().__init__()

        # конфигурация окна
        self.title(title)
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def button_clicked(self):
        set_main_window_state()
        self.destroy()


def hide(btn):
    btn.grid_forget()


def set_main_window_state(state="normal"):
    print(main_window.winfo_children())
    for item in main_window.winfo_children():
        item.configure(state = state)

def new_window_on_click(text):
    new_window = Window(title=text)
    set_main_window_state('disabled')

    btn7 = CTkButton(new_window, text='проба', width=30)
    btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

    for i in range(1, 10):
        for j in range(1, 10):
            btn = CTkButton(new_window, text=f'{i} {j}')
            btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)



main_window = CTk()
main_window.title("Приложение для турникета")
main_window.geometry('900x600')
main_window.resizable(width=False, height=False)

for c in range(3): main_window.columnconfigure(index=c, weight=1)
for r in range(2): main_window.rowconfigure(index=r, weight=1)

btn1 = CTkButton(main_window, text="Добавить новые данные", width=300, height=300, command=lambda: new_window_on_click("Окно1"))
btn2 = CTkButton(main_window, text="Изменить данные", width=300, height=300, command=lambda: new_window_on_click("Окно2"))
btn3 = CTkButton(main_window, text="Удалить данные", width=300, height=300, command=lambda: new_window_on_click("Окно3"))
btn4 = CTkButton(main_window, text="Открыть логи", width=300, height=300, command=lambda: new_window_on_click("Окно4"))
btn5 = CTkButton(main_window, text="Открыть локальную базу", width=300, height=300, command=lambda: new_window_on_click("Окно5"))
btn6 = CTkButton(main_window, text="Перейти в режим консоли", width=300, height=300, command=lambda: new_window_on_click("Окно6"), bg_color="black", fg_color="blue", corner_radius=50)

btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=2, row=0)
btn4.grid(column=0, row=1)
btn5.grid(column=1, row=1)
btn6.grid(column=2, row=1)


main_window.mainloop()