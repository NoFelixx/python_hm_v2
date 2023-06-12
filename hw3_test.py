import pytest as pytest
from hw3 import Teacher, Student, Homework, Submission


@pytest.fixture
def teacher():
    return Teacher.objects.create(name='John Doe', email='johndoe@example.com')

@pytest.fixture
def student():
    return Student.objects.create(name='Jane Doe', email='janedoe@example.com')

@pytest.fixture
def homework(teacher):
    return Homework.objects.create(title='Math Homework', description='Solve the following problems', deadline='2023-06-30 23:59:59', teacher=teacher)

@pytest.fixture
def submission(student, homework):
    return Submission.objects.create(student=student, homework=homework, file='math_homework.pdf')

def test_teacher_model(teacher):
    assert teacher.name == 'John Doe'
    assert teacher.email == 'johndoe@example.com'

def test_student_model(student):
    assert student.name == 'Jane Doe'
    assert student.email == 'janedoe@example.com'

def test_homework_model(homework, teacher):
    assert homework.title == 'Math Homework'
    assert homework.description == 'Solve the following problems'
    assert homework.deadline == '2023-06-30 23:59:59'
    assert homework.teacher == teacher

def test_submission_model(submission, student, homework):
    assert submission.student == student
    assert submission.homework == homework
    assert submission.file == 'math_homework.pdf'