from terminaltables import AsciiTable


def print_table(table, title_list):
    table_data = [title_list]
    temp_table = table
    for items in table:
        table_data.append(items)
    table = AsciiTable(table_data)
    table.inner_row_border = True
    for num in range(len(temp_table)):
        table.justify_columns[num] = 'center'
    print(table.table)
    print()


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print(label, "\n", result)
    # your code


# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print()
    print(title + ":")
    count = 1
    for item in list_options:
        print("(" + str(count) + ")", item)
        count += 1
    print("(0)", exit_message)
    print()


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    labels = ""
    for label in list_labels:
        labels += label
    received_values = input(labels)
    values_list = received_values.split()

    for option in values_list:
        inputs.append(option)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print('Error: %s' % message)
    print()

