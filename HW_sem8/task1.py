import data


def add_phone():
    phone_number = int(input("Телефон: "))
    name = input("Имя: ")

    data.add_number(phone_number , name)
    

def print_all():    
    print("\nВаши контакты")
    data.print_numbers()
    
    

def  search_by_last_name():
    
    print("\nВведите имя для поиска")
    name = input("Поиск: ")
    data.sort(name)


operation_list = {"1": {"добавить контакт": add_phone}, "2": {"вывести список контактов": print_all} , "3" : {"поиск по фамилии": search_by_last_name}}



def run ():
    print ("Привет")
    triger = True
    while triger:
        
        for i in operation_list.keys():
            operation_name = list(operation_list.get(i).keys())[0]
            print(f"{i} - {operation_name}")
        print ("q - завершить работу") 

        user_input = input()

        if user_input=='q':
            triger = False
        elif user_input in list(operation_list.keys()):

            list(operation_list.get(user_input).values())[0]()
        else:
            print ("Выберите вариант из списка")    

        
    
run ()
    


    
