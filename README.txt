REST API test app.

Small guide with examples:


Add new department(POST/JSON):
request:
{
	"dept_name": "Food Service",
	"add_position": "department", 
	"dept_no": "d011"
}
repsonse:
{
	"response": "OK",
	"message": "New department saved."
}


Add new employee(POST/JSON):
request:
{
	"add_position": "employee", 
	"emp_no": "500100",
	"dept_no": "d005",
	"birth_date": "1991-05-04",
	"hire_date": "2018-05-05",
	"dismiss_date": "2020-05-05",
	"first_name": "John",
	"last_name": "Doe-Smith",
	"gender": "M"
}
repsonse:
{
	"response": "OK",
	"message": "New employee saved."
}


Delete employee(DELETE/JSON):
request:
{ 
	"emp_no": "500100"
}
repsonse:
{
	"response": "OK",
	"message": "Employee deleted."
}


Get all Employees/Departments(GET/JSON):
request: *empty*
repsonse:
{
	"departments_list": [],
	"employees_list": [],
	"dep_emp_list": [],
	"response": "OK"
}

