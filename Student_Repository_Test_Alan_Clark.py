"""
   File Name:    HW09_Test_Alan_Clark.py
   Author:       Alan Clark
   CWID:         10457554
   Date:         14 April 2021
   Description:  Test the printed data from the University class
                 in HW09_Alan_Clark.py.
"""

from HW09_Alan_Clark import University
from prettytable import PrettyTable
import unittest


class HW09Test(unittest.TestCase):
    """ Class for testing HW09 functions """

    # Create an instance of the class.
    fake_u: University = University('Fredonia University', 'E:\Data\PythonHW')
    
    def test_display_instructors(self):
        """ Test the data from the class's display_instructors() method. """
        # Capture the output.
        pt: PrettyTable = self.fake_u.display_instructors()
        # Can't see a way to check into a PrettyTable object!
        # Instead, checking the instances of Instructor
        # stored within the instance of University.
        for index, (key, value) in enumerate(self.fake_u.all_instructors.items()):
            if key == 98765:
                print('Checking CWID 98765')
                self.assertTrue(value.name == 'Einstein, A')
                self.assertTrue(value.dept == 'SFEN')
                self.assertTrue(value.courses['SSW 567'] == 4)
                self.assertTrue(value.courses['SSW 540'] == 3)
            elif key == 98764:
                print('Checking CWID 98764')
                self.assertTrue(value.name == 'Feynman, R')
                self.assertTrue(value.dept == 'SFEN')
                self.assertTrue(value.courses['SSW 564'] == 3)
                self.assertTrue(value.courses['SSW 687'] == 3)
                self.assertTrue(value.courses['CS 501'] == 1)
                self.assertTrue(value.courses['CS 545'] == 1)
            elif key == 98763:
                print('Checking CWID 98763')
                self.assertTrue(value.name == 'Newton, I')
                self.assertTrue(value.dept == 'SFEN')
                self.assertTrue(value.courses['SSW 555'] == 1)
                self.assertTrue(value.courses['SSW 689'] == 1)
            elif key == 98760:
                print('Checking CWID 98760')
                self.assertTrue(value.name == 'Darwin, C')
                self.assertTrue(value.dept == 'SYEN')
                self.assertTrue(value.courses['SYS 800'] == 1)
                self.assertTrue(value.courses['SYS 750'] == 1)
                self.assertTrue(value.courses['SYS 611'] == 2)
                self.assertTrue(value.courses['SYS 645'] == 1)
            
    def test_display_students(self):
        """ Test the data from the class's display_students() method. """
        # Capture the output.
        pt: PrettyTable = self.fake_u.display_students()
        # Can't see a way to check into a PrettyTable object!
        # Instead, checking the instances of Student stored
        # within the instance of University.
        for index, (key, value) in enumerate(self.fake_u.all_students.items()):
            if key == 10103:
                print('Checking CWID 10103')
                self.assertTrue(value.name == 'Baldwin, C')
                self.assertTrue(value.major == 'SFEN')
                self.assertTrue(value.courses['SSW 567'] == 'A')
                self.assertTrue(value.courses['SSW 564'] == 'A-')
                self.assertTrue(value.courses['SSW 687'] == 'B')
                self.assertTrue(value.courses['CS 501'] == 'B')
            elif key == 10115:
                print('Checking CWID 10115')
                self.assertTrue(value.name == 'Wyatt, X')
                self.assertTrue(value.major == 'SFEN')
                self.assertTrue(value.courses['CS 545'] == 'A')
                self.assertTrue(value.courses['SSW 564'] == 'B+')
                self.assertTrue(value.courses['SSW 567'] == 'A')
                self.assertTrue(value.courses['SSW 687'] == 'A')
            elif key == 10172:
                print('Checking CWID 10172')
                self.assertTrue(value.name == 'Forbes, I')
                self.assertTrue(value.major == 'SFEN')
                self.assertTrue(value.courses['SSW 555'] == 'A')
                self.assertTrue(value.courses['SSW 567'] == 'A-')
            elif key == 10175:
                print('Checking CWID 10175')
                self.assertTrue(value.name == 'Erickson, D')
                self.assertTrue(value.major == 'SFEN')
                self.assertTrue(value.courses['SSW 687'] == 'B-')
                self.assertTrue(value.courses['SSW 564'] == 'A')
                self.assertTrue(value.courses['SSW 567'] == 'A')
            elif key == 10183:
                print('Checking CWID 10183')
                self.assertTrue(value.name == 'Chapman, O')
                self.assertTrue(value.major == 'SFEN')
                self.assertTrue(value.courses['SSW 689'] == 'A')
            elif key == 11399:
                print('Checking CWID 11399')
                self.assertTrue(value.name == 'Cordova, I')
                self.assertTrue(value.major == 'SYEN')
                self.assertTrue(value.courses['SSW 540'] == 'B')
            elif key == 11461:
                print('Checking CWID 11461')
                self.assertTrue(value.name == 'Wright, U')
                self.assertTrue(value.major == 'SYEN')
                self.assertTrue(value.courses['SYS 611'] == 'A')
                self.assertTrue(value.courses['SYS 750'] == 'A-')
                self.assertTrue(value.courses['SYS 800'] == 'A')
            elif key == 11658:
                print('Checking CWID 11658')
                self.assertTrue(value.name == 'Kelly, P')
                self.assertTrue(value.major == 'SYEN')
                self.assertTrue(value.courses['SSW 540'] == 'F')
            elif key == 11714:
                print('Checking CWID 11714')
                self.assertTrue(value.name == 'Morton, A')
                self.assertTrue(value.major == 'SYEN')
                self.assertTrue(value.courses['SYS 611'] == 'A')
                self.assertTrue(value.courses['SYS 645'] == 'C')
            elif key == 11788:
                print('Checking CWID 11788')
                self.assertTrue(value.name == 'Fuller, E')
                self.assertTrue(value.major == 'SYEN')
                self.assertTrue(value.courses['SSW 540'] == 'A')


# This runs all the test case functions from the classes in this file.
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
