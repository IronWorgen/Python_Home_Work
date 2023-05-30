import data


def add_phone():
    phone_number = int(input("Телефон: "))
    name = input("Имя: ")
    data.add_number(phone_number, name)
    print()


def print_all():
    print("\nВаши контакты")
    data.print_numbers()


def search_by_last_name():

    print("\nВведите имя для поиска")
    name = input("Поиск: ")
    if (data.sorted(name)):
        print()

        triger =  True
        while triger:
            new_name=name 
            print(f"Введите:\n1 - чтобы изменить имя {name}\nq - вернуться")

            user_input = input() 
            if user_input=="1":
                new_name = input(f"{name} -> ")
                data.replace_name(name, new_name)
                print("Имя успешно изменено\n")
                name = new_name

                triger = False
            elif user_input=="q":
                print()
                return
            else :
                print ("Выберите вариант из списка")
    print()            


        


def delete_number():
    user_input = input("Введите номер: ")
    data.delete_by_number(user_input)
     
    

def delete_name():
    print("Введите фамилию")

    print("Удалить все номера по фамилии")      


operation_list = {"1": {"добавить контакт": add_phone}, "2": {
    "вывести список контактов": print_all}, "3": {"поиск по фамилии": search_by_last_name}}

operation_list["4"]={"Удалить номер": delete_number}
operation_list["5"]={"Удаление по фамилии ": delete_name}



def run():
    print("Привет")
    triger = True
    while triger:

        for i in operation_list.keys():
            operation_name = list(operation_list.get(i).keys())[0]
            print(f"{i} - {operation_name}")
        print("q - завершить работу")

        user_input = input()

        if user_input == 'q':
            triger = False
        elif user_input in list(operation_list.keys()):

            list(operation_list.get(user_input).values())[0]()
        else:
            print("Выберите вариант из списка")


run()
