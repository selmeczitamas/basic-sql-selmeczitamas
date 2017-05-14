import sys
import os
import ui  # User Interface
import sql   # Database


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        sql.name_of_mentors()
    elif option == "2":
        sql.nickname_of_mentors_from_miskolc()
    elif option == "3":
        sql.information_from_carol()
    elif option == "4":
        sql.information_from_unknown_girl()
    elif option == "5":
        sql.add_new_applicant()
    elif option == "6":
        sql.change_phonenumber()
    elif option == "7":
        sql.delete_user()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["The First and Last name of mentors",
               "The nickname of the Mentors from Miskolc",
               "Information from Carol",
               "Information from the unknown girl by email address",
               "Add new applicants",
               "Change phone number",
               "Delete user"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
