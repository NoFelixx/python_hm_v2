import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Raised in case of the late hw submission"""
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < (self.created + self.deadline)


class HomeworkResult:
    def __init__(self, author, homework: Homework, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError('Given object is NOT a "Homework" object')
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            hw_done = HomeworkResult(self, homework, solution)
            return hw_done
        else:
            raise DeadlineError("You are late.")


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult):
        hw = hw_result.homework
        if len(hw_result.solution) > 5 and hw_result not in cls.homework_done:
            cls.homework_done[hw].append(hw_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, hw=None):
        if isinstance(hw, Homework):
            cls.homework_done.pop(hw)

        elif hw is None:
            cls.homework_done.clear()
        else:
            raise TypeError('this method takes only a "Homework" object as an argument')