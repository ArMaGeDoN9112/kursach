from   customtkinter import *
from main import input_data_about_employee, permission_list, get_dict_from_json
from time import sleep


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Приложение для турникета")
        self.geometry('900x600')
        self.resizable(width=False, height=False)

        for c in range(3): self.columnconfigure(index=c, weight=1)
        for r in range(2): self.rowconfigure(index=r, weight=1)

        btn1 = CTkButton(self, text="Добавить новые данные", width=300, height=300,
                         command=lambda: new_window_on_click(0))
        btn2 = CTkButton(self, text="Изменить данные", width=300, height=300,
                         command=lambda: new_window_on_click(1))
        btn3 = CTkButton(self, text="Удалить данные", width=300, height=300,
                         command=lambda: new_window_on_click(2))
        btn4 = CTkButton(self, text="Открыть логи", width=300, height=300,
                         command=lambda: new_window_on_click(3))
        btn5 = CTkButton(self, text="Открыть локальную базу", width=300, height=300,
                         command=lambda: new_window_on_click(4))
        btn6 = CTkButton(self, text="Перейти в режим консоли", width=300, height=300,
                         command=lambda: new_window_on_click(5), bg_color="black", fg_color="blue",
                         corner_radius=50)

        btn1.grid(column=0, row=0)
        btn2.grid(column=1, row=0)
        btn3.grid(column=2, row=0)
        btn4.grid(column=0, row=1)
        btn5.grid(column=1, row=1)
        btn6.grid(column=2, row=1)


class AddNewDataWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Добавить новую информацию")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        btn7 = CTkButton(self, text='проба', width=30)
        btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

        for i in range(1, 10):
            for j in range(1, 10):
                btn = CTkButton(self, text=f'{i} {j}')
                btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.back_button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def back_button_clicked(self):
        set_main_window_state()
        self.destroy()


class ChangeDataWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Изменить информацию")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        btn7 = CTkButton(self, text='Измена', width=30)
        btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

        for i in range(1, 10):
            for j in range(1, 10):
                btn = CTkButton(self, text=f'{i} {j}')
                btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.back_button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def back_button_clicked(self):
        set_main_window_state()
        self.destroy()


class DeleteDataWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Очистить данные с карты")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        btn7 = CTkButton(self, text='Удаление', width=30)
        btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

        for i in range(1, 10):
            for j in range(1, 10):
                btn = CTkButton(self, text=f'{i} {j}')
                btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.back_button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def back_button_clicked(self):
        set_main_window_state()
        self.destroy()


class OpenLogsWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Логи")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        btn7 = CTkButton(self, text='Логи', width=30)
        btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

        for i in range(1, 10):
            for j in range(1, 10):
                btn = CTkButton(self, text=f'{i} {j}')
                btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.back_button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def back_button_clicked(self):
        set_main_window_state()
        self.destroy()


class OpenLocalDataWindow(CTk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Локальная база данных")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        for i in range(11):
            self.columnconfigure(index=i, weight=1)
            self.rowconfigure(index=i, weight=1)

        btn7 = CTkButton(self, text='База', width=30)
        btn7.grid(column=0, row=0, columnspan=11, ipadx=6, ipady=6, padx=4, pady=4)

        for i in range(1, 10):
            for j in range(1, 10):
                btn = CTkButton(self, text=f'{i} {j}')
                btn.grid(column=j, row=i, ipadx=6, ipady=6, padx=4, pady=4)

        # определение кнопки
        self.button = CTkButton(self, text="закрыть", width=50, height=2, command=self.back_button_clicked)
        self.button.grid(column=0, row=10, columnspan=11)

    def back_button_clicked(self):
        set_main_window_state()
        self.destroy()



def hide(btn):
    btn.grid_forget()


def set_main_window_state(state="normal"):
    for item in main_window.winfo_children():
        item.configure(state = state)


def new_window_on_click(mode: int):
    match mode:
        case 0:
            new_window = AddNewDataWindow()
        case 1:
            new_window = ChangeDataWindow()
        case 2:
            new_window = DeleteDataWindow()
        case 3:
            new_window = OpenLogsWindow()
        case 4:
            new_window = OpenLocalDataWindow()
        case 5:
            pass

    set_main_window_state('disabled')


main_window = MainWindow()

main_window.mainloop()