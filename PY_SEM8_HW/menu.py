from function import *
import os

def main_menu(): # Главное меню
    play = True
    print("=======Phone book=======\n")
    while play:
        read_records()
        answer = input("Choose a Number:\n"
                       "1. Show All Records\n"
                       "2. Add a Record\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                play = False
            case _:
                print("Try again!\n")


def edit_menu(): # Меню редактирования
    
    add_dict = {"1": "Surname", "2": "Name", "3": "Patronymic", "4": "Phone Number"}

    show_all()
    record_id = input("Enter the Record ID: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. Surname\n"
                           "2. Name\n"
                           "3. Patronymic\n"
                           "4. Phone Number\n"
                           "5. Exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The Data is not Recognized, Repeat the Input.")
    else:
        print("The Data is not Correct!")

main_menu()