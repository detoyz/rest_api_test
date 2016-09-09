from django.http import HttpResponse
from rest_api.models import *
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json

def rest_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['add_position'] == 'department':
            new_entry = Departments(
                dept_no=data['dept_no'],
                dept_name=data['dept_name']
            )
            new_entry.save()
            response_data = json.dumps({
                'response': 'OK',
                'message': 'New department saved.'
            }, indent=4, separators=(',', ': '), encoding='utf-8', cls=DjangoJSONEncoder)
            return HttpResponse(response_data, content_type="application/json")
        elif data['add_position'] == 'employee':
            for date in ['birth_date', 'hire_date', 'dismiss_date']:
                data[date] = datetime.strptime(data[date], '%Y-%m-%d')
            new_employee_entry = Employees(
                emp_no=data['emp_no'],
                birth_date=data['birth_date'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                gender=data['gender'],
                hire_date=data['hire_date']
            )
            new_employee_entry.save()
            new_dep_emp_entry = DeptEmp(
                emp_no=Employees.objects.get(emp_no=data['emp_no']),
                dept_no=Departments.objects.get(dept_no=data['dept_no']),
                from_date=data['hire_date'],
                to_date=data['dismiss_date']
            )
            new_dep_emp_entry.save()
            response_data = json.dumps({
                'response': 'OK',
                'message': 'New employee saved.'
            }, indent=4, separators=(',', ': '), encoding='utf-8', cls=DjangoJSONEncoder)
            return HttpResponse(response_data, content_type="application/json")
        else:
            response_data = json.dumps({
                'response': 'error',
                'message': 'Wrong JSON format'
            }, indent=4, separators=(',', ': '), encoding='utf-8', cls=DjangoJSONEncoder)
            return HttpResponse(response_data, content_type="application/json")

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        DeptEmp.objects.filter(emp_no=data['emp_no']).delete()
        Employees.objects.filter(emp_no=data['emp_no']).delete()
        response_data = json.dumps({
            'response': 'OK',
            'message': 'Employee deleted.'
        }, indent=4, separators=(',', ': '), encoding='utf-8', cls=DjangoJSONEncoder)
        return HttpResponse(response_data, content_type="application/json")
    else:
        employees_list = Employees.objects.all().values()
        departments_list = Departments.objects.all().values()
        dep_emp_list = DeptEmp.objects.all().values('emp_no', 'dept_no', 'from_date', 'to_date')
        response_data = json.dumps({
            'response': 'OK',
            'employees_list': list(employees_list),
            'departments_list': list(departments_list),
            'dep_emp_list': list(dep_emp_list)
        }, indent=4, separators=(',', ': '), encoding='utf-8', cls=DjangoJSONEncoder)
        return HttpResponse(response_data, content_type="application/json")
