import codecs


def get_list_number_plus_name():
    contacts = ""
    with codecs.open("HW_sem8\телефоны.txt", "r", "utf-8") as data:
        for i in data:
            contacts += i

    contacts = contacts.split("\n")
    contacts.pop(len(contacts)-1)
    contacts = list(map(lambda x: x.split(" - "), contacts))
    return contacts


def add_number(number, name):
    with codecs.open("HW_sem8\телефоны.txt", "a", "utf-8") as data:
        data.write(str(number)+" - " + name+"\n")
    data.close


def print_numbers():
    with codecs.open("HW_sem8\телефоны.txt", "r", "utf-8") as data:
        contacts = ""
        for i in data:
            contacts += i
        print(contacts)
    data.close


def sorted(name):
    contacts = get_list_number_plus_name()
    contacts = list(filter(lambda x: x[1] == name, contacts))

    if (len(contacts) == 0):
        print(f"Фамилия {name} не найдена\n")
        return False

    result = ""
    for i in range(len(contacts)):
        contacts[i] = " - ".join(contacts[i])

    for i in range(len(contacts)-1):
        result += contacts[i]+"\n"
    result += contacts[len(contacts)-1]

    print(result)
    return True


def replace_name(name, new_name):
    with codecs.open("HW_sem8\телефоны.txt", "r", "utf-8") as data:
        text = data.read()
        text = text.replace(name, new_name)
    data.close

    with codecs.open("HW_sem8\телефоны.txt", "w", "utf-8") as data:
        data.write(text)


def delete_by_number(number):
    contacts = get_list_number_plus_name()
    new_contacts = list(filter(lambda x: x[0] != number, contacts))

    if (len(contacts) == len(new_contacts)):
        print("номер не найден")
        return

    result = ""
    for i in range(len(new_contacts)):
        result += new_contacts[i][0]+" - " + new_contacts[i][1]+"\n"
    with codecs.open("HW_sem8\телефоны.txt", "w", "utf-8") as data:
        data.write(result)
    data.close
    print(f"номер {number} удален")


def delete_by_name(name):
    contacts = get_list_number_plus_name()
    new_contacts = list(filter(lambda x: x[1] != name, contacts))
    if (len(contacts) == len(new_contacts)):
        print("Пользователь не найден")
        return

    result = ""
    for i in range(len(new_contacts)):
        result += new_contacts[i][0]+" - " + new_contacts[i][1]+"\n"
    with codecs.open("HW_sem8\телефоны.txt", "w", "utf-8") as data:
        data.write(result)
    data.close
    print(f"Контакт {name} удален")
