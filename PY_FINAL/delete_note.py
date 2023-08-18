import tkinter as tk
from tkinter import messagebox
import work_with_file as wwf

def del_not():
    path = 'my_note.json'
    
    def del_note_from_file():
        id = int(entry_ind.get())
        print(id)
        wwf.del_note(path, id)
        messagebox.showinfo('удаление', 'Запись удалена')
        del_not.destroy()
        
    def are_you_shure():
        id_del = int(entry_ind.get())
        
        if wwf.seak_in_file(id_del, path):
            lbl_question = tk.Label(master=del_not, text='Перед удалением проверьте запись').pack()
            lbl_note = tk.Label(master=del_not, text=wwf.get_info(id_del, path)).pack()
            btn_yes = tk.Button(master=del_not, text='Точно удалить', relief=tk.RAISED, command=del_note_from_file)
            btn_yes.pack()
        else:
            messagebox.showerror('Ошибка', 'Записи с таким номером нет')
            del_not.destroy()

    del_not = tk.Tk()
    del_not.geometry('300x200+100+200')
    del_not.title('Удаление записи')

    lbl_enter = tk.Label(text='Введите индекс удаляемой записи', master=del_not).pack()
    entry_ind = tk.Entry(master=del_not, relief=tk.RAISED)
    entry_ind.pack()
    btn_entry = tk.Button(master=del_not, text='Удалить', command=are_you_shure)
    btn_entry.pack()

    del_not.mainloop()

