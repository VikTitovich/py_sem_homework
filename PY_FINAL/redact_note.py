import tkinter as tk
import work_with_file as wwf
from tkinter import messagebox


def redact_note():
    path = 'my_note.json'

    def redact_note_from_id():
        def save_note():
            id = int(entry_id.get())
            name = entry_name.get()
            text = entry_text.get("1.0", tk.END)
            wwf.redact_note_in_file(id, name, text, path)
            messagebox.showinfo('', 'Изменения внесены')
            red_note.destroy()

        id = int(entry_id.get())
        if wwf.seak_in_file(id, path):
            frm_lable = tk.Frame(master=red_note, relief=tk.RAISED)
            frm_lable.pack()
            list_titel = ['Номер записи', 'Заголовок']
            for i in range(len(list_titel)):
                tk.Label(master=frm_lable, text=list_titel[i]).grid(column=i, row=0)
            note_to_reduct = wwf.note_from_file(id, path)
            tk.Label(master=frm_lable, text=note_to_reduct.get('id')).grid(column=0, row=1)
            entry_name = tk.Entry(master=frm_lable)
            entry_name.insert(0, note_to_reduct.get('name'))
            entry_name.grid(column=1, row=1)
            tk.Label(master=red_note, text='Содержание').pack()
            entry_text = tk.Text(master=red_note, relief=tk.RAISED, width=50, height=10)
            entry_text.insert("1.0", note_to_reduct.get('text'))
            entry_text.pack()
            btn_save = tk.Button(master=red_note, relief=tk.RAISED, command=save_note, text='Внести измения')
            btn_save.pack()

    red_note = tk.Tk()
    red_note.geometry('400x400+200+100')
    red_note.title('Редактирование записи')

    lbl_ask_id = tk.Label(master=red_note, text='Введите номер записи').pack()
    entry_id = tk.Entry(master=red_note, relief=tk.SUNKEN)
    entry_id.pack()
    btn_get_id = tk.Button(master=red_note, text='Найти запись для редактирования', relief=tk.RAISED, command=redact_note_from_id)
    btn_get_id.pack()


    red_note.mainloop()
