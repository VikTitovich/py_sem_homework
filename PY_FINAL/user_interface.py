import tkinter as tk
import show_notes as sn
import add_note as an
import delete_note as dn
import redact_note as rn

def user_interface():
        # Функция для управления кнопками
    def choice(x):
        if x == "Список заметок": sn.show_notes()
        if x == "Создать новую заметку": an.add_note()
        if x == "Редактировать заметки": rn.redact_note()
        if x == "Удалить заметку": dn.del_not()
        
        
        #Создание основного диалогового окна
    notes = tk.Tk()
    notes.title('Мои заметки')
    notes.geometry('350x300+200+100')
    notes.rowconfigure(0, minsize=5, weight=1)
    notes.columnconfigure(0, minsize=100, weight=1)

        #На окне находятся следующие кнопки
    frm_button = tk.Frame(master = notes, relief=tk.RAISED, border=10, )
    frm_button.pack()
    btn_list = ['Список заметок', 'Создать новую заметку', 'Редактировать заметки', 'Удалить заметку']
    r = 4
    for i in btn_list:
        cmd = lambda x = i: choice(x)
        tk.Button(master = frm_button, text = i, width=30, height=2, command=cmd).grid(row=r, column=0, padx=3, pady=10)
        r +=1
    notes.mainloop() #появление окна на экран
user_interface()