from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records(): # Считывание данных

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])

        return all_data

def show_all(): # Отображение содержимого

    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")
        print()        

def add_new_contact(): #Добавление новой записи

    global last_id

    array = ['Surname', 'Name', 'Patronymic', 'Phone Number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("The Entry Has Been Successfully Added to the Phone Book!\n")
        
    else:
        print("The Data Already Exists!")

def del_contact(): #Удаление записи

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the Record ID: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record Deleted!\n")
    else:
        print("The Data is not Correct!")

def change_contact(data_tuple): #Изменение записи

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The Data Already Exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record Changed!\n")

def search_contact(): # Поиск
    search_data = exist_contact(0, input("Enter the Search Data: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("The Data is not Correct!")

def exist_contact(rec_id, data): #Проверка записи и ID
    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num): #Проверка полученных данных

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "Surname Name Patronymic":
            if answer.isalpha():
                break
            answer = input(f"Data is Incorrect!\n"
                       f"Use Only the Letters"
                       f" of the Alphabet!\n"
                       f"Enter a {num}: ")
        if num == "Phone Number":
            if answer.isdigit(): 
                break
            answer = input(f"Data is Incorrect!\n"
                       f"Use only the Digits\n"
                       f"Enter a {num}: ")
    return answer


