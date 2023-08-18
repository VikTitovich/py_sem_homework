import tkinter as tk
import work_with_file as wwf
import work_with_date as wwd

def show_notes():

    path = 'my_note.json'
    show_notes = tk.Tk()
    show_notes.title('Список заметок')
    show_notes.geometry('500x600+100+100')
    show_notes.rowconfigure(0, minsize=1, weight=1)
    show_notes.columnconfigure(0, minsize=20, weight=1)

    frm_label = tk.Frame(master=show_notes, relief=tk.RAISED)
    frm_label.pack()
    list_title = ["Номер записи","Название заметки", 'Содержание заметки', 'Дата редактирования']
    c = 0
    for item in list_title:
        tk.Label(text=item, master=frm_label).grid(column=c, row=0, padx=5, pady= 3)
        c +=1
    list_notes = wwf.get_notes_from_file(path)
    list_dates = wwd.sort_date_from_file(path)

    r = 1
    while len(list_dates)>0:
        for note in list_notes:
            #print(list_dates[0])
            str_date = note.get("date_redact")
            if wwd.str_in_date(str_date) == list_dates[0]:
                    tk.Label(master=frm_label, text=note.get('id')).grid(column=0, row=r)
                    tk.Label(master=frm_label, text=note.get('name')).grid(column=1, row=r)
                    tk.Label(master=frm_label, text=note.get('text')).grid(column=2, row=r)
                    tk.Label(master=frm_label, text=note.get("date_redact")).grid(column=3 , row=r)
                    r += 1
                    break
        list_dates.pop(0)

    show_notes.mainloop()


