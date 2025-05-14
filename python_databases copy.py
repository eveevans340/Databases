# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'music_lessons.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" music_lessons "
           "LEFT JOIN genders ON music_lessons.gender_id = genders.gender_id "
           "LEFT JOIN instruments ON music_lessons.instrument_id = instruments.instrument_id "
           "LEFT JOIN schools ON music_lessons.school_id = schools.school_id "
           "LEFT JOIN lesson_days ON music_lessons.lesson_day_id = lesson_days.lesson_day_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  


def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice = ''
while menu_choice != '7':
    menu_choice = input('Welcome to the music lesson database!\n\n'
                        'Type the number for the information you want:\n'
                        '1: All information\n'
                        '2: Children with Monday lessons\n'
                        '3: Children with\n'
                        '4: Cars made by English manufacturers\n'
                        '5: Non-electric cars\n'
                        '6: The top ten fastest cars\n'
                        '7: Exit\n\nType option here: ')
    if menu_choice == '1':
        print_query('all_cars')
    elif menu_choice == '2':
        print_query('bugatti_cars')
    elif menu_choice == '3':
        print_query('cheap_fast_cars')
    elif menu_choice == '4':
        print_query('english_cars')
    elif menu_choice == '5':
        print_query('non_electric')
    elif menu_choice == '6':
        print_query('top_ten_fastest_cars')

make = input('Which make cars do you want to see: ')
print_parameter_query("model, top_speed", "make = ? ORDER BY top_speed DESC",make)