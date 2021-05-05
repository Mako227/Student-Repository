"""
   File Name:    HW12_Alan_Clark.py
   Author:       Alan Clark
   CWID:         10457554
   Date:         5 May 2021
   Description:  Homework assignment for week 12
"""

from flask import Flask, render_template
from typing import Dict, List
import sqlite3

app: Flask = Flask(__name__, template_folder = 'templates')

@app.route('/students')
def student_grades() -> str:
    """ Get student grades from the database and convert into HTML. """
    table: List[Dict[str, str]] = list()
    db: sqlite3.Connection = sqlite3.connect('810_startup.db')
    for row in db.execute("select students.name, students.CWID, grades.Course, \
                            grades.Grade, instructors.Name from students \
                            join grades on students.CWID = grades.StudentCWID \
                            join instructors on instructors.CWID = grades.InstructorCWID;"):
        table.append({'name': row[0], 'cwid': row[1], 'course': row[2],
                      'grade': row[3], 'instructor': row[4]})
    # Remember to close the database.
    db.close()
    return render_template('student_courses.html',
                           title = 'Stevens Repository',
                           table_title = 'Student, Course, Grade, and Instructor',
                           students = table)

# Run the app.
app.run(debug = False)
