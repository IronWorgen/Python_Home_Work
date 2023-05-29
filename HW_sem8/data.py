import codecs

def add_number(number , name):
    with codecs.open("HW_sem8\телефоны.txt", "a", "utf-8") as data:
        data.write(str(number)+" - "+ name+"\n")
    data.close 


def print_numbers():
        with codecs.open("HW_sem8\телефоны.txt", "r", "utf-8") as data:
            contacts=""
            for i in data:
                contacts+=i
            print(contacts)
        data.close 


def sort(name):
    contacts = ""
    with codecs.open("HW_sem8\телефоны.txt", "r", "utf-8") as data:
        for i in data:
            contacts+=i

    contacts = contacts.split("\n")
    contacts.pop(len(contacts)-1)
    contacts = list(map(lambda x : x.split(" - "), contacts))
    contacts = list(filter ( lambda x: x[1]==name, contacts))

    if (len(contacts)==0):
        print (f"Фамилия {name} не найдена\n")
        return
    
    result = ""
    for i in range(len(contacts)):
        contacts[i]=" - ".join(contacts[i])

    for i in range (len(contacts)-1):
        result+=  contacts[i]+"\n"
    result+=contacts[len(contacts)-1]   

    print (result)

