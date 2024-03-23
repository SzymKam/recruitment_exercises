"""
Co się stanie, gdy wykonamy polecenie ‘python main.py’? (Przyjmijmy, że wszystkie moduły znajdują się w PYTHONPATH)

constants.py
from classes import Student

DEFAULT_DATE_FORMAT = '%Y-%M-%d'
GREETING_MESSAGE = "Welcome to the %s University" % (Student.UNIVERSITY,)



classes.py
from main import datefmt

class Student:
 UNIVERSITY = 'MIT'

 def __init__(self, name, date_string, *args):
   self.name = name
   self.birthdate = datefmt(date_string)



main.py
from datetime import datetime
from constants import DEFAULT_DATE_FORMAT

def datefmt(date_string):
 return datetime.strptime(date_string, DEFAULT_DATE_FORMAT)

s = Student('Mary', '1981-7-23')



A. Pojawi się TypeError, ponieważ konstruktor Studenta przyjmuje co najmniej 3 argumenty, a zostały przekazane dwa.
B. Pojawi się SyntaxError, ponieważ ‘class Student’ jest nieprawidłowa. Powinniśmy zapisać ‘class Student(object)’.
C. Pojawi się ImportError
D. Obiekty zostaną prawidłowo utworzone
"""
'C - import error'

