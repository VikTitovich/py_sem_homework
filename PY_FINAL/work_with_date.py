from datetime import datetime
import work_with_file as wwf


def str_in_date(datetime_string):  #переводит строку с датой в формат даты
    
    datetime_obj = datetime.strptime(datetime_string, '%d/%m/%y %H:%M:%S')
    
    return datetime_obj

def get_list_of_dates(path):  # получает список всех дат редактирования записей
    notes = wwf.get_notes_from_file(path)
    list_dates = []
    for note in notes:
        str_date = note.get("date_redact")
        
        list_dates.append(str_in_date(str_date))
    return list_dates

def sort_list_date(list_dates):  #сортирует даты из списка в порядке убывания
    
    for i in range(len(list_dates)-1):
        
        pos_min = 0
        for k in range(len(list_dates)-i):
        
            if list_dates[k]<list_dates[pos_min]:
                pos_min=k
            temp = list_dates[pos_min]
            list_dates[pos_min] = list_dates[len(list_dates)-1-i]
            list_dates[len(list_dates)-1-i] = temp
            
    return list_dates

def sort_date_from_file(path):  
    list_date = get_list_of_dates(path)
    
    list_sort_date = sort_list_date(list_date)
    return list_sort_date
