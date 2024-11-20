import employee_info as EI
from employee_info import employee_data as EMP_DATA

def test_get_employee_by_age_range():
    result=[]
    upper_limit = 33
    lower_limit = 29
    expected = [EMP_DATA[0],EMP_DATA[4]]
    result = EI.get_employees_by_age_range(lower_limit,upper_limit)
    assert(result==expected)

def test_calc_avg_salary():
    expected = 60166.67
    result = EI.calculate_average_salary()
    assert(result==expected)

def test_get_employee_dept():
    result = []
    expected = [EMP_DATA[3],EMP_DATA[4]]
    result = EI.get_employees_by_dept("Engineering")
    assert(result==expected)
