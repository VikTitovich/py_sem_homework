import tkinter as tk
from tkinter import messagebox

import datetime
import work_with_file as wf

def add_note():
    path = 'my_note.json'
    def save_note():
        
        id = wf.get_id(path)
        note = {'id':id, 'name': name_entry.get(), 
                'text':text_box.get("1.0", tk.END), 'date_create': datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S'), 
                'date_redact':datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}
        wf.save_note_on_file(note, 'my_note.json')
        messagebox.showinfo("Запись сохранена", "Запись была внесена в файл")
        add_note.destroy()
  
    def exit():
        add_note.destroy()
    
    # Создание окна с необходимыми заголовками, полями ввода и кнопками
    add_note = tk.Tk()
    
    add_note.title('Создание заметки')
    add_note.geometry('450x300+300+200')
    add_note.rowconfigure(0, minsize=1, weight=1)
    add_note.columnconfigure(0, minsize=20, weight=1)

    frm_form = tk.Frame(master=add_note, relief=tk.SUNKEN)
    frm_form.pack()
    name_lb = tk.Label(master=frm_form, text='Заголовок').grid(row=0, column=0)
    name_entry = tk.Entry(master=frm_form, width=50)
    name_entry.grid(row=0, column=2)
    text_lb = tk.Label(master=frm_form, text='Содержание').grid(row=1, column=0)
    text_box = tk.Text(master=add_note, width=50, height=10)
    text_box.pack()
    frm_button = tk.Frame(master=add_note, relief=tk.RAISED)
    frm_button.pack()
    
    save_btm = tk.Button(master=frm_button, width=10, text='Сохранить',height=1, command=save_note)
    save_btm.grid(row=2, column=1)
    cancle_btm = tk.Button(master=frm_button, width=10, text='Отмена',height=1, command=exit)
    cancle_btm.grid(row=2, column=2)

    add_note.mainloop()

