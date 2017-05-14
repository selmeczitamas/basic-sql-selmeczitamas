import psycopg2
import ui


# def connectdb():
try:
    # setup connection string
    connect_str = "dbname='dizsit' user='dizsit' host='localhost' password='digit'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # Fetch and print the result of the last execution
    rows = cursor.fetchall()
    # return conn
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def name_of_mentors():
    cursor = conn.cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    ui.print_table(cursor.fetchall(), ["Firstname", "Lastname"])


def nickname_of_mentors_from_miskolc():
    cursor = conn.cursor()
    cursor.execute("""SELECT mentors.nick_name FROM mentors WHERE city='Miskolc';""")
    ui.print_table(cursor.fetchall(), ["Nickname"])


def information_from_carol():
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                    WHERE first_name='Carol' """)
    ui.print_table(cursor.fetchall(), ["Full Name", "Phone number"])


def information_from_unknown_girl():
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu' """)
    ui.print_table(cursor.fetchall(), ["Full Name", "Phone number"])


def add_new_applicant():
    details = ["ID", "First name", "Last name", "Phone number", "Email address", "Application Code"]
    cursor = conn.cursor()
    try:
        cursor.execute(""" INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
                    VALUES (12, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
        cursor.execute(""" SELECT * FROM applicants WHERE application_code = 54823 ;""")
        ui.print_table(cursor.fetchall(), details)
    except psycopg2.IntegrityError:
        cursor.execute(""" SELECT * FROM applicants WHERE application_code = 54823 ;""")
        ui.print_table(cursor.fetchall(), details)


def change_phonenumber():
    cursor = conn.cursor()
    cursor.execute(""" UPDATE applicants
                    SET phone_number = '003670/223-7459'
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    cursor.execute(""" SELECT phone_number FROM applicants
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    ui.print_table(cursor.fetchall(), ["Phone number"])


def delete_user():
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM applicants
                    WHERE email LIKE '%@mauriseu.net';""")
    cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
    details = ["ID", "First name", "Last name", "Phone number", "Email address", "Application Code"]
    ui.print_table(cursor.fetchall(), details)
