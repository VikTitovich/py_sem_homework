import json
import datetime

def save_note_on_file(note, path):  #сохранение записи в файле
    with open(path, 'a') as file:
        if get_id(path) != 1:
            file.write("\n")
        json.dump(note, file)

def seak_in_file(id, path):  # проверяет есть ли запись с данным индексом в файле
    list_notes = get_notes_from_file(path)
    for note in list_notes:
        if note.get('id') == id:
            return True
    else: return False

def note_from_file(id, path):  #возвращает запись по индексу
    list_notes = get_notes_from_file(path)
    for note in list_notes:
        if note.get('id') == id:
            result = note
    return result
  
def print_dict_val(list_dict): # печатает запись
    for note in list_dict:
        str_info = ''
        for value in note.values():
            str_info = str_info +': '+ str(value)
        print(str_info)        

def get_notes_from_file(path): #возвращает все записи списком
    list_notes = []
    with open(path, 'r') as file:
        for line in file:
            js_line = json.loads(line)
            list_notes.append(js_line)
    return list_notes

def get_id(path):  # для автозаполнения индекса записи
    try:
        list_notes = get_notes_from_file(path)
        id_last_note = list_notes[-1].get('id')
        
    except:
        id_last_note=0    
    return id_last_note+1

def clear_file(path):  # очищает файл полностью
    with open(path, 'w') as file:
        file.write('')

def del_note(path, id_note): #удаление записи с проверкой, но можно и без неё
    list_notes = get_notes_from_file(path)
    try:
        for note in list_notes:
            if note.get('id') == id_note:
                print(note)
                list_notes.pop(list_notes.index(note))
        clear_file(path)
   
        for note in list_notes:
            save_note_on_file(note, path)
        
    except:
        print('Something wrong')
        
def get_info(id, path): #возвращает строку с записью, но не все данные
    list_notes = get_notes_from_file(path)
    for note in list_notes:
        if note.get('id') == id:
            str_info = str(note.get('id')) + ' ' + str(note.get('name')) + ': ' + str(note.get('text'))
            return str_info

def redact_note_in_file(id, name, text, path): #редактирование записи
    list_notes = get_notes_from_file(path)
    for note in list_notes:
        if note.get('id')== id:
            note['name'] = name
            note['text'] = text
            note['date_redact'] = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')
    clear_file(path)
    for note in list_notes:
        save_note_on_file(note, path)
    
