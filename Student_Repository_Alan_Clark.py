"""
   File Name:    HW09_Alan_Clark.py
   Author:       Alan Clark
   CWID:         10457554
   Date:         14 April 2021
   Description:  Homework assignment for week 9
"""

# CRC Cards:
# C = Class
# R = Responsibilities -- What does this class take care of?
# C = Collaborators -- What other classes does it interact with?

from typing import List, Tuple, Dict, DefaultDict, Iterator
from collections import defaultdict
import os
from prettytable import PrettyTable


def file_reader(path: str, fields: int, sep: str=',', header: bool=False) -> Iterator[List[str]]:
    """ This is a generator that reads a field-separated text file and
    yields a tuple with all of the values from a single line in the file
    on each call.  If a separation character is not specified, the
    function defaults to using a comma. """
    line_count: int = 0
    try:
        the_file = open(path, 'r')
    except FileNotFoundError:
        print('Unable to open file', path)
    else:
        with the_file:
            for line in the_file:
                line_count = line_count + 1
                # Strip away leading/trailing whitespace and newline and
                # split into words using 'sep' as the word boundary.
                words: List = line.strip().split(sep)
                field_count: int = len(words)
                if field_count != fields:
                    raise ValueError(f'File {path} line {line_count} has {field_count} fields instead of the expected {fields}.')
                # Skip the header line if the function call says to.
                elif header == True and line_count == 1:
                    continue
                else:
                    yield words
            the_file.close()


class Instructor:
    """ Store information about a single instructor, including all
    courses taught and the number of students in each course. """

    def __init__(self, cwid: int, name: str, dept: str) -> None:
        """ Function to initialize an instance of Instructor. """
        self.cwid: int = cwid
        self.name: str = name
        # Other attributes might be added later.
        self.dept: str = dept
        # The defaultdict of courses and number of students uses (int),
        # which sets the default value to 0.
        self.courses: DefaultDict[str, int] = defaultdict(int)
    

class Student:
    """ Store information about a single student, including all courses
    taken and the grade for each. """

    def __init__(self, cwid: int, name: str, major: str) -> None:
        """ Function to initialize an instance of Student. """
        self.cwid: int = cwid
        self.name: str = name
        # Other attributes might be added later.
        self.major: str = major
        # Each key is a course, each value is a grade.
        self.courses: Dict[str, str] = dict()

    
class University:
    """ Store information on instructors, students, and student grades
    for a single university. """

    # Use this set to check for legal school names.
    legal_name: set = set('abcdefghijklmnopqrstuvwxyz ')

    instructor_rows: int
    student_rows: int
    # These store data read from the other two classes.  For each, the
    # keys are CWIDs and the values are Instructor and Student class
    # instances.
    all_instructors: dict = dict()
    all_students: dict = dict()

    def __init__(self, name: str, path: str) -> None:
        """ Function to initialize an instance of University. """
        # Make sure the school name contains only letters and spaces,
        # and is at least 2 characters long WITHOUT spaces.
        if not University.legal_name.issuperset(name.lower()):
            raise ValueError('Invalid characters in school name', name)
        elif len(name.replace(' ', '')) < 2:
            raise ValueError('Incomplete school name:', name)
        self.name: str = name
        # If the data-file directory exists, record it.
        if not os.path.exists(path):
            raise ValueError('There is no directory path', path)
        self.target_path: str = path
        # Read tab-separated lines of instructors.txt file into a dict
        # of all this school's instructors, each of which is an instance
        # of the Instructor class.
        for line in file_reader(os.path.join(self.target_path, 'instructors.txt'), 3, '\t', False):
            cwid_i: int = int(line[0])
            self.all_instructors[cwid_i] = Instructor(cwid_i, line[1], line[2])
        # Do the same for students using the Student class.
        for line in file_reader(os.path.join(self.target_path, 'students.txt'), 3, '\t', False):
            cwid_s: int = int(line[0])
            self.all_students[cwid_s] = Student(cwid_s, line[1], line[2])
        # Now use the grades.txt file to add course/grade items to the
        # 'courses' dictionary of each student, and course/student count
        # items to the 'courses' dictionary of each instructor.
        for line in file_reader(os.path.join(self.target_path, 'grades.txt'), 4, '\t', False):
            cwid_s = int(line[0])
            cwid_i = int(line[3])
            if not cwid_s in self.all_students:
                raise KeyError('File grades.txt contains unknown student CWID:', cwid_s)
            elif not cwid_i in self.all_instructors:
                raise KeyError('File grades.txt contains unknown instructor CWID:', cwid_i)
            course: str = line[1]
            self.all_students[cwid_s].courses[course] = line[2]
            counter: int = self.all_instructors[cwid_i].courses[course]
            self.all_instructors[cwid_i].courses[course] = counter + 1

    def display_instructors(self) -> PrettyTable:
        """ Print a formatted table of all active instructors with CWID,
        name, department, courses taught, and students per course. """
        pt: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', '# of Students'])
        self.instructor_rows = 0
        for instructor, item in self.all_instructors.items():
            for course_listing in item.courses.keys():
                pt.add_row([item.cwid, item.name, item.dept, course_listing, item.courses[course_listing]])
                self.instructor_rows += 1
        # Print it just for comparison.
        print('')
        print(pt)
        return pt
            
    def display_students(self) -> PrettyTable:
        """ Print a formatted table of all active students with CWID,
        name, major, and a sorted list of courses. """
        pt: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Courses'])
        self.student_rows = 0
        new_list: list = list()
        for student, item in self.all_students.items():
            for course_listing in item.courses.keys():
                new_list.append(course_listing)
                self.student_rows += 1
            new_list.sort()
            pt.add_row([item.cwid, item.name, item.major, ', '.join(new_list)])
            new_list.clear()
        # Print it just for comparison.
        print('')
        print(pt)
        return pt
