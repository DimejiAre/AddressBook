import json
import ast
import sys


def add_entry():
    book = open("/Users/dimeji/PycharmProjects/addressbook.txt", "w+")

    name = raw_input("Enter name: \n")
    address = raw_input("Enter Address: \n")
    phone = raw_input("Enter Phone number: \n")
    email = raw_input("Enter email address: \n")

    entry1 = {"name": name, "address": address, "phone": phone, "email": email}
    list1.append(entry1)
    book.write(json.dumps(list1))
    book.close()

    print "Contact has been successfully added"


def view():
    output1 = file("/Users/dimeji/PycharmProjects/addressbook.txt").read()
    output_json = json.loads(output1)
    print json.dumps(output_json, indent=4)


def search_entry():
    contact = raw_input("Enter Name: ")
    output1 = file("/Users/dimeji/PycharmProjects/addressbook.txt").read()
    output_json = json.loads(output1)

    try:
        entry = [i for i in output_json if i["name"] == contact]
        print json.dumps(entry[0], indent=4)
    except:
        print "Name doesn't exist in database"


def delete_entry():
    contact = raw_input("Enter Name: ")
    output1 = file("/Users/dimeji/PycharmProjects/addressbook.txt").read()
    output_json = json.loads(output1)

    try:
        [output_json.remove(i) for i in output_json if i["name"] == contact]
        book = open("/Users/dimeji/PycharmProjects/addressbook.txt", "w+")
        book.write(json.dumps(output_json))
        book.close()

    except:
        print "An error occurred deleting entry"


if __name__ == '__main__':
    print "WELCOME TO ADDRESS BOOK."

    output = file("/Users/dimeji/PycharmProjects/addressbook.txt").read()
    # list1 = ast.literal_eval(output)

    if output != "":
        list1 = ast.literal_eval(output)
    else:
        list1 = []
        print "it is empty, Add entry:"
        add_entry()

    while True:
        answer = raw_input("""\n\nchoose an action:\n1.View All Contacts\n2.Add Contact\n3.Search Contact
        \r4.Delete Contact\n5.exit\n""")

        if answer == '1':
            view()
        elif answer == '2':
            add_entry()
        elif answer == '3':
            search_entry()
        elif answer == '4':
            delete_entry()
        elif answer == '5':
            break
        else:
            print "invalid input"

