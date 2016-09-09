from __future__ import unicode_literals

from django.db import models


class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'departments'


class DeptEmp(models.Model):
    emp_no = models.ForeignKey('Employees', db_column='emp_no')
    dept_no = models.ForeignKey(Departments, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'dept_emp'


class DeptManager(models.Model):
    dept_no = models.ForeignKey(Departments, db_column='dept_no')
    emp_no = models.ForeignKey('Employees', db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'dept_manager'


class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'employees'


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employees, db_column='emp_no')
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'salaries'


class Titles(models.Model):
    emp_no = models.ForeignKey(Employees, db_column='emp_no')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'
