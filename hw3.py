# Import necessary modules
from django.db import models
from django.db.migrations import Migration

# Define models for Teachers, Students, Homework, and other related tables
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

# Create migration files for the database
class InitialMigration(Migration):
    dependencies = [
    ]
    operations = [
        models.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        models.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        models.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('teacher', models.ForeignKey(on_delete=models.CASCADE, to='app.Teacher')),
            ],
        ),
        models.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
                ('homework', models.ForeignKey(on_delete=models.CASCADE, to='app.Homework')),
                ('student', models.ForeignKey(on_delete=models.CASCADE, to='app.Student')),
            ],
        ),
    ]

class SeedDataMigration(Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]
    operations = [
        models.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        models.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        models.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('teacher', models.ForeignKey(on_delete=models.CASCADE, to='app.Teacher')),
            ],
        ),
        models.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
                ('homework', models.ForeignKey(on_delete=models.CASCADE, to='app.Homework')),
                ('student', models.ForeignKey(on_delete=models.CASCADE, to='app.Student')),
            ],
        ),
    ]

    def apply(self, project_state, schema_editor, collect_sql=False):
        # Create a teacher
        teacher = Teacher.objects.create(name='John Doe', email='johndoe@example.com')

        # Create a student
        student = Student.objects.create(name='Jane Doe', email='janedoe@example.com')

        # Create a homework
        homework = Homework.objects.create(title='Math Homework', description='Solve the following problems', deadline='2023-06-30 23:59:59', teacher=teacher)

        # Create a submission
        submission = Submission.objects.create(student=student, homework=homework, file='math_homework.pdf')