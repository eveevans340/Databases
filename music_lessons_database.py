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
           "LEFT JOIN lesson_days ON music_lessons.lesson_day_id = lesson_days.lesson_day_id "
           "LEFT JOIN parent_info ON music_lessons.parent_id = parent_info.parent_id ")
from easygui import *

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

msg ="What information do you want?"
title = "Music Lessons"
choices = ['All information',
             'Students with a lesson on a specific day',
             'Parents who still owe fees',
             'Lesson information',
             'All of the students information',
             'Lessons in chronological order',
             'Students youngest to oldest',
             'All students born in 2008',
             'Students who play a specific instrument',
             'Students who are siblings']
choice = choicebox(msg, title, choices)
if choice = 'All information':
    print_query('all data')
elif choice = 'Students with a lesson on a specific day':
    lesson_day = input('What day of lessons do you want to see: ').title()
    print_parameter_query('child_first_name, child_surname, instrument, lesson_time', 'lesson_day = ? ORDER BY lesson_time', lesson_day)
elif choice = 'Parents who still owe fees':
    print_query('unpaid_fees')
elif choice = 'Lesson information':
    print_query('lesson_info')
elif choice = 'All of the students information':
    print_query('student_all')
elif choice = 'Lessons in chronological order':
    print_query('lesson_order')
elif choice = 'Students youngest to oldest':
    print_query('student_age_ordered')
elif choice = 'All students born in 2008':
    print_query('born_2008')
elif choice = 'Students who play a specific instrument':
    instrument = input('What type of instrument lessons do you want to see: ').title()
    print_parameter_query('child_first_name, child_surname, instrument, lesson_day, lesson_time', 'instrument = ? ORDER BY lesson_day, lesson_time', instrument)
elif choice = 'Students who are siblings':
    print_query('siblings')



menu_choice = ''
while menu_choice != '11':
    menu_choice = input('Welcome to the music lesson database!\n\n'
                        'Type the number for the information you want:\n'
                        '1: All information\n'
                        '2: Students with a lesson on a specific day\n'
                        '3: Parents who still owe fees\n'
                        '4: Lesson information\n'
                        '5: All of the students information\n'
                        '6: Lessons in chronological order\n'
                        '7: Students youngest to oldest\n'
                        '8: All students born in 2008\n'
                        '9: Students who play a specific instrument\n'
                        '10: Students who are siblings\n'
                        '11: Exit\n\nType option here: ')
    if menu_choice == '1':
        print_query('all_data')
    elif menu_choice == '2':
        lesson_day = input('What day of lessons do you want to see: ').title()
        print_parameter_query('child_first_name, child_surname, instrument, lesson_time', 'lesson_day = ? ORDER BY lesson_time', lesson_day)
    elif menu_choice == '3':
        print_query('unpaid_fees')
    elif menu_choice == '4':
        print_query('lesson_info')
    elif menu_choice == '5':
        print_query('student_all')
    elif menu_choice == '6':
        print_query('lesson_order')
    elif menu_choice == '7':
        print_query('student_age_ordered')
    elif menu_choice == '8':
        print_query('born_2008')
    elif menu_choice == '9':
        instrument = input('What type of instrument lessons do you want to see: ').title()
        print_parameter_query('child_first_name, child_surname, instrument, lesson_day, lesson_time', 'instrument = ? ORDER BY lesson_day, lesson_time', instrument)
    elif menu_choice == '10':
        print_query('siblings')